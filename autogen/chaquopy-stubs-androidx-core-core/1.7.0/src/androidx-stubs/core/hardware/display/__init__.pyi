import typing

import android.content
import android.view
import java
import java.chaquopy
import java.lang

class DisplayManagerCompat(java.lang.Object):
    DISPLAY_CATEGORY_PRESENTATION: typing.ClassVar[str] = ...
    def getDisplay(self, displayId: int | java.jint | java.lang.Integer, /) -> android.view.Display: ...
    @typing.overload
    def getDisplays(self) -> java.chaquopy.JavaArray[android.view.Display]: ...
    @typing.overload
    def getDisplays(self, category: str | java.lang.String, /) -> java.chaquopy.JavaArray[android.view.Display]: ...
    @staticmethod
    def getInstance(context: android.content.Context, /) -> DisplayManagerCompat: ...
