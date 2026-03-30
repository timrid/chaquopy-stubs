import typing

import java
import java.lang
import java.util.concurrent
import java.util.function
import kotlin
import kotlin.coroutines
import kotlin.jvm.functions
import kotlinx.coroutines

_CompletableFutureCoroutine__T = typing.TypeVar('_CompletableFutureCoroutine__T')  # <T>
class CompletableFutureCoroutine(kotlinx.coroutines.AbstractCoroutine[_CompletableFutureCoroutine__T], java.util.function.BiFunction[_CompletableFutureCoroutine__T, java.lang.Throwable, kotlin.Unit], typing.Generic[_CompletableFutureCoroutine__T]):
    def __init__(self, context: kotlin.coroutines.CoroutineContext, future: java.util.concurrent.CompletableFuture[_CompletableFutureCoroutine__T], /) -> None: ...
    def apply(self, value: _CompletableFutureCoroutine__T, exception: java.lang.Throwable, /) -> None: ...
    def onCancelled(self, cause: java.lang.Throwable, handled: bool | java.jboolean | java.lang.Boolean, /) -> None: ...
    def onCompleted(self, value: _CompletableFutureCoroutine__T, /) -> None: ...

_ContinuationHandler__T = typing.TypeVar('_ContinuationHandler__T')  # <T>
class ContinuationHandler(java.util.function.BiFunction[_ContinuationHandler__T, java.lang.Throwable, kotlin.Unit], typing.Generic[_ContinuationHandler__T]):
    cont: kotlin.coroutines.Continuation[_ContinuationHandler__T] = ...
    def __init__(self, cont: kotlin.coroutines.Continuation[_ContinuationHandler__T], /) -> None: ...
    def apply(self, result: _ContinuationHandler__T, exception: java.lang.Throwable, /) -> None: ...

class FutureKt(java.lang.Object):
    _asCompletableFuture_0__T = typing.TypeVar('_asCompletableFuture_0__T')  # <T>
    @typing.overload
    @staticmethod
    def asCompletableFuture(this_asCompletableFuture: kotlinx.coroutines.Deferred[_asCompletableFuture_0__T], /) -> java.util.concurrent.CompletableFuture[_asCompletableFuture_0__T]: ...
    @typing.overload
    @staticmethod
    def asCompletableFuture(this_asCompletableFuture: kotlinx.coroutines.Job, /) -> java.util.concurrent.CompletableFuture[kotlin.Unit]: ...
    _asDeferred__T = typing.TypeVar('_asDeferred__T')  # <T>
    @staticmethod
    def asDeferred(this_asDeferred: java.util.concurrent.CompletionStage[_asDeferred__T], /) -> kotlinx.coroutines.Deferred[_asDeferred__T]: ...
    _await___T = typing.TypeVar('_await___T')  # <T>
    @staticmethod
    def await_(this_await: java.util.concurrent.CompletionStage[_await___T], completion: kotlin.coroutines.Continuation[_await___T], /) -> java.lang.Object: ...
    _future__T = typing.TypeVar('_future__T')  # <T>
    @staticmethod
    def future(this_future: kotlinx.coroutines.CoroutineScope, context: kotlin.coroutines.CoroutineContext, start: kotlinx.coroutines.CoroutineStart, block: kotlin.jvm.functions.Function2[kotlinx.coroutines.CoroutineScope, kotlin.coroutines.Continuation[_future__T], java.lang.Object], /) -> java.util.concurrent.CompletableFuture[_future__T]: ...
