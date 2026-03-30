import android.telephony
import java
import java.lang

class SubscriptionManagerCompat(java.lang.Object):
    @staticmethod
    def getSlotIndex(subId: int | java.jint | java.lang.Integer, /) -> int: ...

class TelephonyManagerCompat(java.lang.Object):
    @staticmethod
    def getImei(telephonyManager: android.telephony.TelephonyManager, /) -> str: ...
    @staticmethod
    def getSubscriptionId(telephonyManager: android.telephony.TelephonyManager, /) -> int: ...
