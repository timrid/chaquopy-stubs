import java.io
import java.lang
import typing



class ConnectTimeoutException(java.io.InterruptedIOException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str | java.lang.String, /) -> None: ...
