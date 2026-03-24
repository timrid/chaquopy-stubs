import typing

import android.content.res
import java.lang

class RippleUtils(java.lang.Object):
    USE_FRAMEWORK_RIPPLE: typing.ClassVar[bool] = ...
    @staticmethod
    def convertToRippleDrawableColor(rippleColor: android.content.res.ColorStateList, /) -> android.content.res.ColorStateList: ...
