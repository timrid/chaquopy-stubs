import android.graphics
import java
import java.lang
import java.util
import org.osmdroid.util
import org.osmdroid.views
import typing



class MyMath(java.lang.Object):
    @staticmethod
    def getNextSquareNumberAbove(factor: float | java.jfloat | java.lang.Float, /) -> int: ...

class PathProjection(java.lang.Object):
    def __init__(self) -> None: ...
    @typing.overload
    @staticmethod
    def toPixels(projection: org.osmdroid.views.Projection, in_: java.util.List[org.osmdroid.util.GeoPoint], reuse: android.graphics.Path, /) -> android.graphics.Path: ...
    @typing.overload
    @staticmethod
    def toPixels(projection: org.osmdroid.views.Projection, in_: java.util.List[org.osmdroid.util.GeoPoint], reuse: android.graphics.Path, doGudermann: bool | java.jboolean | java.lang.Boolean, /) -> android.graphics.Path: ...
