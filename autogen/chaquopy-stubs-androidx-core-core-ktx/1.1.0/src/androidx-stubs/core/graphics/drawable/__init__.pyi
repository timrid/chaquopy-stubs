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
    def toDrawable(this_toDrawable: android.graphics.Bitmap, resources: android.content.res.Resources, /) -> android.graphics.drawable.BitmapDrawable: ...

class ColorDrawableKt(java.lang.Object):
    @typing.overload
    @staticmethod
    def toDrawable(this_toDrawable: int | java.jint | java.lang.Integer, /) -> android.graphics.drawable.ColorDrawable: ...
    @typing.overload
    @staticmethod
    def toDrawable(this_toDrawable: android.graphics.Color, /) -> android.graphics.drawable.ColorDrawable: ...

class DrawableKt(java.lang.Object):
    @staticmethod
    def toBitmap(this_toBitmap: android.graphics.drawable.Drawable, width: int | java.jint | java.lang.Integer, height: int | java.jint | java.lang.Integer, config: android.graphics.Bitmap.Config, /) -> android.graphics.Bitmap: ...
    @staticmethod
    def updateBounds(this_updateBounds: android.graphics.drawable.Drawable, left: int | java.jint | java.lang.Integer, top: int | java.jint | java.lang.Integer, right: int | java.jint | java.lang.Integer, bottom: int | java.jint | java.lang.Integer, /) -> None: ...

class IconKt(java.lang.Object):
    @staticmethod
    def toAdaptiveIcon(this_toAdaptiveIcon: android.graphics.Bitmap, /) -> android.graphics.drawable.Icon: ...
    @typing.overload
    @staticmethod
    def toIcon(this_toIcon: android.graphics.Bitmap, /) -> android.graphics.drawable.Icon: ...
    @typing.overload
    @staticmethod
    def toIcon(this_toIcon: android.net.Uri, /) -> android.graphics.drawable.Icon: ...
    @typing.overload
    @staticmethod
    def toIcon(this_toIcon: java.chaquopy.JavaArrayJByte, /) -> android.graphics.drawable.Icon: ...
