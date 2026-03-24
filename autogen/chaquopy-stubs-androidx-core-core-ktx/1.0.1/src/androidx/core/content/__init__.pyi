import typing

import android.content
import android.content.res
import android.util
import java
import java.chaquopy
import java.lang
import kotlin
import kotlin.jvm.functions

class ContentValuesKt(java.lang.Object):
    @staticmethod
    def contentValuesOf(*pairs: kotlin.Pair[java.lang.String, java.lang.Object]) -> android.content.ContentValues: ...

class ContextKt(java.lang.Object):
    @typing.overload
    @staticmethod
    def withStyledAttributes(receiver: android.content.Context, resourceId: int | java.jint | java.lang.Integer, attrs: java.chaquopy.JavaArrayJInt, block: kotlin.jvm.functions.Function1[android.content.res.TypedArray, kotlin.Unit], /) -> None: ...
    @typing.overload
    @staticmethod
    def withStyledAttributes(receiver: android.content.Context, set: android.util.AttributeSet, attrs: java.chaquopy.JavaArrayJInt, defStyleAttr: int | java.jint | java.lang.Integer, defStyleRes: int | java.jint | java.lang.Integer, block: kotlin.jvm.functions.Function1[android.content.res.TypedArray, kotlin.Unit], /) -> None: ...

class SharedPreferencesKt(java.lang.Object):
    @staticmethod
    def edit(receiver: android.content.SharedPreferences, commit: bool | java.jboolean | java.lang.Boolean, action: kotlin.jvm.functions.Function1[android.content.SharedPreferences.Editor, kotlin.Unit], /) -> None: ...
