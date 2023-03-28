FROM python:3.11-alpine as runtime-image
WORKDIR /code
COPY ./ /code/
RUN pip install --no-cache-dir --user --upgrade -r /code/requirements.txt
ENV PORT=50051
EXPOSE $PORT
ENV PATH=/root/.local/bin:$PATH
CMD ["python","main.py"]

