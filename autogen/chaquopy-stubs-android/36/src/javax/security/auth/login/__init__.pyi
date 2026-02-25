import java.lang
import java.security
import typing



class LoginException(java.security.GeneralSecurityException):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, msg: str | java.lang.String, /) -> None: ...
