import java
import java.lang
import java.util.concurrent



class SatelliteManager(java.lang.Object):
    def registerStateChangeListener(self, executor: java.util.concurrent.Executor, listener: SatelliteStateChangeListener, /) -> None: ...
    def unregisterStateChangeListener(self, listener: SatelliteStateChangeListener, /) -> None: ...

class SatelliteStateChangeListener(java.lang.Object):
    def onEnabledStateChanged(self, arg1: bool | java.jboolean | java.lang.Boolean, /) -> None: ...
