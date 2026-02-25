import java.lang
import java.lang.invoke
import typing



class ObjectMethods(java.lang.Object):
    @staticmethod
    def bootstrap(lookup: java.lang.invoke.MethodHandles.Lookup, methodName: str | java.lang.String, type: java.lang.invoke.TypeDescriptor, recordClass: typing.Type[java.lang.Object], names: str | java.lang.String, /, *getters: java.lang.invoke.MethodHandle) -> java.lang.Object: ...

class SwitchBootstraps(java.lang.Object):
    @staticmethod
    def enumSwitch(lookup: java.lang.invoke.MethodHandles.Lookup, invocationName: str | java.lang.String, invocationType: java.lang.invoke.MethodType, /, *labels: java.lang.Object) -> java.lang.invoke.CallSite: ...
    @staticmethod
    def typeSwitch(lookup: java.lang.invoke.MethodHandles.Lookup, invocationName: str | java.lang.String, invocationType: java.lang.invoke.MethodType, /, *labels: java.lang.Object) -> java.lang.invoke.CallSite: ...
