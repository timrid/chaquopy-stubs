import typing

import java.lang
import java.time
import kotlin
import kotlin.coroutines
import kotlin.jvm.functions
import kotlinx.coroutines
import kotlinx.coroutines.flow
import kotlinx.coroutines.selects

class TimeKt(java.lang.Object):
    _debounce__T = typing.TypeVar('_debounce__T')  # <T>
    @staticmethod
    def debounce(this_debounce: kotlinx.coroutines.flow.Flow[_debounce__T], timeout: java.time.Duration, /) -> kotlinx.coroutines.flow.Flow[_debounce__T]: ...
    @staticmethod
    def delay(duration: java.time.Duration, completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    _onTimeout__R = typing.TypeVar('_onTimeout__R')  # <R>
    @staticmethod
    def onTimeout(this_onTimeout: kotlinx.coroutines.selects.SelectBuilder[_onTimeout__R], duration: java.time.Duration, block: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_onTimeout__R], java.lang.Object], /) -> None: ...
    _sample__T = typing.TypeVar('_sample__T')  # <T>
    @staticmethod
    def sample(this_sample: kotlinx.coroutines.flow.Flow[_sample__T], period: java.time.Duration, /) -> kotlinx.coroutines.flow.Flow[_sample__T]: ...
    _withTimeout__T = typing.TypeVar('_withTimeout__T')  # <T>
    @staticmethod
    def withTimeout(duration: java.time.Duration, block: kotlin.jvm.functions.Function2[kotlinx.coroutines.CoroutineScope, kotlin.coroutines.Continuation[_withTimeout__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_withTimeout__T], /) -> java.lang.Object: ...
    _withTimeoutOrNull__T = typing.TypeVar('_withTimeoutOrNull__T')  # <T>
    @staticmethod
    def withTimeoutOrNull(duration: java.time.Duration, block: kotlin.jvm.functions.Function2[kotlinx.coroutines.CoroutineScope, kotlin.coroutines.Continuation[_withTimeoutOrNull__T], java.lang.Object], completion: kotlin.coroutines.Continuation[_withTimeoutOrNull__T], /) -> java.lang.Object: ...
