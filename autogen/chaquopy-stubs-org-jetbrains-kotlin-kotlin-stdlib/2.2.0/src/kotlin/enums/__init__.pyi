import typing

import java
import java.chaquopy
import java.io
import java.lang
import java.util
import kotlin.collections
import kotlin.jvm.functions
import kotlin.jvm.internal.markers

_EnumEntries__E = typing.TypeVar('_EnumEntries__E', bound=java.lang.Enum[E])  # <E>
class EnumEntries(java.util.List[_EnumEntries__E], kotlin.jvm.internal.markers.KMappedMarker, typing.Generic[_EnumEntries__E]): ...

class EnumEntriesJVMKt(java.lang.Object): ...

class EnumEntriesKt(java.lang.Object):
    _enumEntries_0__E = typing.TypeVar('_enumEntries_0__E', bound=java.lang.Enum[E])  # <E>
    _enumEntries_1__E = typing.TypeVar('_enumEntries_1__E', bound=java.lang.Enum[E])  # <E>
    @typing.overload
    @staticmethod
    def enumEntries(entriesProvider: kotlin.jvm.functions.Function0[java.chaquopy.JavaArray[_enumEntries_0__E]], /) -> EnumEntries[_enumEntries_0__E]: ...
    @typing.overload
    @staticmethod
    def enumEntries(entries: java.chaquopy.JavaArray[_enumEntries_1__E], /) -> EnumEntries[_enumEntries_1__E]: ...

_EnumEntriesList__T = typing.TypeVar('_EnumEntriesList__T', bound=java.lang.Enum[T])  # <T>
class EnumEntriesList(kotlin.collections.AbstractList[_EnumEntriesList__T], EnumEntries[_EnumEntriesList__T], java.io.Serializable, typing.Generic[_EnumEntriesList__T]):
    def __init__(self, entries: java.chaquopy.JavaArray[_EnumEntriesList__T], /) -> None: ...
    def contains(self, element: _EnumEntriesList__T, /) -> bool: ...
    def get(self, index: int | java.jint | java.lang.Integer, /) -> _EnumEntriesList__T: ...
    def getSize(self) -> int: ...
    def indexOf(self, element: _EnumEntriesList__T, /) -> int: ...
    def lastIndexOf(self, element: _EnumEntriesList__T, /) -> int: ...

_EnumEntriesSerializationProxy__E = typing.TypeVar('_EnumEntriesSerializationProxy__E', bound=java.lang.Enum[E])  # <E>
class EnumEntriesSerializationProxy(java.io.Serializable, typing.Generic[_EnumEntriesSerializationProxy__E]):
    def __init__(self, entries: java.chaquopy.JavaArray[_EnumEntriesSerializationProxy__E], /) -> None: ...
