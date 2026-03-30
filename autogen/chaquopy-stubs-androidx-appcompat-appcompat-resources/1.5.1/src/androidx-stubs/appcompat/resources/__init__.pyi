import android.animation
import android.content.res
import android.graphics.drawable
import android.util
import java
import java.lang
import org.xmlpull.v1

class Compatibility(java.lang.Object):

    class Api15Impl(java.lang.Object):
        @staticmethod
        def getValueForDensity(resources: android.content.res.Resources, id: int | java.jint | java.lang.Integer, density: int | java.jint | java.lang.Integer, outValue: android.util.TypedValue, resolveRefs: bool | java.jboolean | java.lang.Boolean, /) -> None: ...

    class Api18Impl(java.lang.Object):
        @staticmethod
        def setAutoCancel(objectAnimator: android.animation.ObjectAnimator, cancel: bool | java.jboolean | java.lang.Boolean, /) -> None: ...

    class Api21Impl(java.lang.Object):
        @staticmethod
        def createFromXmlInner(r: android.content.res.Resources, parser: org.xmlpull.v1.XmlPullParser, attrs: android.util.AttributeSet, theme: android.content.res.Resources.Theme, /) -> android.graphics.drawable.Drawable: ...
        @staticmethod
        def getChangingConfigurations(typedArray: android.content.res.TypedArray, /) -> int: ...
        @staticmethod
        def inflate(drawable: android.graphics.drawable.Drawable, r: android.content.res.Resources, parser: org.xmlpull.v1.XmlPullParser, attrs: android.util.AttributeSet, theme: android.content.res.Resources.Theme, /) -> None: ...
