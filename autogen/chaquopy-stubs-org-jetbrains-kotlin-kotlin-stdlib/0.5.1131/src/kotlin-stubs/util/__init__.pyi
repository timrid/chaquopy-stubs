import java.lang
import jet

class UtilPackage(java.lang.Object):
    @staticmethod
    def measureTimeMillis(block: jet.Function0[jet.Unit], /) -> int: ...
    @staticmethod
    def measureTimeNano(block: jet.Function0[jet.Unit], /) -> int: ...
