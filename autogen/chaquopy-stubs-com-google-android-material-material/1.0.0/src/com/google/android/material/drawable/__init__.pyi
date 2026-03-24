import android.content.res
import android.graphics
import android.graphics.drawable
import java.lang

class DrawableUtils(java.lang.Object):
    @staticmethod
    def updateTintFilter(drawable: android.graphics.drawable.Drawable, tint: android.content.res.ColorStateList, tintMode: android.graphics.PorterDuff.Mode, /) -> android.graphics.PorterDuffColorFilter: ...
