import typing

import android.net
import java.io
import java.lang

class UriKt(java.lang.Object):
    @staticmethod
    def toFile(receiver: android.net.Uri, /) -> java.io.File: ...
    @typing.overload
    @staticmethod
    def toUri(receiver: java.io.File, /) -> android.net.Uri: ...
    @typing.overload
    @staticmethod
    def toUri(receiver: str | java.lang.String, /) -> android.net.Uri: ...
