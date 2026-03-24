import java.lang
import java.util.regex
import kotlin.internal.jdk7
import kotlin.text

class JDK8PlatformImplementations(kotlin.internal.jdk7.JDK7PlatformImplementations):
    def __init__(self) -> None: ...
    def getMatchResultNamedGroup(self, matchResult: java.util.regex.MatchResult, name: str | java.lang.String, /) -> kotlin.text.MatchGroup: ...
