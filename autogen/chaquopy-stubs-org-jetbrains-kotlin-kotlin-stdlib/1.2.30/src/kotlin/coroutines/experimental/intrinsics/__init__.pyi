import typing

import java.lang
import kotlin
import kotlin.coroutines.experimental
import kotlin.jvm.functions

class IntrinsicsJvmKt(java.lang.Object): ...

class IntrinsicsKt(java.lang.Object):
    _createCoroutineUnchecked_0__T = typing.TypeVar('_createCoroutineUnchecked_0__T')  # <T>
    _createCoroutineUnchecked_1__R = typing.TypeVar('_createCoroutineUnchecked_1__R')  # <R>
    _createCoroutineUnchecked_1__T = typing.TypeVar('_createCoroutineUnchecked_1__T')  # <T>
    @typing.overload
    @staticmethod
    def createCoroutineUnchecked(receiver: kotlin.jvm.functions.Function1[kotlin.coroutines.experimental.Continuation[_createCoroutineUnchecked_0__T], java.lang.Object], completion: kotlin.coroutines.experimental.Continuation[_createCoroutineUnchecked_0__T], /) -> kotlin.coroutines.experimental.Continuation[kotlin.Unit]: ...
    @typing.overload
    @staticmethod
    def createCoroutineUnchecked(receiver: kotlin.jvm.functions.Function2[_createCoroutineUnchecked_1__R, kotlin.coroutines.experimental.Continuation[_createCoroutineUnchecked_1__T], java.lang.Object], receiver: _createCoroutineUnchecked_1__R, completion: kotlin.coroutines.experimental.Continuation[_createCoroutineUnchecked_1__T], /) -> kotlin.coroutines.experimental.Continuation[kotlin.Unit]: ...
    @staticmethod
    def getCOROUTINE_SUSPENDED() -> java.lang.Object: ...
    @staticmethod
    def getCoroutineContext() -> kotlin.coroutines.experimental.CoroutineContext: ...
