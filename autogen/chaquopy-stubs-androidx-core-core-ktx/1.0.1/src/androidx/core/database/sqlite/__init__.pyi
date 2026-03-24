import typing

import android.database.sqlite
import java
import java.lang
import kotlin.jvm.functions

class SQLiteDatabaseKt(java.lang.Object):
    _transaction__T = typing.TypeVar('_transaction__T')  # <T>
    @staticmethod
    def transaction(receiver: android.database.sqlite.SQLiteDatabase, exclusive: bool | java.jboolean | java.lang.Boolean, body: kotlin.jvm.functions.Function1[android.database.sqlite.SQLiteDatabase, _transaction__T], /) -> _transaction__T: ...
