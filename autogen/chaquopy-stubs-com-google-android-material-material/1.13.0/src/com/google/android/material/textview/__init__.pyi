import android.content
import android.util
import androidx.appcompat.widget
import java
import java.lang
import typing



class MaterialTextView(androidx.appcompat.widget.AppCompatTextView):
    @typing.overload
    def __init__(self, context: android.content.Context, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, defStyleAttr: int | java.jint | java.lang.Integer, /) -> None: ...
    @typing.overload
    def __init__(self, context: android.content.Context, attrs: android.util.AttributeSet, defStyleAttr: int | java.jint | java.lang.Integer, defStyleRes: int | java.jint | java.lang.Integer, /) -> None: ...
    def setTextAppearance(self, context: android.content.Context, resId: int | java.jint | java.lang.Integer, /) -> None: ...
