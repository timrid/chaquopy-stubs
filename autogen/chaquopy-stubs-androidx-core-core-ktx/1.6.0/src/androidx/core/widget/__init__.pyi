import android.text
import android.widget
import java.lang
import kotlin
import kotlin.jvm.functions

class TextViewKt(java.lang.Object):
    @staticmethod
    def addTextChangedListener(this_addTextChangedListener: android.widget.TextView, beforeTextChanged: kotlin.jvm.functions.Function4[java.lang.CharSequence, int, int, int, kotlin.Unit], onTextChanged: kotlin.jvm.functions.Function4[java.lang.CharSequence, int, int, int, kotlin.Unit], afterTextChanged: kotlin.jvm.functions.Function1[android.text.Editable, kotlin.Unit], /) -> android.text.TextWatcher: ...
    @staticmethod
    def doAfterTextChanged(this_doAfterTextChanged: android.widget.TextView, action: kotlin.jvm.functions.Function1[android.text.Editable, kotlin.Unit], /) -> android.text.TextWatcher: ...
    @staticmethod
    def doBeforeTextChanged(this_doBeforeTextChanged: android.widget.TextView, action: kotlin.jvm.functions.Function4[java.lang.CharSequence, int, int, int, kotlin.Unit], /) -> android.text.TextWatcher: ...
    @staticmethod
    def doOnTextChanged(this_doOnTextChanged: android.widget.TextView, action: kotlin.jvm.functions.Function4[java.lang.CharSequence, int, int, int, kotlin.Unit], /) -> android.text.TextWatcher: ...
