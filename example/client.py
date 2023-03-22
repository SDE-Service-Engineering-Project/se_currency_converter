# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc

from generated.currency_service_pb2 import ConversionRequest, ConversionResponse, CurrencyResponse, CurrencyRequest
from generated.currency_service_pb2_grpc import CurrencyConversionStub


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CurrencyConversionStub(channel)
        response: ConversionResponse = stub.Convert(
            ConversionRequest(from_currency="USD", to_currency="EUR", amount=100))
        print(f"Converted amount: {response.amount}")

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = CurrencyConversionStub(channel)
        response: CurrencyResponse = stub.GetCurrencies(CurrencyRequest())
        print(f"Currencies amount: {[currency.name for currency in response.currencies]}")


if __name__ == '__main__':
    logging.basicConfig()
    run()
