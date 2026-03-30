import typing

import java.chaquopy
import java.lang
import java.lang.instrument
import java.security

class AgentPremain(java.lang.Object):
    INSTANCE: typing.ClassVar[AgentPremain] = ...
    @staticmethod
    def premain(args: str | java.lang.String, instrumentation: java.lang.instrument.Instrumentation, /) -> None: ...

    class DebugProbesTransformer(java.lang.instrument.ClassFileTransformer):
        INSTANCE: typing.ClassVar[AgentPremain.DebugProbesTransformer] = ...
        def transform(self, loader: java.lang.ClassLoader, className: str | java.lang.String, classBeingRedefined: typing.Type[java.lang.Object], protectionDomain: java.security.ProtectionDomain, classfileBuffer: java.chaquopy.JavaArrayJByte, /) -> java.chaquopy.JavaArrayJByte: ...
