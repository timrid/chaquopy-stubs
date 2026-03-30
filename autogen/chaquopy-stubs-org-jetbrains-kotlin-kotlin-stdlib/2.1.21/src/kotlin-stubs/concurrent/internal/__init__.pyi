import typing

import java
import java.lang
import java.util.concurrent.atomic

class AtomicIntrinsicsKt(java.lang.Object):
    _compareAndExchange_3__T = typing.TypeVar('_compareAndExchange_3__T')  # <T>
    _compareAndExchange_6__T = typing.TypeVar('_compareAndExchange_6__T')  # <T>
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicBoolean, expected: bool | java.jboolean | java.lang.Boolean, newValue: bool | java.jboolean | java.lang.Boolean, /) -> bool: ...
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicInteger, expected: int | java.jint | java.lang.Integer, newValue: int | java.jint | java.lang.Integer, /) -> int: ...
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicLong, expected: int | java.jlong | java.lang.Long, newValue: int | java.jlong | java.lang.Long, /) -> int: ...
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicReference[_compareAndExchange_3__T], expected: _compareAndExchange_3__T, newValue: _compareAndExchange_3__T, /) -> _compareAndExchange_3__T: ...
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicIntegerArray, index: int | java.jint | java.lang.Integer, expected: int | java.jint | java.lang.Integer, newValue: int | java.jint | java.lang.Integer, /) -> int: ...
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicLongArray, index: int | java.jint | java.lang.Integer, expected: int | java.jlong | java.lang.Long, newValue: int | java.jlong | java.lang.Long, /) -> int: ...
    @typing.overload
    @staticmethod
    def compareAndExchange(this_compareAndExchange: java.util.concurrent.atomic.AtomicReferenceArray[_compareAndExchange_6__T], index: int | java.jint | java.lang.Integer, expected: _compareAndExchange_6__T, newValue: _compareAndExchange_6__T, /) -> _compareAndExchange_6__T: ...
