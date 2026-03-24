import java.lang.annotation
import kotlin

class Intrinsic(kotlin.jvm.internal.KObject, java.lang.annotation.Annotation):
    def value(self) -> str: ...
