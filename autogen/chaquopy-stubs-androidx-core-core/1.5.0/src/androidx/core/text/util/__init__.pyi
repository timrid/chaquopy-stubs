import typing

import android.text
import android.text.util
import android.widget
import java
import java.chaquopy
import java.lang
import java.lang.annotation
import java.util.regex

class FindAddress(java.lang.Object):
    @staticmethod
    def isValidLocationName(location: str | java.lang.String, /) -> bool: ...
    @typing.overload
    @staticmethod
    def isValidZipCode(zipCode: str | java.lang.String, /) -> bool: ...
    @typing.overload
    @staticmethod
    def isValidZipCode(zipCode: str | java.lang.String, state: str | java.lang.String, /) -> bool: ...
    @staticmethod
    def matchHouseNumber(content: str | java.lang.String, offset: int | java.jint | java.lang.Integer, /) -> java.util.regex.MatchResult: ...
    @staticmethod
    def matchState(content: str | java.lang.String, offset: int | java.jint | java.lang.Integer, /) -> java.util.regex.MatchResult: ...

class LinkifyCompat(java.lang.Object):
    @typing.overload
    @staticmethod
    def addLinks(text: android.text.Spannable, mask: int | java.jint | java.lang.Integer, /) -> bool: ...
    @typing.overload
    @staticmethod
    def addLinks(text: android.widget.TextView, mask: int | java.jint | java.lang.Integer, /) -> bool: ...
    @typing.overload
    @staticmethod
    def addLinks(text: android.text.Spannable, pattern: java.util.regex.Pattern, scheme: str | java.lang.String, /) -> bool: ...
    @typing.overload
    @staticmethod
    def addLinks(text: android.widget.TextView, pattern: java.util.regex.Pattern, scheme: str | java.lang.String, /) -> None: ...
    @typing.overload
    @staticmethod
    def addLinks(spannable: android.text.Spannable, pattern: java.util.regex.Pattern, scheme: str | java.lang.String, matchFilter: android.text.util.Linkify.MatchFilter, transformFilter: android.text.util.Linkify.TransformFilter, /) -> bool: ...
    @typing.overload
    @staticmethod
    def addLinks(text: android.widget.TextView, pattern: java.util.regex.Pattern, scheme: str | java.lang.String, matchFilter: android.text.util.Linkify.MatchFilter, transformFilter: android.text.util.Linkify.TransformFilter, /) -> None: ...
    @typing.overload
    @staticmethod
    def addLinks(spannable: android.text.Spannable, pattern: java.util.regex.Pattern, defaultScheme: str | java.lang.String, schemes: java.chaquopy.JavaArray[java.lang.String], matchFilter: android.text.util.Linkify.MatchFilter, transformFilter: android.text.util.Linkify.TransformFilter, /) -> bool: ...
    @typing.overload
    @staticmethod
    def addLinks(text: android.widget.TextView, pattern: java.util.regex.Pattern, defaultScheme: str | java.lang.String, schemes: java.chaquopy.JavaArray[java.lang.String], matchFilter: android.text.util.Linkify.MatchFilter, transformFilter: android.text.util.Linkify.TransformFilter, /) -> None: ...

    class LinkifyMask(java.lang.annotation.Annotation): ...
