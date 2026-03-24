import java.lang
import kotlin

class UtilPackage(java.lang.Object):
    @staticmethod
    def measureTimeMillis(block: kotlin.Function0[kotlin.Unit], /) -> int: ...
    @staticmethod
    def measureTimeNano(block: kotlin.Function0[kotlin.Unit], /) -> int: ...
