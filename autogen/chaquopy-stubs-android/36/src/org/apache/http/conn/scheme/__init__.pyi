import java
import java.lang
import java.net
import org.apache.http.params



class HostNameResolver(java.lang.Object):
    def resolve(self, arg1: str | java.lang.String, /) -> java.net.InetAddress: ...

class LayeredSocketFactory(SocketFactory):
    def createSocket(self, arg1: java.net.Socket, arg2: str | java.lang.String, arg3: int | java.jint | java.lang.Integer, arg4: bool | java.jboolean | java.lang.Boolean, /) -> java.net.Socket: ...

class SocketFactory(java.lang.Object):
    def connectSocket(self, arg1: java.net.Socket, arg2: str | java.lang.String, arg3: int | java.jint | java.lang.Integer, arg4: java.net.InetAddress, arg5: int | java.jint | java.lang.Integer, arg6: org.apache.http.params.HttpParams, /) -> java.net.Socket: ...
    def createSocket(self) -> java.net.Socket: ...
    def isSecure(self, arg1: java.net.Socket, /) -> bool: ...
