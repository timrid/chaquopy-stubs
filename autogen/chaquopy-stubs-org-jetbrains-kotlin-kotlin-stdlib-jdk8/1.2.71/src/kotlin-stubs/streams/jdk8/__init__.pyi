import typing

import java.lang
import java.util
import java.util.stream
import kotlin.sequences

class StreamsKt(java.lang.Object):
    _asSequence_3__T = typing.TypeVar('_asSequence_3__T')  # <T>
    @typing.overload
    @staticmethod
    def asSequence(receiver: java.util.stream.DoubleStream, /) -> kotlin.sequences.Sequence[java.lang.Double]: ...
    @typing.overload
    @staticmethod
    def asSequence(receiver: java.util.stream.IntStream, /) -> kotlin.sequences.Sequence[java.lang.Integer]: ...
    @typing.overload
    @staticmethod
    def asSequence(receiver: java.util.stream.LongStream, /) -> kotlin.sequences.Sequence[java.lang.Long]: ...
    @typing.overload
    @staticmethod
    def asSequence(receiver: java.util.stream.Stream[_asSequence_3__T], /) -> kotlin.sequences.Sequence[_asSequence_3__T]: ...
    _asStream__T = typing.TypeVar('_asStream__T')  # <T>
    @staticmethod
    def asStream(receiver: kotlin.sequences.Sequence[_asStream__T], /) -> java.util.stream.Stream[_asStream__T]: ...
    _toList_3__T = typing.TypeVar('_toList_3__T')  # <T>
    @typing.overload
    @staticmethod
    def toList(receiver: java.util.stream.DoubleStream, /) -> java.util.List[java.lang.Double]: ...
    @typing.overload
    @staticmethod
    def toList(receiver: java.util.stream.IntStream, /) -> java.util.List[java.lang.Integer]: ...
    @typing.overload
    @staticmethod
    def toList(receiver: java.util.stream.LongStream, /) -> java.util.List[java.lang.Long]: ...
    @typing.overload
    @staticmethod
    def toList(receiver: java.util.stream.Stream[_toList_3__T], /) -> java.util.List[_toList_3__T]: ...
