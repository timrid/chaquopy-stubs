import typing

import android.graphics
import java
import java.lang

class CanvasCompat(java.lang.Object):
    @typing.overload
    @staticmethod
    def saveLayerAlpha(canvas: android.graphics.Canvas, bounds: android.graphics.RectF, alpha: int | java.jint | java.lang.Integer, /) -> int: ...
    @typing.overload
    @staticmethod
    def saveLayerAlpha(canvas: android.graphics.Canvas, left: float | java.jfloat | java.lang.Float, top: float | java.jfloat | java.lang.Float, right: float | java.jfloat | java.lang.Float, bottom: float | java.jfloat | java.lang.Float, alpha: int | java.jint | java.lang.Integer, /) -> int: ...
