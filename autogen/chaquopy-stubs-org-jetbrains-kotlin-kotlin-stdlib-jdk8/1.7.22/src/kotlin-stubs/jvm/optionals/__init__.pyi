import typing

import java.lang
import java.util
import kotlin.jvm.functions
import kotlin.sequences

class OptionalsKt(java.lang.Object):
    _asSequence__T = typing.TypeVar('_asSequence__T')  # <T>
    @staticmethod
    def asSequence(this_asSequence: java.util.Optional[_asSequence__T], /) -> kotlin.sequences.Sequence[_asSequence__T]: ...
    _getOrDefault__R = typing.TypeVar('_getOrDefault__R')  # <R>
    @staticmethod
    def getOrDefault(this_getOrDefault: java.util.Optional[java.lang.Object], defaultValue: _getOrDefault__R, /) -> _getOrDefault__R: ...
    _getOrElse__R = typing.TypeVar('_getOrElse__R')  # <R>
    @staticmethod
    def getOrElse(this_getOrElse: java.util.Optional[java.lang.Object], defaultValue: kotlin.jvm.functions.Function0[_getOrElse__R], /) -> _getOrElse__R: ...
    _getOrNull__T = typing.TypeVar('_getOrNull__T')  # <T>
    @staticmethod
    def getOrNull(this_getOrNull: java.util.Optional[_getOrNull__T], /) -> _getOrNull__T: ...
    _toCollection__C = typing.TypeVar('_toCollection__C')  # <C>
    @staticmethod
    def toCollection(this_toCollection: java.util.Optional[java.lang.Object], destination: _toCollection__C, /) -> _toCollection__C: ...
    _toList__T = typing.TypeVar('_toList__T')  # <T>
    @staticmethod
    def toList(this_toList: java.util.Optional[_toList__T], /) -> java.util.List[_toList__T]: ...
    _toSet__T = typing.TypeVar('_toSet__T')  # <T>
    @staticmethod
    def toSet(this_toSet: java.util.Optional[_toSet__T], /) -> java.util.Set[_toSet__T]: ...
