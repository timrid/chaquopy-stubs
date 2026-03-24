import java.chaquopy
import java.lang
import java.lang.annotation

class GuardedBy(java.lang.annotation.Annotation):
    def value(self) -> str: ...

class LazyInit(java.lang.annotation.Annotation): ...

class LockMethod(java.lang.annotation.Annotation):
    def value(self) -> java.chaquopy.JavaArray[java.lang.String]: ...

class UnlockMethod(java.lang.annotation.Annotation):
    def value(self) -> java.chaquopy.JavaArray[java.lang.String]: ...
