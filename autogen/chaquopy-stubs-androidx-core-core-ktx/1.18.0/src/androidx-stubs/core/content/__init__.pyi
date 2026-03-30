import typing

import android.content
import android.content.res
import android.os
import android.util
import java
import java.chaquopy
import java.lang
import kotlin
import kotlin.coroutines
import kotlin.jvm.functions

class ContentValuesKt(java.lang.Object):
    @staticmethod
    def contentValuesOf(*pairs: kotlin.Pair[java.lang.String, java.lang.Object]) -> android.content.ContentValues: ...

class ContextKt(java.lang.Object):
    @staticmethod
    def receiveBroadcasts(this_receiveBroadcasts: android.content.Context, filter: android.content.IntentFilter, flags: int | java.jint | java.lang.Integer, broadcastPermission: str | java.lang.String, scheduler: android.os.Handler, onReceive: kotlin.jvm.functions.Function2[android.content.BroadcastReceiver, android.content.Intent, kotlin.Unit], completion: kotlin.coroutines.Continuation[java.lang.Object], /) -> java.lang.Object: ...
    @staticmethod
    def receiveBroadcastsAsync(this_receiveBroadcastsAsync: android.content.Context, filter: android.content.IntentFilter, flags: int | java.jint | java.lang.Integer, broadcastPermission: str | java.lang.String, scheduler: android.os.Handler, onReceive: kotlin.jvm.functions.Function3[android.content.BroadcastReceiver.PendingResult, android.content.Intent, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], completion: kotlin.coroutines.Continuation[java.lang.Object], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def withStyledAttributes(this_withStyledAttributes: android.content.Context, resourceId: int | java.jint | java.lang.Integer, attrs: java.chaquopy.JavaArrayJInt, block: kotlin.jvm.functions.Function1[android.content.res.TypedArray, kotlin.Unit], /) -> None: ...
    @typing.overload
    @staticmethod
    def withStyledAttributes(this_withStyledAttributes: android.content.Context, set: android.util.AttributeSet, attrs: java.chaquopy.JavaArrayJInt, defStyleAttr: int | java.jint | java.lang.Integer, defStyleRes: int | java.jint | java.lang.Integer, block: kotlin.jvm.functions.Function1[android.content.res.TypedArray, kotlin.Unit], /) -> None: ...

class ContinuationBroadcastReceiver(android.content.BroadcastReceiver):
    def __init__(self, continuation: kotlin.coroutines.Continuation[java.lang.Object], onReceiveChecked: kotlin.jvm.functions.Function2[android.content.BroadcastReceiver, android.content.Intent, kotlin.Unit], /) -> None: ...
    def onReceive(self, context: android.content.Context, intent: android.content.Intent, /) -> None: ...

class SharedPreferencesKt(java.lang.Object):
    @staticmethod
    def edit(this_edit: android.content.SharedPreferences, commit: bool | java.jboolean | java.lang.Boolean, action: kotlin.jvm.functions.Function1[android.content.SharedPreferences.Editor, kotlin.Unit], /) -> None: ...
