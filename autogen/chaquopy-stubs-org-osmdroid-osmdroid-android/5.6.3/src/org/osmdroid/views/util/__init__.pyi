import typing

import android.graphics
import java
import java.lang
import java.util
import org.osmdroid.api
import org.osmdroid.util
import org.osmdroid.views
import org.osmdroid.views.util.constants

class Mercator(org.osmdroid.views.util.constants.MapViewConstants):
    @staticmethod
    def getBoundingBoxFromCoords(left: float | java.jdouble | java.lang.Double, top: float | java.jdouble | java.lang.Double, right: float | java.jdouble | java.lang.Double, bottom: float | java.jdouble | java.lang.Double, zoom: int | java.jint | java.lang.Integer, /) -> org.osmdroid.util.BoundingBox: ...
    @staticmethod
    def getBoundingBoxFromPointInMapTile(aMapTile: android.graphics.Point, aZoom: int | java.jint | java.lang.Integer, /) -> org.osmdroid.util.BoundingBox: ...
    @typing.overload
    @staticmethod
    def projectGeoPoint(aGeoPoint: org.osmdroid.api.IGeoPoint, aZoom: int | java.jint | java.lang.Integer, aReuse: android.graphics.Point, /) -> android.graphics.Point: ...
    @typing.overload
    @staticmethod
    def projectGeoPoint(aLat: float | java.jdouble | java.lang.Double, aLon: float | java.jdouble | java.lang.Double, aZoom: int | java.jint | java.lang.Integer, aReuse: android.graphics.Point, /) -> android.graphics.Point: ...
    @staticmethod
    def projectPoint(x: int | java.jint | java.lang.Integer, y: int | java.jint | java.lang.Integer, aZoom: int | java.jint | java.lang.Integer, /) -> org.osmdroid.util.GeoPoint: ...
    @staticmethod
    def tile2lat(y: int | java.jint | java.lang.Integer, aZoom: int | java.jint | java.lang.Integer, /) -> float: ...
    @staticmethod
    def tile2lon(x: int | java.jint | java.lang.Integer, aZoom: int | java.jint | java.lang.Integer, /) -> float: ...

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
