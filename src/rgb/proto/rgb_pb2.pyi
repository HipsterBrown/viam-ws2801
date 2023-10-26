"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class AnimateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___AnimateRequest = AnimateRequest

@typing_extensions.final
class AnimateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    text: builtins.str
    def __init__(
        self,
        *,
        text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["text", b"text"]) -> None: ...

global___AnimateResponse = AnimateResponse

@typing_extensions.final
class FillRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    RED_FIELD_NUMBER: builtins.int
    GREEN_FIELD_NUMBER: builtins.int
    BLUE_FIELD_NUMBER: builtins.int
    name: builtins.str
    red: builtins.int
    green: builtins.int
    blue: builtins.int
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        red: builtins.int = ...,
        green: builtins.int = ...,
        blue: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["blue", b"blue", "green", b"green", "name", b"name", "red", b"red"]) -> None: ...

global___FillRequest = FillRequest

@typing_extensions.final
class FillResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    text: builtins.str
    def __init__(
        self,
        *,
        text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["text", b"text"]) -> None: ...

global___FillResponse = FillResponse

@typing_extensions.final
class ClearRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___ClearRequest = ClearRequest

@typing_extensions.final
class ClearResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    text: builtins.str
    def __init__(
        self,
        *,
        text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["text", b"text"]) -> None: ...

global___ClearResponse = ClearResponse

@typing_extensions.final
class StopRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["name", b"name"]) -> None: ...

global___StopRequest = StopRequest

@typing_extensions.final
class StopResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEXT_FIELD_NUMBER: builtins.int
    text: builtins.str
    def __init__(
        self,
        *,
        text: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["text", b"text"]) -> None: ...

global___StopResponse = StopResponse
