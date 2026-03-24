import typing

import android.os
import java
import java.lang
import kotlin
import kotlin.jvm.functions

class BundleKt(java.lang.Object):
    @staticmethod
    def bundleOf(*pairs: kotlin.Pair[java.lang.String, java.lang.Object]) -> android.os.Bundle: ...

class HandlerKt(java.lang.Object):
    @staticmethod
    def postAtTime(receiver: android.os.Handler, uptimeMillis: int | java.jlong | java.lang.Long, token: java.lang.Object | int | bool | float | str, action: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> java.lang.Runnable: ...
    @staticmethod
    def postDelayed(receiver: android.os.Handler, delayInMillis: int | java.jlong | java.lang.Long, token: java.lang.Object | int | bool | float | str, action: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> java.lang.Runnable: ...
    @staticmethod
    def postDelayedWithToken(receiver: android.os.Handler, runnable: java.lang.Runnable, token: java.lang.Object | int | bool | float | str, delayInMillis: int | java.jlong | java.lang.Long, /) -> None: ...

class PersistableBundleKt(java.lang.Object):
    @staticmethod
    def persistableBundleOf(*pairs: kotlin.Pair[java.lang.String, java.lang.Object]) -> android.os.PersistableBundle: ...

class TraceKt(java.lang.Object):
    _trace__T = typing.TypeVar('_trace__T')  # <T>
    @staticmethod
    def trace(sectionName: str | java.lang.String, block: kotlin.jvm.functions.Function0[_trace__T], /) -> _trace__T: ...
