import logging
import threading
import time

import schedule
from schedule import repeat, every

from services.data_load import load_currencies


def run_schedules_continuously(interval=1):
    """Continuously run, while executing pending jobs at each
    elapsed time interval.
    @return cease_continuous_run: threading. Event which can
    be set to cease continuous run. Please note that it is
    *intended behavior that run_continuously() does not run
    missed jobs*. For example, if you've registered a job that
    should run every minute and you set a continuous run
    interval of one hour then your job won't be run 60 times
    at each interval but only once.
    """
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(interval)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run


# According to the ecb website, the exchange rates are updated daily around 16:00 CET,
# therefore the cache is cleared at 16:05 (because of the "around" formulation)
# https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
@repeat(every(1).days.at("17:00"))
# todo Remove the extra loads after this is confirmed working
def invalidate_exchange_rate_cache():
    logging.info("Invalidating exchange rate cache.")
    current_exchange_rates = load_currencies()
    load_currencies.cache_clear()
    new_exchange_rates = load_currencies()
    logging.info(f"The exchange rates are now updated: {current_exchange_rates != new_exchange_rates}")
