import typing

import android.content
import android.widget
import java
import java.lang

class ToastKt(java.lang.Object):
    @typing.overload
    @staticmethod
    def toast(receiver: android.content.Context, resId: int | java.jint | java.lang.Integer, duration: int | java.jint | java.lang.Integer, /) -> android.widget.Toast: ...
    @typing.overload
    @staticmethod
    def toast(receiver: android.content.Context, text: java.lang.CharSequence, duration: int | java.jint | java.lang.Integer, /) -> android.widget.Toast: ...
