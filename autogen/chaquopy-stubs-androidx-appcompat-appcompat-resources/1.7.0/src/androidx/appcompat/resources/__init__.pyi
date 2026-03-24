import android.content.res
import android.graphics.drawable
import android.util
import java.lang
import org.xmlpull.v1

class Compatibility(java.lang.Object):

    class Api21Impl(java.lang.Object):
        @staticmethod
        def createFromXmlInner(r: android.content.res.Resources, parser: org.xmlpull.v1.XmlPullParser, attrs: android.util.AttributeSet, theme: android.content.res.Resources.Theme, /) -> android.graphics.drawable.Drawable: ...
        @staticmethod
        def getChangingConfigurations(typedArray: android.content.res.TypedArray, /) -> int: ...
        @staticmethod
        def inflate(drawable: android.graphics.drawable.Drawable, r: android.content.res.Resources, parser: org.xmlpull.v1.XmlPullParser, attrs: android.util.AttributeSet, theme: android.content.res.Resources.Theme, /) -> None: ...
