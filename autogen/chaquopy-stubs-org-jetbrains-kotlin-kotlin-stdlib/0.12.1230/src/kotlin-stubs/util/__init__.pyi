import java.lang
import kotlin
import kotlin.jvm.functions

class UtilPackage(java.lang.Object):
    @staticmethod
    def measureTimeMillis(block: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> int: ...
    @staticmethod
    def measureTimeNano(block: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> int: ...
