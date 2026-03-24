import typing

import android.net
import java.io
import java.lang

class UriKt(java.lang.Object):
    @staticmethod
    def toFile(this_toFile: android.net.Uri, /) -> java.io.File: ...
    @typing.overload
    @staticmethod
    def toUri(this_toUri: java.io.File, /) -> android.net.Uri: ...
    @typing.overload
    @staticmethod
    def toUri(this_toUri: str | java.lang.String, /) -> android.net.Uri: ...
