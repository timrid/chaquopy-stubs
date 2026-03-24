import android.content
import android.content.res
import android.graphics
import android.graphics.drawable
import android.util
import java
import java.lang

class DrawableUtils(java.lang.Object):
    @staticmethod
    def parseDrawableXml(context: android.content.Context, id: int | java.jint | java.lang.Integer, startTag: java.lang.CharSequence, /) -> android.util.AttributeSet: ...
    @staticmethod
    def setRippleDrawableRadius(drawable: android.graphics.drawable.RippleDrawable, radius: int | java.jint | java.lang.Integer, /) -> None: ...
    @staticmethod
    def updateTintFilter(drawable: android.graphics.drawable.Drawable, tint: android.content.res.ColorStateList, tintMode: android.graphics.PorterDuff.Mode, /) -> android.graphics.PorterDuffColorFilter: ...
