import android.content
import android.util
import android.view
import android.widget
import java
import java.lang
import typing



class FloatingToolbarLayout(android.widget.FrameLayout):
    @typing.overload
    def __init__(self, context: android.content.Context, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, defStyleAttr: int | java.jint | java.lang.Integer, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, defStyleAttr: int | java.jint | java.lang.Integer, defStyleRes: int | java.jint | java.lang.Integer, /) -> None: ...
    def setLayoutParams(self, params: android.view.ViewGroup.LayoutParams, /) -> None: ...
