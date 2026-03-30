import android.content
import android.util
import androidx.appcompat.app
import androidx.appcompat.widget

class MaterialComponentsViewInflater(androidx.appcompat.app.AppCompatViewInflater):
    def __init__(self) -> None: ...
    def createButton(self, context: android.content.Context, attrs: android.util.AttributeSet, /) -> androidx.appcompat.widget.AppCompatButton: ...
