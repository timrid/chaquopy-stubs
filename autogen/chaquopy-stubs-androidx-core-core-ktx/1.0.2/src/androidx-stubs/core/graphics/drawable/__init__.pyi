import typing

import android.content.res
import android.graphics
import android.graphics.drawable
import android.net
import java
import java.chaquopy
import java.lang

class BitmapDrawableKt(java.lang.Object):
    @staticmethod
    def toDrawable(receiver: android.graphics.Bitmap, resources: android.content.res.Resources, /) -> android.graphics.drawable.BitmapDrawable: ...

class ColorDrawableKt(java.lang.Object):
    @typing.overload
    @staticmethod
    def toDrawable(receiver: int | java.jint | java.lang.Integer, /) -> android.graphics.drawable.ColorDrawable: ...
    @typing.overload
    @staticmethod
    def toDrawable(receiver: android.graphics.Color, /) -> android.graphics.drawable.ColorDrawable: ...

class DrawableKt(java.lang.Object):
    @staticmethod
    def toBitmap(receiver: android.graphics.drawable.Drawable, width: int | java.jint | java.lang.Integer, height: int | java.jint | java.lang.Integer, config: android.graphics.Bitmap.Config, /) -> android.graphics.Bitmap: ...
    @staticmethod
    def updateBounds(receiver: android.graphics.drawable.Drawable, left: int | java.jint | java.lang.Integer, top: int | java.jint | java.lang.Integer, right: int | java.jint | java.lang.Integer, bottom: int | java.jint | java.lang.Integer, /) -> None: ...

class IconKt(java.lang.Object):
    @staticmethod
    def toAdaptiveIcon(receiver: android.graphics.Bitmap, /) -> android.graphics.drawable.Icon: ...
    @typing.overload
    @staticmethod
    def toIcon(receiver: android.graphics.Bitmap, /) -> android.graphics.drawable.Icon: ...
    @typing.overload
    @staticmethod
    def toIcon(receiver: android.net.Uri, /) -> android.graphics.drawable.Icon: ...
    @typing.overload
    @staticmethod
    def toIcon(receiver: java.chaquopy.JavaArrayJByte, /) -> android.graphics.drawable.Icon: ...
