import typing

import java.lang
import java.util.stream
import kotlin
import kotlin.coroutines
import kotlinx.coroutines.flow

_StreamFlow__T = typing.TypeVar('_StreamFlow__T')  # <T>
class StreamFlow(kotlinx.coroutines.flow.Flow[_StreamFlow__T], typing.Generic[_StreamFlow__T]):
    def __init__(self, stream: java.util.stream.Stream[_StreamFlow__T], /) -> None: ...
    def collect(self, collector: kotlinx.coroutines.flow.FlowCollector[_StreamFlow__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...

class StreamKt(java.lang.Object):
    _consumeAsFlow__T = typing.TypeVar('_consumeAsFlow__T')  # <T>
    @staticmethod
    def consumeAsFlow(this_consumeAsFlow: java.util.stream.Stream[_consumeAsFlow__T], /) -> kotlinx.coroutines.flow.Flow[_consumeAsFlow__T]: ...
