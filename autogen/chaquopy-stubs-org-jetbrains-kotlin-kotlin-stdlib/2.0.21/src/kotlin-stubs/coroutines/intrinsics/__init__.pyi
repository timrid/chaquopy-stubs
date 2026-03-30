import typing

import java.chaquopy
import java.lang
import kotlin
import kotlin.coroutines
import kotlin.enums
import kotlin.jvm.functions

class CoroutineSingletons(java.lang.Enum[CoroutineSingletons]):
    COROUTINE_SUSPENDED: typing.ClassVar[CoroutineSingletons] = ...
    UNDECIDED: typing.ClassVar[CoroutineSingletons] = ...
    RESUMED: typing.ClassVar[CoroutineSingletons] = ...
    @staticmethod
    def getEntries() -> kotlin.enums.EnumEntries[CoroutineSingletons]: ...
    @staticmethod
    def valueOf(value: str | java.lang.String, /) -> CoroutineSingletons: ...
    @staticmethod
    def values() -> java.chaquopy.JavaArray[CoroutineSingletons]: ...

class IntrinsicsKt(IntrinsicsKt__IntrinsicsKt): ...

class IntrinsicsKt__IntrinsicsJvmKt(java.lang.Object):
    def __init__(self) -> None: ...
    _createCoroutineUnintercepted_0__T = typing.TypeVar('_createCoroutineUnintercepted_0__T')  # <T>
    _createCoroutineUnintercepted_1__R = typing.TypeVar('_createCoroutineUnintercepted_1__R')  # <R>
    _createCoroutineUnintercepted_1__T = typing.TypeVar('_createCoroutineUnintercepted_1__T')  # <T>
    @typing.overload
    @staticmethod
    def createCoroutineUnintercepted(this_createCoroutineUnintercepted: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_createCoroutineUnintercepted_0__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_createCoroutineUnintercepted_0__T], /) -> kotlin.coroutines.Continuation[kotlin.Unit]: ...
    @typing.overload
    @staticmethod
    def createCoroutineUnintercepted(this_createCoroutineUnintercepted: kotlin.jvm.functions.Function2[_createCoroutineUnintercepted_1__R, kotlin.coroutines.Continuation[_createCoroutineUnintercepted_1__T], java.lang.Object], receiver: _createCoroutineUnintercepted_1__R, completion: kotlin.coroutines.Continuation[_createCoroutineUnintercepted_1__T], /) -> kotlin.coroutines.Continuation[kotlin.Unit]: ...
    _intercepted__T = typing.TypeVar('_intercepted__T')  # <T>
    @staticmethod
    def intercepted(this_intercepted: kotlin.coroutines.Continuation[_intercepted__T], /) -> kotlin.coroutines.Continuation[_intercepted__T]: ...
    _wrapWithContinuationImpl_0__T = typing.TypeVar('_wrapWithContinuationImpl_0__T')  # <T>
    _wrapWithContinuationImpl_1__R = typing.TypeVar('_wrapWithContinuationImpl_1__R')  # <R>
    _wrapWithContinuationImpl_1__T = typing.TypeVar('_wrapWithContinuationImpl_1__T')  # <T>
    _wrapWithContinuationImpl_2__R = typing.TypeVar('_wrapWithContinuationImpl_2__R')  # <R>
    _wrapWithContinuationImpl_2__P = typing.TypeVar('_wrapWithContinuationImpl_2__P')  # <P>
    _wrapWithContinuationImpl_2__T = typing.TypeVar('_wrapWithContinuationImpl_2__T')  # <T>
    @typing.overload
    @staticmethod
    def wrapWithContinuationImpl(this_wrapWithContinuationImpl: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_wrapWithContinuationImpl_0__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_wrapWithContinuationImpl_0__T], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def wrapWithContinuationImpl(this_wrapWithContinuationImpl: kotlin.jvm.functions.Function2[_wrapWithContinuationImpl_1__R, kotlin.coroutines.Continuation[_wrapWithContinuationImpl_1__T], java.lang.Object], receiver: _wrapWithContinuationImpl_1__R, completion: kotlin.coroutines.Continuation[_wrapWithContinuationImpl_1__T], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def wrapWithContinuationImpl(this_wrapWithContinuationImpl: kotlin.jvm.functions.Function3[_wrapWithContinuationImpl_2__R, _wrapWithContinuationImpl_2__P, kotlin.coroutines.Continuation[_wrapWithContinuationImpl_2__T], java.lang.Object], receiver: _wrapWithContinuationImpl_2__R, param: _wrapWithContinuationImpl_2__P, completion: kotlin.coroutines.Continuation[_wrapWithContinuationImpl_2__T], /) -> java.lang.Object: ...

class IntrinsicsKt__IntrinsicsKt(IntrinsicsKt__IntrinsicsJvmKt):
    def __init__(self) -> None: ...
    @staticmethod
    def getCOROUTINE_SUSPENDED() -> java.lang.Object: ...
