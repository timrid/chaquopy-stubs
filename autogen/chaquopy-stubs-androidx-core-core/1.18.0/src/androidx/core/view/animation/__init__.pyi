import typing

import android.graphics
import android.view.animation
import java
import java.lang

class PathInterpolatorCompat(java.lang.Object):
    @typing.overload
    @staticmethod
    def create(path: android.graphics.Path, /) -> android.view.animation.Interpolator: ...
    @typing.overload
    @staticmethod
    def create(controlX: float | java.jfloat | java.lang.Float, controlY: float | java.jfloat | java.lang.Float, /) -> android.view.animation.Interpolator: ...
    @typing.overload
    @staticmethod
    def create(controlX1: float | java.jfloat | java.lang.Float, controlY1: float | java.jfloat | java.lang.Float, controlX2: float | java.jfloat | java.lang.Float, controlY2: float | java.jfloat | java.lang.Float, /) -> android.view.animation.Interpolator: ...
