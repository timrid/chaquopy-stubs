import android.view.autofill
import java.lang

class AutofillIdCompat(java.lang.Object):
    def toAutofillId(self) -> android.view.autofill.AutofillId: ...
    @staticmethod
    def toAutofillIdCompat(autofillId: android.view.autofill.AutofillId, /) -> AutofillIdCompat: ...
