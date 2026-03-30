import android.animation
import android.content
import java
import java.lang

class MotionUtils(java.lang.Object):
    @staticmethod
    def resolveThemeDuration(context: android.content.Context, attrResId: int | java.jint | java.lang.Integer, defaultDuration: int | java.jint | java.lang.Integer, /) -> int: ...
    @staticmethod
    def resolveThemeInterpolator(context: android.content.Context, attrResId: int | java.jint | java.lang.Integer, defaultInterpolator: android.animation.TimeInterpolator, /) -> android.animation.TimeInterpolator: ...
