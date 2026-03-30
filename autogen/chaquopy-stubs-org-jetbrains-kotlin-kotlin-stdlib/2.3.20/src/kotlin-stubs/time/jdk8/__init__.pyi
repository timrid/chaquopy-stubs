import java.lang
import java.time
import kotlin.time

class DurationConversionsJDK8Kt(java.lang.Object): ...

class InstantConversionsJDK8Kt(java.lang.Object):
    @staticmethod
    def toJavaInstant(this_toJavaInstant: kotlin.time.Instant, /) -> java.time.Instant: ...
    @staticmethod
    def toKotlinInstant(this_toKotlinInstant: java.time.Instant, /) -> kotlin.time.Instant: ...
