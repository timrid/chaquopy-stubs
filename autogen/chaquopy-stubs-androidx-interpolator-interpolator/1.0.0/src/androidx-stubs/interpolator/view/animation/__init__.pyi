import android.view.animation
import java
import java.chaquopy
import java.lang

class FastOutLinearInInterpolator(LookupTableInterpolator):
    def __init__(self) -> None: ...

class FastOutSlowInInterpolator(LookupTableInterpolator):
    def __init__(self) -> None: ...

class LinearOutSlowInInterpolator(LookupTableInterpolator):
    def __init__(self) -> None: ...

class LookupTableInterpolator(android.view.animation.Interpolator):
    def __init__(self, values: java.chaquopy.JavaArrayJFloat, /) -> None: ...
    def getInterpolation(self, input: float | java.jfloat | java.lang.Float, /) -> float: ...
