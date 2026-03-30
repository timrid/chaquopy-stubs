import typing

import android.os
import android.util
import java
import java.chaquopy
import java.lang
import java.util
import java.util.concurrent.atomic
import kotlin
import kotlin.coroutines
import kotlin.jvm.functions

class BundleApi21ImplKt(java.lang.Object):
    INSTANCE: typing.ClassVar[BundleApi21ImplKt] = ...
    @staticmethod
    def putSize(bundle: android.os.Bundle, key: str | java.lang.String, value: android.util.Size, /) -> None: ...
    @staticmethod
    def putSizeF(bundle: android.os.Bundle, key: str | java.lang.String, value: android.util.SizeF, /) -> None: ...

class BundleKt(java.lang.Object):
    @typing.overload
    @staticmethod
    def bundleOf() -> android.os.Bundle: ...
    @typing.overload
    @staticmethod
    def bundleOf(*pairs: kotlin.Pair[java.lang.String, java.lang.Object]) -> android.os.Bundle: ...

_ContinuationOutcomeReceiver__R = typing.TypeVar('_ContinuationOutcomeReceiver__R')  # <R>
_ContinuationOutcomeReceiver__E = typing.TypeVar('_ContinuationOutcomeReceiver__E', bound=java.lang.Throwable)  # <E>
class ContinuationOutcomeReceiver(java.util.concurrent.atomic.AtomicBoolean, android.os.OutcomeReceiver[_ContinuationOutcomeReceiver__R, _ContinuationOutcomeReceiver__E], typing.Generic[_ContinuationOutcomeReceiver__R, _ContinuationOutcomeReceiver__E]):
    def __init__(self, continuation: kotlin.coroutines.Continuation[_ContinuationOutcomeReceiver__R], /) -> None: ...
    def onError(self, error: _ContinuationOutcomeReceiver__E, /) -> None: ...
    def onResult(self, result: _ContinuationOutcomeReceiver__R, /) -> None: ...
    def toString(self) -> str: ...

class HandlerKt(java.lang.Object):
    @staticmethod
    def postAtTime(this_postAtTime: android.os.Handler, uptimeMillis: int | java.jlong | java.lang.Long, token: java.lang.Object | int | bool | float | str, action: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> java.lang.Runnable: ...
    @staticmethod
    def postDelayed(this_postDelayed: android.os.Handler, delayInMillis: int | java.jlong | java.lang.Long, token: java.lang.Object | int | bool | float | str, action: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> java.lang.Runnable: ...

class OutcomeReceiverKt(java.lang.Object):
    _asOutcomeReceiver__R = typing.TypeVar('_asOutcomeReceiver__R')  # <R>
    @staticmethod
    def asOutcomeReceiver(this_asOutcomeReceiver: kotlin.coroutines.Continuation[_asOutcomeReceiver__R], /) -> android.os.OutcomeReceiver[_asOutcomeReceiver__R, java.lang.Throwable]: ...

class ParcelKt(java.lang.Object):
    _use__T = typing.TypeVar('_use__T')  # <T>
    @staticmethod
    def use(this_use: android.os.Parcel, block: kotlin.jvm.functions.Function1[android.os.Parcel, _use__T], /) -> _use__T: ...

class PersistableBundleApi21ImplKt(java.lang.Object):
    INSTANCE: typing.ClassVar[PersistableBundleApi21ImplKt] = ...
    @staticmethod
    def createPersistableBundle(capacity: int | java.jint | java.lang.Integer, /) -> android.os.PersistableBundle: ...
    @staticmethod
    def putValue(persistableBundle: android.os.PersistableBundle, key: str | java.lang.String, value: java.lang.Object | int | bool | float | str, /) -> None: ...

class PersistableBundleApi22ImplKt(java.lang.Object):
    INSTANCE: typing.ClassVar[PersistableBundleApi22ImplKt] = ...
    @staticmethod
    def putBoolean(persistableBundle: android.os.PersistableBundle, key: str | java.lang.String, value: bool | java.jboolean | java.lang.Boolean, /) -> None: ...
    @staticmethod
    def putBooleanArray(persistableBundle: android.os.PersistableBundle, key: str | java.lang.String, value: java.chaquopy.JavaArrayJBoolean, /) -> None: ...

class PersistableBundleKt(java.lang.Object):
    @typing.overload
    @staticmethod
    def persistableBundleOf() -> android.os.PersistableBundle: ...
    @typing.overload
    @staticmethod
    def persistableBundleOf(*pairs: kotlin.Pair[java.lang.String, java.lang.Object]) -> android.os.PersistableBundle: ...
    @staticmethod
    def toPersistableBundle(this_toPersistableBundle: java.util.Map[java.lang.String, java.lang.Object], /) -> android.os.PersistableBundle: ...

class TraceKt(java.lang.Object):
    _trace__T = typing.TypeVar('_trace__T')  # <T>
    @staticmethod
    def trace(sectionName: str | java.lang.String, block: kotlin.jvm.functions.Function0[_trace__T], /) -> _trace__T: ...
