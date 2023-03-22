from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversionRequest(_message.Message):
    __slots__ = ["amount", "from_currency", "to_currency"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FROM_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    TO_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    amount: float
    from_currency: str
    to_currency: str
    def __init__(self, from_currency: _Optional[str] = ..., to_currency: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...

class ConversionResponse(_message.Message):
    __slots__ = ["amount"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: float
    def __init__(self, amount: _Optional[float] = ...) -> None: ...

class Currency(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class CurrencyRequest(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class CurrencyResponse(_message.Message):
    __slots__ = ["currencies"]
    CURRENCIES_FIELD_NUMBER: _ClassVar[int]
    currencies: _containers.RepeatedCompositeFieldContainer[Currency]
    def __init__(self, currencies: _Optional[_Iterable[_Union[Currency, _Mapping]]] = ...) -> None: ...
