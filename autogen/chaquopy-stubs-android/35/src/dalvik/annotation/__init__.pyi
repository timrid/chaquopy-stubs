import java.chaquopy
import java.lang
import java.lang.annotation
import typing



class TestTarget(java.lang.annotation.Annotation):
    def conceptName(self) -> str: ...
    def methodArgs(self) -> java.chaquopy.JavaArray[typing.Type[java.lang.Object]]: ...
    def methodName(self) -> str: ...

class TestTargetClass(java.lang.annotation.Annotation):
    def value(self) -> typing.Type[java.lang.Object]: ...
