import android.text
import android.text.method
import android.view
import android.widget

class LinkMovementMethodCompat(android.text.method.LinkMovementMethod):
    @staticmethod
    def getInstance() -> LinkMovementMethodCompat: ...
    def onTouchEvent(self, widget: android.widget.TextView, buffer: android.text.Spannable, event: android.view.MotionEvent, /) -> bool: ...
