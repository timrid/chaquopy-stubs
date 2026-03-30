import typing

import java
import java.lang

class MathUtils(java.lang.Object):
    @typing.overload
    @staticmethod
    def clamp(value: float | java.jdouble | java.lang.Double, min: float | java.jdouble | java.lang.Double, max: float | java.jdouble | java.lang.Double, /) -> float: ...
    @typing.overload
    @staticmethod
    def clamp(value: float | java.jfloat | java.lang.Float, min: float | java.jfloat | java.lang.Float, max: float | java.jfloat | java.lang.Float, /) -> float: ...
    @typing.overload
    @staticmethod
    def clamp(value: int | java.jint | java.lang.Integer, min: int | java.jint | java.lang.Integer, max: int | java.jint | java.lang.Integer, /) -> int: ...
    @typing.overload
    @staticmethod
    def clamp(value: int | java.jlong | java.lang.Long, min: int | java.jlong | java.lang.Long, max: int | java.jlong | java.lang.Long, /) -> int: ...
