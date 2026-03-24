import typing

import java.lang
import kotlin
import kotlin.coroutines
import kotlin.jvm.functions
import kotlinx.coroutines.internal

class CancellableKt(java.lang.Object):
    _startCoroutineCancellable_1__T = typing.TypeVar('_startCoroutineCancellable_1__T')  # <T>
    _startCoroutineCancellable_2__R = typing.TypeVar('_startCoroutineCancellable_2__R')  # <R>
    _startCoroutineCancellable_2__T = typing.TypeVar('_startCoroutineCancellable_2__T')  # <T>
    @typing.overload
    @staticmethod
    def startCoroutineCancellable(this_startCoroutineCancellable: kotlin.coroutines.Continuation[kotlin.Unit], fatalCompletion: kotlin.coroutines.Continuation[java.lang.Object], /) -> None: ...
    @typing.overload
    @staticmethod
    def startCoroutineCancellable(this_startCoroutineCancellable: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_startCoroutineCancellable_1__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_startCoroutineCancellable_1__T], /) -> None: ...
    @typing.overload
    @staticmethod
    def startCoroutineCancellable(this_startCoroutineCancellable: kotlin.jvm.functions.Function2[_startCoroutineCancellable_2__R, kotlin.coroutines.Continuation[_startCoroutineCancellable_2__T], java.lang.Object], receiver: _startCoroutineCancellable_2__R, completion: kotlin.coroutines.Continuation[_startCoroutineCancellable_2__T], onCancellation: kotlin.jvm.functions.Function1[java.lang.Throwable, kotlin.Unit], /) -> None: ...

class UndispatchedKt(java.lang.Object):
    _startCoroutineUndispatched_0__T = typing.TypeVar('_startCoroutineUndispatched_0__T')  # <T>
    _startCoroutineUndispatched_1__R = typing.TypeVar('_startCoroutineUndispatched_1__R')  # <R>
    _startCoroutineUndispatched_1__T = typing.TypeVar('_startCoroutineUndispatched_1__T')  # <T>
    @typing.overload
    @staticmethod
    def startCoroutineUndispatched(this_startCoroutineUndispatched: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_startCoroutineUndispatched_0__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_startCoroutineUndispatched_0__T], /) -> None: ...
    @typing.overload
    @staticmethod
    def startCoroutineUndispatched(this_startCoroutineUndispatched: kotlin.jvm.functions.Function2[_startCoroutineUndispatched_1__R, kotlin.coroutines.Continuation[_startCoroutineUndispatched_1__T], java.lang.Object], receiver: _startCoroutineUndispatched_1__R, completion: kotlin.coroutines.Continuation[_startCoroutineUndispatched_1__T], /) -> None: ...
    _startCoroutineUnintercepted__T = typing.TypeVar('_startCoroutineUnintercepted__T')  # <T>
    @staticmethod
    def startCoroutineUnintercepted(this_startCoroutineUnintercepted: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_startCoroutineUnintercepted__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_startCoroutineUnintercepted__T], /) -> None: ...
    _startUndispatchedOrReturn__T = typing.TypeVar('_startUndispatchedOrReturn__T')  # <T>
    _startUndispatchedOrReturn__R = typing.TypeVar('_startUndispatchedOrReturn__R')  # <R>
    @staticmethod
    def startUndispatchedOrReturn(this_startUndispatchedOrReturn: kotlinx.coroutines.internal.ScopeCoroutine[_startUndispatchedOrReturn__T], receiver: _startUndispatchedOrReturn__R, block: kotlin.jvm.functions.Function2[_startUndispatchedOrReturn__R, kotlin.coroutines.Continuation[_startUndispatchedOrReturn__T], java.lang.Object], /) -> java.lang.Object: ...
    _startUndispatchedOrReturnIgnoreTimeout__T = typing.TypeVar('_startUndispatchedOrReturnIgnoreTimeout__T')  # <T>
    _startUndispatchedOrReturnIgnoreTimeout__R = typing.TypeVar('_startUndispatchedOrReturnIgnoreTimeout__R')  # <R>
    @staticmethod
    def startUndispatchedOrReturnIgnoreTimeout(this_startUndispatchedOrReturnIgnoreTimeout: kotlinx.coroutines.internal.ScopeCoroutine[_startUndispatchedOrReturnIgnoreTimeout__T], receiver: _startUndispatchedOrReturnIgnoreTimeout__R, block: kotlin.jvm.functions.Function2[_startUndispatchedOrReturnIgnoreTimeout__R, kotlin.coroutines.Continuation[_startUndispatchedOrReturnIgnoreTimeout__T], java.lang.Object], /) -> java.lang.Object: ...
