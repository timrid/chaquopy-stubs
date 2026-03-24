import android.content
import android.graphics
import android.text.method
import android.view
import java
import java.lang

class AllCapsTransformationMethod(android.text.method.TransformationMethod):
    def __init__(self, context: android.content.Context, /) -> None: ...
    def getTransformation(self, source: java.lang.CharSequence, view: android.view.View, /) -> java.lang.CharSequence: ...
    def onFocusChanged(self, view: android.view.View, sourceText: java.lang.CharSequence, focused: bool | java.jboolean | java.lang.Boolean, direction: int | java.jint | java.lang.Integer, previouslyFocusedRect: android.graphics.Rect, /) -> None: ...
