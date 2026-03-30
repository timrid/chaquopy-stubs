import typing

import java.lang
import java.util.concurrent

_ListenableFuture__V = typing.TypeVar('_ListenableFuture__V')  # <V>
class ListenableFuture(java.util.concurrent.Future[_ListenableFuture__V], typing.Generic[_ListenableFuture__V]):
    def addListener(self, arg1: java.lang.Runnable, arg2: java.util.concurrent.Executor, /) -> None: ...
