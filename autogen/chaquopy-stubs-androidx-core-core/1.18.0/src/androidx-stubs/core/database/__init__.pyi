import android.database
import java
import java.chaquopy
import java.lang

class CursorWindowCompat(java.lang.Object):
    @staticmethod
    def create(name: str | java.lang.String, windowSizeBytes: int | java.jlong | java.lang.Long, /) -> android.database.CursorWindow: ...

class DatabaseUtilsCompat(java.lang.Object):
    @staticmethod
    def appendSelectionArgs(originalValues: java.chaquopy.JavaArray[java.lang.String], newValues: java.chaquopy.JavaArray[java.lang.String], /) -> java.chaquopy.JavaArray[java.lang.String]: ...
    @staticmethod
    def concatenateWhere(a: str | java.lang.String, b: str | java.lang.String, /) -> str: ...
