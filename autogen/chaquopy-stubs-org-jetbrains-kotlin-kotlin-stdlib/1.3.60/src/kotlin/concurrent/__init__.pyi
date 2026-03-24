import java
import java.lang
import java.util
import kotlin
import kotlin.jvm.functions

class LocksKt(java.lang.Object): ...

class ThreadsKt(java.lang.Object):
    @staticmethod
    def thread(start: bool | java.jboolean | java.lang.Boolean, isDaemon: bool | java.jboolean | java.lang.Boolean, contextClassLoader: java.lang.ClassLoader, name: str | java.lang.String, priority: int | java.jint | java.lang.Integer, block: kotlin.jvm.functions.Function0[kotlin.Unit], /) -> java.lang.Thread: ...

class TimersKt(java.lang.Object):
    @staticmethod
    def timer(name: str | java.lang.String, daemon: bool | java.jboolean | java.lang.Boolean, /) -> java.util.Timer: ...
