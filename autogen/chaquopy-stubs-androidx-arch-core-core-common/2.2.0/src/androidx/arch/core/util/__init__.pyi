import typing

import java.lang

_Function__I = typing.TypeVar('_Function__I')  # <I>
_Function__O = typing.TypeVar('_Function__O')  # <O>
class Function(java.lang.Object, typing.Generic[_Function__I, _Function__O]):
    def apply(self, arg1: _Function__I, /) -> _Function__O: ...
