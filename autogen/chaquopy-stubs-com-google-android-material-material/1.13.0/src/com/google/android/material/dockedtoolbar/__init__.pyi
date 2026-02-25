import android.content
import android.util
import android.widget
import java
import java.lang
import typing



class DockedToolbarLayout(android.widget.FrameLayout):
    @typing.overload
    def __init__(self, context: android.content.Context, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, defStyleAttr: int | java.jint | java.lang.Integer, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, defStyleAttr: int | java.jint | java.lang.Integer, defStyleRes: int | java.jint | java.lang.Integer, /) -> None: ...
    def onMeasure(self, widthMeasureSpec: int | java.jint | java.lang.Integer, heightMeasureSpec: int | java.jint | java.lang.Integer, /) -> None: ...
