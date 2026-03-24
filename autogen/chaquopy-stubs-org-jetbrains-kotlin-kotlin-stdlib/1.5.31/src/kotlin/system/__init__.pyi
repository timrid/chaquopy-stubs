import java.lang
import kotlin
import kotlin.jvm.functions

class ProcessKt(java.lang.Object): ...

class TimingKt(java.lang.Object):
    @staticmethod
    def measureNanoTime(block: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> int: ...
    @staticmethod
    def measureTimeMillis(block: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> int: ...
