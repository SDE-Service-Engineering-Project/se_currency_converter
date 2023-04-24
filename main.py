import logging
from concurrent import futures

import grpc

from controller.currency import Converter
from generated import currency_service_pb2_grpc
from helper.scheduling import run_schedules_continuously

logging.basicConfig(level=logging.INFO)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    currency_service_pb2_grpc.add_CurrencyConversionServicer_to_server(Converter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    run_schedules_continuously(1)
    serve()
