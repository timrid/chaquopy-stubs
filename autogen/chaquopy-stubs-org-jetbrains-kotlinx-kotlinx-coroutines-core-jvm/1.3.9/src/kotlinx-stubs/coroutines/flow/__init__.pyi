import typing

import java
import java.chaquopy
import java.lang
import java.util
import kotlin
import kotlin.collections
import kotlin.coroutines
import kotlin.jvm.functions
import kotlin.ranges
import kotlin.sequences
import kotlinx.coroutines
import kotlinx.coroutines.channels
import kotlinx.coroutines.flow.internal

_AbstractFlow__T = typing.TypeVar('_AbstractFlow__T')  # <T>
class AbstractFlow(Flow[_AbstractFlow__T], typing.Generic[_AbstractFlow__T]):
    def __init__(self) -> None: ...
    def collect(self, collector: FlowCollector[_AbstractFlow__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def collectSafely(self, arg1: FlowCollector[_AbstractFlow__T], arg2: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...

_CallbackFlowBuilder__T = typing.TypeVar('_CallbackFlowBuilder__T')  # <T>
class CallbackFlowBuilder(ChannelFlowBuilder[_CallbackFlowBuilder__T], typing.Generic[_CallbackFlowBuilder__T]):
    def __init__(self, block: kotlin.jvm.functions.Function2[kotlinx.coroutines.channels.ProducerScope[_CallbackFlowBuilder__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> None: ...
    def collectTo(self, scope: kotlinx.coroutines.channels.ProducerScope[_CallbackFlowBuilder__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def create(self, context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> kotlinx.coroutines.flow.internal.ChannelFlow[_CallbackFlowBuilder__T]: ...

_ChannelAsFlow__T = typing.TypeVar('_ChannelAsFlow__T')  # <T>
class ChannelAsFlow(kotlinx.coroutines.flow.internal.ChannelFlow[_ChannelAsFlow__T], typing.Generic[_ChannelAsFlow__T]):
    def __init__(self, channel: kotlinx.coroutines.channels.ReceiveChannel[_ChannelAsFlow__T], consume: bool | java.jboolean | java.lang.Boolean, context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> None: ...
    def additionalToStringProps(self) -> str: ...
    def broadcastImpl(self, scope: kotlinx.coroutines.CoroutineScope, start: kotlinx.coroutines.CoroutineStart, /) -> kotlinx.coroutines.channels.BroadcastChannel[_ChannelAsFlow__T]: ...
    def collect(self, collector: FlowCollector[_ChannelAsFlow__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def collectTo(self, scope: kotlinx.coroutines.channels.ProducerScope[_ChannelAsFlow__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def create(self, context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> kotlinx.coroutines.flow.internal.ChannelFlow[_ChannelAsFlow__T]: ...
    def produceImpl(self, scope: kotlinx.coroutines.CoroutineScope, /) -> kotlinx.coroutines.channels.ReceiveChannel[_ChannelAsFlow__T]: ...

_ChannelFlowBuilder__T = typing.TypeVar('_ChannelFlowBuilder__T')  # <T>
class ChannelFlowBuilder(kotlinx.coroutines.flow.internal.ChannelFlow[_ChannelFlowBuilder__T], typing.Generic[_ChannelFlowBuilder__T]):
    def __init__(self, block: kotlin.jvm.functions.Function2[kotlinx.coroutines.channels.ProducerScope[_ChannelFlowBuilder__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> None: ...
    def collectTo(self, arg1: kotlinx.coroutines.channels.ProducerScope[_ChannelFlowBuilder__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def create(self, context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> kotlinx.coroutines.flow.internal.ChannelFlow[_ChannelFlowBuilder__T]: ...
    def toString(self) -> str: ...

class EmptyFlow(Flow):
    INSTANCE: typing.ClassVar[EmptyFlow] = ...
    def collect(self, collector: FlowCollector[java.lang.Object], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...

_Flow__T = typing.TypeVar('_Flow__T')  # <T>
class Flow(java.lang.Object, typing.Generic[_Flow__T]):
    def collect(self, arg1: FlowCollector[_Flow__T], arg2: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...

_FlowCollector__T = typing.TypeVar('_FlowCollector__T')  # <T>
class FlowCollector(java.lang.Object, typing.Generic[_FlowCollector__T]):
    def emit(self, arg1: _FlowCollector__T, arg2: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...

class FlowKt(java.lang.Object):
    DEFAULT_CONCURRENCY_PROPERTY_NAME: typing.ClassVar[str] = ...
    _asFlow_0__T = typing.TypeVar('_asFlow_0__T')  # <T>
    _asFlow_1__T = typing.TypeVar('_asFlow_1__T')  # <T>
    _asFlow_2__T = typing.TypeVar('_asFlow_2__T')  # <T>
    _asFlow_3__T = typing.TypeVar('_asFlow_3__T')  # <T>
    _asFlow_6__T = typing.TypeVar('_asFlow_6__T')  # <T>
    _asFlow_7__T = typing.TypeVar('_asFlow_7__T')  # <T>
    _asFlow_10__T = typing.TypeVar('_asFlow_10__T')  # <T>
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: java.lang.Iterable[_asFlow_0__T], /) -> Flow[_asFlow_0__T]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: java.util.Iterator[_asFlow_1__T], /) -> Flow[_asFlow_1__T]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: kotlin.jvm.functions.Function0[_asFlow_2__T], /) -> Flow[_asFlow_2__T]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: kotlin.jvm.functions.Function1[kotlin.coroutines.Continuation[_asFlow_3__T], java.lang.Object], /) -> Flow[_asFlow_3__T]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: kotlin.ranges.IntRange, /) -> Flow[java.lang.Integer]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: kotlin.ranges.LongRange, /) -> Flow[java.lang.Long]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: kotlin.sequences.Sequence[_asFlow_6__T], /) -> Flow[_asFlow_6__T]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: kotlinx.coroutines.channels.BroadcastChannel[_asFlow_7__T], /) -> Flow[_asFlow_7__T]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: java.chaquopy.JavaArrayJInt, /) -> Flow[java.lang.Integer]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: java.chaquopy.JavaArrayJLong, /) -> Flow[java.lang.Long]: ...
    @typing.overload
    @staticmethod
    def asFlow(this_asFlow: java.chaquopy.JavaArray[_asFlow_10__T], /) -> Flow[_asFlow_10__T]: ...
    _broadcastIn__T = typing.TypeVar('_broadcastIn__T')  # <T>
    @staticmethod
    def broadcastIn(this_broadcastIn: Flow[_broadcastIn__T], scope: kotlinx.coroutines.CoroutineScope, start: kotlinx.coroutines.CoroutineStart, /) -> kotlinx.coroutines.channels.BroadcastChannel[_broadcastIn__T]: ...
    _buffer__T = typing.TypeVar('_buffer__T')  # <T>
    @staticmethod
    def buffer(this_buffer: Flow[_buffer__T], capacity: int | java.jint | java.lang.Integer, /) -> Flow[_buffer__T]: ...
    _callbackFlow__T = typing.TypeVar('_callbackFlow__T')  # <T>
    @staticmethod
    def callbackFlow(block: kotlin.jvm.functions.Function2[kotlinx.coroutines.channels.ProducerScope[_callbackFlow__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_callbackFlow__T]: ...
    _cancellable__T = typing.TypeVar('_cancellable__T')  # <T>
    @staticmethod
    def cancellable(this_cancellable: Flow[_cancellable__T], /) -> Flow[_cancellable__T]: ...
    _catch__T = typing.TypeVar('_catch__T')  # <T>
    @staticmethod
    def catch(this_catch: Flow[_catch__T], action: kotlin.jvm.functions.Function3[FlowCollector[_catch__T], java.lang.Throwable, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_catch__T]: ...
    _catchImpl__T = typing.TypeVar('_catchImpl__T')  # <T>
    @staticmethod
    def catchImpl(this_catchImpl: Flow[_catchImpl__T], collector: FlowCollector[_catchImpl__T], completion: kotlin.coroutines.Continuation[java.lang.Throwable], /) -> java.lang.Object: ...
    _channelFlow__T = typing.TypeVar('_channelFlow__T')  # <T>
    @staticmethod
    def channelFlow(block: kotlin.jvm.functions.Function2[kotlinx.coroutines.channels.ProducerScope[_channelFlow__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_channelFlow__T]: ...
    _collect_1__T = typing.TypeVar('_collect_1__T')  # <T>
    @typing.overload
    @staticmethod
    def collect(this_collect: Flow[java.lang.Object], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def collect(this_collect: Flow[_collect_1__T], action: kotlin.jvm.functions.Function2[_collect_1__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    _collectIndexed__T = typing.TypeVar('_collectIndexed__T')  # <T>
    @staticmethod
    def collectIndexed(this_collectIndexed: Flow[_collectIndexed__T], action: kotlin.jvm.functions.Function3[int, _collectIndexed__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    _collectLatest__T = typing.TypeVar('_collectLatest__T')  # <T>
    @staticmethod
    def collectLatest(this_collectLatest: Flow[_collectLatest__T], action: kotlin.jvm.functions.Function2[_collectLatest__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    _collectWhile__T = typing.TypeVar('_collectWhile__T')  # <T>
    @staticmethod
    def collectWhile(this_collectWhile: Flow[_collectWhile__T], predicate: kotlin.jvm.functions.Function2[_collectWhile__T, kotlin.coroutines.Continuation[bool], java.lang.Object], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    _combine_0__T1 = typing.TypeVar('_combine_0__T1')  # <T1>
    _combine_0__T2 = typing.TypeVar('_combine_0__T2')  # <T2>
    _combine_0__R = typing.TypeVar('_combine_0__R')  # <R>
    _combine_1__T1 = typing.TypeVar('_combine_1__T1')  # <T1>
    _combine_1__T2 = typing.TypeVar('_combine_1__T2')  # <T2>
    _combine_1__T3 = typing.TypeVar('_combine_1__T3')  # <T3>
    _combine_1__R = typing.TypeVar('_combine_1__R')  # <R>
    _combine_2__T1 = typing.TypeVar('_combine_2__T1')  # <T1>
    _combine_2__T2 = typing.TypeVar('_combine_2__T2')  # <T2>
    _combine_2__T3 = typing.TypeVar('_combine_2__T3')  # <T3>
    _combine_2__T4 = typing.TypeVar('_combine_2__T4')  # <T4>
    _combine_2__R = typing.TypeVar('_combine_2__R')  # <R>
    _combine_3__T1 = typing.TypeVar('_combine_3__T1')  # <T1>
    _combine_3__T2 = typing.TypeVar('_combine_3__T2')  # <T2>
    _combine_3__T3 = typing.TypeVar('_combine_3__T3')  # <T3>
    _combine_3__T4 = typing.TypeVar('_combine_3__T4')  # <T4>
    _combine_3__T5 = typing.TypeVar('_combine_3__T5')  # <T5>
    _combine_3__R = typing.TypeVar('_combine_3__R')  # <R>
    @typing.overload
    @staticmethod
    def combine(flow: Flow[_combine_0__T1], flow2: Flow[_combine_0__T2], transform: kotlin.jvm.functions.Function3[_combine_0__T1, _combine_0__T2, kotlin.coroutines.Continuation[_combine_0__R], java.lang.Object], /) -> Flow[_combine_0__R]: ...
    @typing.overload
    @staticmethod
    def combine(flow: Flow[_combine_1__T1], flow2: Flow[_combine_1__T2], flow3: Flow[_combine_1__T3], transform: kotlin.jvm.functions.Function4[_combine_1__T1, _combine_1__T2, _combine_1__T3, kotlin.coroutines.Continuation[_combine_1__R], java.lang.Object], /) -> Flow[_combine_1__R]: ...
    @typing.overload
    @staticmethod
    def combine(flow: Flow[_combine_2__T1], flow2: Flow[_combine_2__T2], flow3: Flow[_combine_2__T3], flow4: Flow[_combine_2__T4], transform: kotlin.jvm.functions.Function5[_combine_2__T1, _combine_2__T2, _combine_2__T3, _combine_2__T4, kotlin.coroutines.Continuation[_combine_2__R], java.lang.Object], /) -> Flow[_combine_2__R]: ...
    @typing.overload
    @staticmethod
    def combine(flow: Flow[_combine_3__T1], flow2: Flow[_combine_3__T2], flow3: Flow[_combine_3__T3], flow4: Flow[_combine_3__T4], flow5: Flow[_combine_3__T5], transform: kotlin.jvm.functions.Function6[_combine_3__T1, _combine_3__T2, _combine_3__T3, _combine_3__T4, _combine_3__T5, kotlin.coroutines.Continuation[_combine_3__R], java.lang.Object], /) -> Flow[_combine_3__R]: ...
    _combineLatest_0__T1 = typing.TypeVar('_combineLatest_0__T1')  # <T1>
    _combineLatest_0__T2 = typing.TypeVar('_combineLatest_0__T2')  # <T2>
    _combineLatest_0__R = typing.TypeVar('_combineLatest_0__R')  # <R>
    _combineLatest_1__T1 = typing.TypeVar('_combineLatest_1__T1')  # <T1>
    _combineLatest_1__T2 = typing.TypeVar('_combineLatest_1__T2')  # <T2>
    _combineLatest_1__T3 = typing.TypeVar('_combineLatest_1__T3')  # <T3>
    _combineLatest_1__R = typing.TypeVar('_combineLatest_1__R')  # <R>
    _combineLatest_2__T1 = typing.TypeVar('_combineLatest_2__T1')  # <T1>
    _combineLatest_2__T2 = typing.TypeVar('_combineLatest_2__T2')  # <T2>
    _combineLatest_2__T3 = typing.TypeVar('_combineLatest_2__T3')  # <T3>
    _combineLatest_2__T4 = typing.TypeVar('_combineLatest_2__T4')  # <T4>
    _combineLatest_2__R = typing.TypeVar('_combineLatest_2__R')  # <R>
    _combineLatest_3__T1 = typing.TypeVar('_combineLatest_3__T1')  # <T1>
    _combineLatest_3__T2 = typing.TypeVar('_combineLatest_3__T2')  # <T2>
    _combineLatest_3__T3 = typing.TypeVar('_combineLatest_3__T3')  # <T3>
    _combineLatest_3__T4 = typing.TypeVar('_combineLatest_3__T4')  # <T4>
    _combineLatest_3__T5 = typing.TypeVar('_combineLatest_3__T5')  # <T5>
    _combineLatest_3__R = typing.TypeVar('_combineLatest_3__R')  # <R>
    @typing.overload
    @staticmethod
    def combineLatest(this_combineLatest: Flow[_combineLatest_0__T1], other: Flow[_combineLatest_0__T2], transform: kotlin.jvm.functions.Function3[_combineLatest_0__T1, _combineLatest_0__T2, kotlin.coroutines.Continuation[_combineLatest_0__R], java.lang.Object], /) -> Flow[_combineLatest_0__R]: ...
    @typing.overload
    @staticmethod
    def combineLatest(this_combineLatest: Flow[_combineLatest_1__T1], other: Flow[_combineLatest_1__T2], other2: Flow[_combineLatest_1__T3], transform: kotlin.jvm.functions.Function4[_combineLatest_1__T1, _combineLatest_1__T2, _combineLatest_1__T3, kotlin.coroutines.Continuation[_combineLatest_1__R], java.lang.Object], /) -> Flow[_combineLatest_1__R]: ...
    @typing.overload
    @staticmethod
    def combineLatest(this_combineLatest: Flow[_combineLatest_2__T1], other: Flow[_combineLatest_2__T2], other2: Flow[_combineLatest_2__T3], other3: Flow[_combineLatest_2__T4], transform: kotlin.jvm.functions.Function5[_combineLatest_2__T1, _combineLatest_2__T2, _combineLatest_2__T3, _combineLatest_2__T4, kotlin.coroutines.Continuation[_combineLatest_2__R], java.lang.Object], /) -> Flow[_combineLatest_2__R]: ...
    @typing.overload
    @staticmethod
    def combineLatest(this_combineLatest: Flow[_combineLatest_3__T1], other: Flow[_combineLatest_3__T2], other2: Flow[_combineLatest_3__T3], other3: Flow[_combineLatest_3__T4], other4: Flow[_combineLatest_3__T5], transform: kotlin.jvm.functions.Function6[_combineLatest_3__T1, _combineLatest_3__T2, _combineLatest_3__T3, _combineLatest_3__T4, _combineLatest_3__T5, kotlin.coroutines.Continuation[_combineLatest_3__R], java.lang.Object], /) -> Flow[_combineLatest_3__R]: ...
    _combineTransform_0__T1 = typing.TypeVar('_combineTransform_0__T1')  # <T1>
    _combineTransform_0__T2 = typing.TypeVar('_combineTransform_0__T2')  # <T2>
    _combineTransform_0__R = typing.TypeVar('_combineTransform_0__R')  # <R>
    _combineTransform_1__T1 = typing.TypeVar('_combineTransform_1__T1')  # <T1>
    _combineTransform_1__T2 = typing.TypeVar('_combineTransform_1__T2')  # <T2>
    _combineTransform_1__T3 = typing.TypeVar('_combineTransform_1__T3')  # <T3>
    _combineTransform_1__R = typing.TypeVar('_combineTransform_1__R')  # <R>
    _combineTransform_2__T1 = typing.TypeVar('_combineTransform_2__T1')  # <T1>
    _combineTransform_2__T2 = typing.TypeVar('_combineTransform_2__T2')  # <T2>
    _combineTransform_2__T3 = typing.TypeVar('_combineTransform_2__T3')  # <T3>
    _combineTransform_2__T4 = typing.TypeVar('_combineTransform_2__T4')  # <T4>
    _combineTransform_2__R = typing.TypeVar('_combineTransform_2__R')  # <R>
    _combineTransform_3__T1 = typing.TypeVar('_combineTransform_3__T1')  # <T1>
    _combineTransform_3__T2 = typing.TypeVar('_combineTransform_3__T2')  # <T2>
    _combineTransform_3__T3 = typing.TypeVar('_combineTransform_3__T3')  # <T3>
    _combineTransform_3__T4 = typing.TypeVar('_combineTransform_3__T4')  # <T4>
    _combineTransform_3__T5 = typing.TypeVar('_combineTransform_3__T5')  # <T5>
    _combineTransform_3__R = typing.TypeVar('_combineTransform_3__R')  # <R>
    @typing.overload
    @staticmethod
    def combineTransform(flow: Flow[_combineTransform_0__T1], flow2: Flow[_combineTransform_0__T2], transform: kotlin.jvm.functions.Function4[FlowCollector[_combineTransform_0__R], _combineTransform_0__T1, _combineTransform_0__T2, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_combineTransform_0__R]: ...
    @typing.overload
    @staticmethod
    def combineTransform(flow: Flow[_combineTransform_1__T1], flow2: Flow[_combineTransform_1__T2], flow3: Flow[_combineTransform_1__T3], transform: kotlin.jvm.functions.Function5[FlowCollector[_combineTransform_1__R], _combineTransform_1__T1, _combineTransform_1__T2, _combineTransform_1__T3, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_combineTransform_1__R]: ...
    @typing.overload
    @staticmethod
    def combineTransform(flow: Flow[_combineTransform_2__T1], flow2: Flow[_combineTransform_2__T2], flow3: Flow[_combineTransform_2__T3], flow4: Flow[_combineTransform_2__T4], transform: kotlin.jvm.functions.Function6[FlowCollector[_combineTransform_2__R], _combineTransform_2__T1, _combineTransform_2__T2, _combineTransform_2__T3, _combineTransform_2__T4, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_combineTransform_2__R]: ...
    @typing.overload
    @staticmethod
    def combineTransform(flow: Flow[_combineTransform_3__T1], flow2: Flow[_combineTransform_3__T2], flow3: Flow[_combineTransform_3__T3], flow4: Flow[_combineTransform_3__T4], flow5: Flow[_combineTransform_3__T5], transform: kotlin.jvm.functions.Function7[FlowCollector[_combineTransform_3__R], _combineTransform_3__T1, _combineTransform_3__T2, _combineTransform_3__T3, _combineTransform_3__T4, _combineTransform_3__T5, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_combineTransform_3__R]: ...
    _compose__T = typing.TypeVar('_compose__T')  # <T>
    _compose__R = typing.TypeVar('_compose__R')  # <R>
    @staticmethod
    def compose(this_compose: Flow[_compose__T], transformer: kotlin.jvm.functions.Function1[Flow[_compose__T], Flow[_compose__R]], /) -> Flow[_compose__R]: ...
    _concatMap__T = typing.TypeVar('_concatMap__T')  # <T>
    _concatMap__R = typing.TypeVar('_concatMap__R')  # <R>
    @staticmethod
    def concatMap(this_concatMap: Flow[_concatMap__T], mapper: kotlin.jvm.functions.Function1[_concatMap__T, Flow[_concatMap__R]], /) -> Flow[_concatMap__R]: ...
    _concatWith_0__T = typing.TypeVar('_concatWith_0__T')  # <T>
    _concatWith_1__T = typing.TypeVar('_concatWith_1__T')  # <T>
    @typing.overload
    @staticmethod
    def concatWith(this_concatWith: Flow[_concatWith_0__T], value: _concatWith_0__T, /) -> Flow[_concatWith_0__T]: ...
    @typing.overload
    @staticmethod
    def concatWith(this_concatWith: Flow[_concatWith_1__T], other: Flow[_concatWith_1__T], /) -> Flow[_concatWith_1__T]: ...
    _conflate__T = typing.TypeVar('_conflate__T')  # <T>
    @staticmethod
    def conflate(this_conflate: Flow[_conflate__T], /) -> Flow[_conflate__T]: ...
    _consumeAsFlow__T = typing.TypeVar('_consumeAsFlow__T')  # <T>
    @staticmethod
    def consumeAsFlow(this_consumeAsFlow: kotlinx.coroutines.channels.ReceiveChannel[_consumeAsFlow__T], /) -> Flow[_consumeAsFlow__T]: ...
    _count_1__T = typing.TypeVar('_count_1__T')  # <T>
    @typing.overload
    @staticmethod
    def count(this_count: Flow[java.lang.Object], completion: kotlin.coroutines.Continuation[int], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def count(this_count: Flow[_count_1__T], predicate: kotlin.jvm.functions.Function2[_count_1__T, kotlin.coroutines.Continuation[bool], java.lang.Object], completion: kotlin.coroutines.Continuation[int], /) -> java.lang.Object: ...
    _debounce__T = typing.TypeVar('_debounce__T')  # <T>
    @staticmethod
    def debounce(this_debounce: Flow[_debounce__T], timeoutMillis: int | java.jlong | java.lang.Long, /) -> Flow[_debounce__T]: ...
    _delayEach__T = typing.TypeVar('_delayEach__T')  # <T>
    @staticmethod
    def delayEach(this_delayEach: Flow[_delayEach__T], timeMillis: int | java.jlong | java.lang.Long, /) -> Flow[_delayEach__T]: ...
    _delayFlow__T = typing.TypeVar('_delayFlow__T')  # <T>
    @staticmethod
    def delayFlow(this_delayFlow: Flow[_delayFlow__T], timeMillis: int | java.jlong | java.lang.Long, /) -> Flow[_delayFlow__T]: ...
    _distinctUntilChanged_0__T = typing.TypeVar('_distinctUntilChanged_0__T')  # <T>
    _distinctUntilChanged_1__T = typing.TypeVar('_distinctUntilChanged_1__T')  # <T>
    @typing.overload
    @staticmethod
    def distinctUntilChanged(this_distinctUntilChanged: Flow[_distinctUntilChanged_0__T], /) -> Flow[_distinctUntilChanged_0__T]: ...
    @typing.overload
    @staticmethod
    def distinctUntilChanged(this_distinctUntilChanged: Flow[_distinctUntilChanged_1__T], areEquivalent: kotlin.jvm.functions.Function2[_distinctUntilChanged_1__T, _distinctUntilChanged_1__T, java.lang.Boolean], /) -> Flow[_distinctUntilChanged_1__T]: ...
    _distinctUntilChangedBy__T = typing.TypeVar('_distinctUntilChangedBy__T')  # <T>
    @staticmethod
    def distinctUntilChangedBy(this_distinctUntilChangedBy: Flow[_distinctUntilChangedBy__T], keySelector: kotlin.jvm.functions.Function1[_distinctUntilChangedBy__T, java.lang.Object], /) -> Flow[_distinctUntilChangedBy__T]: ...
    _drop__T = typing.TypeVar('_drop__T')  # <T>
    @staticmethod
    def drop(this_drop: Flow[_drop__T], count: int | java.jint | java.lang.Integer, /) -> Flow[_drop__T]: ...
    _dropWhile__T = typing.TypeVar('_dropWhile__T')  # <T>
    @staticmethod
    def dropWhile(this_dropWhile: Flow[_dropWhile__T], predicate: kotlin.jvm.functions.Function2[_dropWhile__T, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_dropWhile__T]: ...
    _emitAll_0__T = typing.TypeVar('_emitAll_0__T')  # <T>
    _emitAll_1__T = typing.TypeVar('_emitAll_1__T')  # <T>
    @typing.overload
    @staticmethod
    def emitAll(this_emitAll: FlowCollector[_emitAll_0__T], channel: kotlinx.coroutines.channels.ReceiveChannel[_emitAll_0__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def emitAll(this_emitAll: FlowCollector[_emitAll_1__T], flow: Flow[_emitAll_1__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    @staticmethod
    def emptyFlow() -> Flow[java.lang.Object]: ...
    _filter__T = typing.TypeVar('_filter__T')  # <T>
    @staticmethod
    def filter(this_filter: Flow[_filter__T], predicate: kotlin.jvm.functions.Function2[_filter__T, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_filter__T]: ...
    _filterNot__T = typing.TypeVar('_filterNot__T')  # <T>
    @staticmethod
    def filterNot(this_filterNot: Flow[_filterNot__T], predicate: kotlin.jvm.functions.Function2[_filterNot__T, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_filterNot__T]: ...
    _filterNotNull__T = typing.TypeVar('_filterNotNull__T')  # <T>
    @staticmethod
    def filterNotNull(this_filterNotNull: Flow[_filterNotNull__T], /) -> Flow[_filterNotNull__T]: ...
    _first_0__T = typing.TypeVar('_first_0__T')  # <T>
    _first_1__T = typing.TypeVar('_first_1__T')  # <T>
    @typing.overload
    @staticmethod
    def first(this_first: Flow[_first_0__T], completion: kotlin.coroutines.Continuation[_first_0__T], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def first(this_first: Flow[_first_1__T], predicate: kotlin.jvm.functions.Function2[_first_1__T, kotlin.coroutines.Continuation[bool], java.lang.Object], completion: kotlin.coroutines.Continuation[_first_1__T], /) -> java.lang.Object: ...
    _firstOrNull_0__T = typing.TypeVar('_firstOrNull_0__T')  # <T>
    _firstOrNull_1__T = typing.TypeVar('_firstOrNull_1__T')  # <T>
    @typing.overload
    @staticmethod
    def firstOrNull(this_firstOrNull: Flow[_firstOrNull_0__T], completion: kotlin.coroutines.Continuation[_firstOrNull_0__T], /) -> java.lang.Object: ...
    @typing.overload
    @staticmethod
    def firstOrNull(this_firstOrNull: Flow[_firstOrNull_1__T], predicate: kotlin.jvm.functions.Function2[_firstOrNull_1__T, kotlin.coroutines.Continuation[bool], java.lang.Object], completion: kotlin.coroutines.Continuation[_firstOrNull_1__T], /) -> java.lang.Object: ...
    @staticmethod
    def fixedPeriodTicker(this_fixedPeriodTicker: kotlinx.coroutines.CoroutineScope, delayMillis: int | java.jlong | java.lang.Long, initialDelayMillis: int | java.jlong | java.lang.Long, /) -> kotlinx.coroutines.channels.ReceiveChannel[kotlin.Unit]: ...
    _flatMap__T = typing.TypeVar('_flatMap__T')  # <T>
    _flatMap__R = typing.TypeVar('_flatMap__R')  # <R>
    @staticmethod
    def flatMap(this_flatMap: Flow[_flatMap__T], mapper: kotlin.jvm.functions.Function2[_flatMap__T, kotlin.coroutines.Continuation[Flow[_flatMap__R]], java.lang.Object], /) -> Flow[_flatMap__R]: ...
    _flatMapConcat__T = typing.TypeVar('_flatMapConcat__T')  # <T>
    _flatMapConcat__R = typing.TypeVar('_flatMapConcat__R')  # <R>
    @staticmethod
    def flatMapConcat(this_flatMapConcat: Flow[_flatMapConcat__T], transform: kotlin.jvm.functions.Function2[_flatMapConcat__T, kotlin.coroutines.Continuation[Flow[_flatMapConcat__R]], java.lang.Object], /) -> Flow[_flatMapConcat__R]: ...
    _flatMapLatest__T = typing.TypeVar('_flatMapLatest__T')  # <T>
    _flatMapLatest__R = typing.TypeVar('_flatMapLatest__R')  # <R>
    @staticmethod
    def flatMapLatest(this_flatMapLatest: Flow[_flatMapLatest__T], transform: kotlin.jvm.functions.Function2[_flatMapLatest__T, kotlin.coroutines.Continuation[Flow[_flatMapLatest__R]], java.lang.Object], /) -> Flow[_flatMapLatest__R]: ...
    _flatMapMerge__T = typing.TypeVar('_flatMapMerge__T')  # <T>
    _flatMapMerge__R = typing.TypeVar('_flatMapMerge__R')  # <R>
    @staticmethod
    def flatMapMerge(this_flatMapMerge: Flow[_flatMapMerge__T], concurrency: int | java.jint | java.lang.Integer, transform: kotlin.jvm.functions.Function2[_flatMapMerge__T, kotlin.coroutines.Continuation[Flow[_flatMapMerge__R]], java.lang.Object], /) -> Flow[_flatMapMerge__R]: ...
    _flatten__T = typing.TypeVar('_flatten__T')  # <T>
    @staticmethod
    def flatten(this_flatten: Flow[Flow[_flatten__T]], /) -> Flow[_flatten__T]: ...
    _flattenConcat__T = typing.TypeVar('_flattenConcat__T')  # <T>
    @staticmethod
    def flattenConcat(this_flattenConcat: Flow[Flow[_flattenConcat__T]], /) -> Flow[_flattenConcat__T]: ...
    _flattenMerge__T = typing.TypeVar('_flattenMerge__T')  # <T>
    @staticmethod
    def flattenMerge(this_flattenMerge: Flow[Flow[_flattenMerge__T]], concurrency: int | java.jint | java.lang.Integer, /) -> Flow[_flattenMerge__T]: ...
    _flow__T = typing.TypeVar('_flow__T')  # <T>
    @staticmethod
    def flow(block: kotlin.jvm.functions.Function2[FlowCollector[_flow__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_flow__T]: ...
    _flowCombine__T1 = typing.TypeVar('_flowCombine__T1')  # <T1>
    _flowCombine__T2 = typing.TypeVar('_flowCombine__T2')  # <T2>
    _flowCombine__R = typing.TypeVar('_flowCombine__R')  # <R>
    @staticmethod
    def flowCombine(this_combine: Flow[_flowCombine__T1], flow: Flow[_flowCombine__T2], transform: kotlin.jvm.functions.Function3[_flowCombine__T1, _flowCombine__T2, kotlin.coroutines.Continuation[_flowCombine__R], java.lang.Object], /) -> Flow[_flowCombine__R]: ...
    _flowCombineTransform__T1 = typing.TypeVar('_flowCombineTransform__T1')  # <T1>
    _flowCombineTransform__T2 = typing.TypeVar('_flowCombineTransform__T2')  # <T2>
    _flowCombineTransform__R = typing.TypeVar('_flowCombineTransform__R')  # <R>
    @staticmethod
    def flowCombineTransform(this_combineTransform: Flow[_flowCombineTransform__T1], flow: Flow[_flowCombineTransform__T2], transform: kotlin.jvm.functions.Function4[FlowCollector[_flowCombineTransform__R], _flowCombineTransform__T1, _flowCombineTransform__T2, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_flowCombineTransform__R]: ...
    _flowOf_0__T = typing.TypeVar('_flowOf_0__T')  # <T>
    _flowOf_1__T = typing.TypeVar('_flowOf_1__T')  # <T>
    @typing.overload
    @staticmethod
    def flowOf(value: _flowOf_0__T, /) -> Flow[_flowOf_0__T]: ...
    @typing.overload
    @staticmethod
    def flowOf(*elements: _flowOf_1__T) -> Flow[_flowOf_1__T]: ...
    _flowOn__T = typing.TypeVar('_flowOn__T')  # <T>
    @staticmethod
    def flowOn(this_flowOn: Flow[_flowOn__T], context: kotlin.coroutines.CoroutineContext, /) -> Flow[_flowOn__T]: ...
    _flowViaChannel__T = typing.TypeVar('_flowViaChannel__T')  # <T>
    @staticmethod
    def flowViaChannel(bufferSize: int | java.jint | java.lang.Integer, block: kotlin.jvm.functions.Function2[kotlinx.coroutines.CoroutineScope, kotlinx.coroutines.channels.SendChannel[_flowViaChannel__T], kotlin.Unit], /) -> Flow[_flowViaChannel__T]: ...
    _flowWith__T = typing.TypeVar('_flowWith__T')  # <T>
    _flowWith__R = typing.TypeVar('_flowWith__R')  # <R>
    @staticmethod
    def flowWith(this_flowWith: Flow[_flowWith__T], flowContext: kotlin.coroutines.CoroutineContext, bufferSize: int | java.jint | java.lang.Integer, builder: kotlin.jvm.functions.Function1[Flow[_flowWith__T], Flow[_flowWith__R]], /) -> Flow[_flowWith__R]: ...
    _fold__T = typing.TypeVar('_fold__T')  # <T>
    _fold__R = typing.TypeVar('_fold__R')  # <R>
    @staticmethod
    def fold(this_fold: Flow[_fold__T], initial: _fold__R, operation: kotlin.jvm.functions.Function3[_fold__R, _fold__T, kotlin.coroutines.Continuation[_fold__R], java.lang.Object], completion: kotlin.coroutines.Continuation[_fold__R], /) -> java.lang.Object: ...
    _forEach__T = typing.TypeVar('_forEach__T')  # <T>
    @staticmethod
    def forEach(this_forEach: Flow[_forEach__T], action: kotlin.jvm.functions.Function2[_forEach__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> None: ...
    @staticmethod
    def getDEFAULT_CONCURRENCY() -> int: ...
    @staticmethod
    def launchIn(this_launchIn: Flow[java.lang.Object], scope: kotlinx.coroutines.CoroutineScope, /) -> kotlinx.coroutines.Job: ...
    _map__T = typing.TypeVar('_map__T')  # <T>
    _map__R = typing.TypeVar('_map__R')  # <R>
    @staticmethod
    def map(this_map: Flow[_map__T], transform: kotlin.jvm.functions.Function2[_map__T, kotlin.coroutines.Continuation[_map__R], java.lang.Object], /) -> Flow[_map__R]: ...
    _mapLatest__T = typing.TypeVar('_mapLatest__T')  # <T>
    _mapLatest__R = typing.TypeVar('_mapLatest__R')  # <R>
    @staticmethod
    def mapLatest(this_mapLatest: Flow[_mapLatest__T], transform: kotlin.jvm.functions.Function2[_mapLatest__T, kotlin.coroutines.Continuation[_mapLatest__R], java.lang.Object], /) -> Flow[_mapLatest__R]: ...
    _mapNotNull__T = typing.TypeVar('_mapNotNull__T')  # <T>
    _mapNotNull__R = typing.TypeVar('_mapNotNull__R')  # <R>
    @staticmethod
    def mapNotNull(this_mapNotNull: Flow[_mapNotNull__T], transform: kotlin.jvm.functions.Function2[_mapNotNull__T, kotlin.coroutines.Continuation[_mapNotNull__R], java.lang.Object], /) -> Flow[_mapNotNull__R]: ...
    _merge_0__T = typing.TypeVar('_merge_0__T')  # <T>
    _merge_1__T = typing.TypeVar('_merge_1__T')  # <T>
    _merge_2__T = typing.TypeVar('_merge_2__T')  # <T>
    @typing.overload
    @staticmethod
    def merge(this_merge: java.lang.Iterable[Flow[_merge_0__T]], /) -> Flow[_merge_0__T]: ...
    @typing.overload
    @staticmethod
    def merge(this_merge: Flow[Flow[_merge_1__T]], /) -> Flow[_merge_1__T]: ...
    @typing.overload
    @staticmethod
    def merge(*flows: Flow[_merge_2__T]) -> Flow[_merge_2__T]: ...
    @staticmethod
    def noImpl() -> None: ...
    _observeOn__T = typing.TypeVar('_observeOn__T')  # <T>
    @staticmethod
    def observeOn(this_observeOn: Flow[_observeOn__T], context: kotlin.coroutines.CoroutineContext, /) -> Flow[_observeOn__T]: ...
    _onCompletion__T = typing.TypeVar('_onCompletion__T')  # <T>
    @staticmethod
    def onCompletion(this_onCompletion: Flow[_onCompletion__T], action: kotlin.jvm.functions.Function3[FlowCollector[_onCompletion__T], java.lang.Throwable, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_onCompletion__T]: ...
    _onEach__T = typing.TypeVar('_onEach__T')  # <T>
    @staticmethod
    def onEach(this_onEach: Flow[_onEach__T], action: kotlin.jvm.functions.Function2[_onEach__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_onEach__T]: ...
    _onEmpty__T = typing.TypeVar('_onEmpty__T')  # <T>
    @staticmethod
    def onEmpty(this_onEmpty: Flow[_onEmpty__T], action: kotlin.jvm.functions.Function2[FlowCollector[_onEmpty__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_onEmpty__T]: ...
    _onErrorCollect__T = typing.TypeVar('_onErrorCollect__T')  # <T>
    @staticmethod
    def onErrorCollect(this_onErrorCollect: Flow[_onErrorCollect__T], fallback: Flow[_onErrorCollect__T], predicate: kotlin.jvm.functions.Function1[java.lang.Throwable, java.lang.Boolean], /) -> Flow[_onErrorCollect__T]: ...
    _onErrorResume__T = typing.TypeVar('_onErrorResume__T')  # <T>
    @staticmethod
    def onErrorResume(this_onErrorResume: Flow[_onErrorResume__T], fallback: Flow[_onErrorResume__T], /) -> Flow[_onErrorResume__T]: ...
    _onErrorResumeNext__T = typing.TypeVar('_onErrorResumeNext__T')  # <T>
    @staticmethod
    def onErrorResumeNext(this_onErrorResumeNext: Flow[_onErrorResumeNext__T], fallback: Flow[_onErrorResumeNext__T], /) -> Flow[_onErrorResumeNext__T]: ...
    _onErrorReturn_0__T = typing.TypeVar('_onErrorReturn_0__T')  # <T>
    _onErrorReturn_1__T = typing.TypeVar('_onErrorReturn_1__T')  # <T>
    @typing.overload
    @staticmethod
    def onErrorReturn(this_onErrorReturn: Flow[_onErrorReturn_0__T], fallback: _onErrorReturn_0__T, /) -> Flow[_onErrorReturn_0__T]: ...
    @typing.overload
    @staticmethod
    def onErrorReturn(this_onErrorReturn: Flow[_onErrorReturn_1__T], fallback: _onErrorReturn_1__T, predicate: kotlin.jvm.functions.Function1[java.lang.Throwable, java.lang.Boolean], /) -> Flow[_onErrorReturn_1__T]: ...
    _onStart__T = typing.TypeVar('_onStart__T')  # <T>
    @staticmethod
    def onStart(this_onStart: Flow[_onStart__T], action: kotlin.jvm.functions.Function2[FlowCollector[_onStart__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_onStart__T]: ...
    _produceIn__T = typing.TypeVar('_produceIn__T')  # <T>
    @staticmethod
    def produceIn(this_produceIn: Flow[_produceIn__T], scope: kotlinx.coroutines.CoroutineScope, /) -> kotlinx.coroutines.channels.ReceiveChannel[_produceIn__T]: ...
    _publishOn__T = typing.TypeVar('_publishOn__T')  # <T>
    @staticmethod
    def publishOn(this_publishOn: Flow[_publishOn__T], context: kotlin.coroutines.CoroutineContext, /) -> Flow[_publishOn__T]: ...
    _receiveAsFlow__T = typing.TypeVar('_receiveAsFlow__T')  # <T>
    @staticmethod
    def receiveAsFlow(this_receiveAsFlow: kotlinx.coroutines.channels.ReceiveChannel[_receiveAsFlow__T], /) -> Flow[_receiveAsFlow__T]: ...
    _reduce__S = typing.TypeVar('_reduce__S')  # <S>
    _reduce__T = typing.TypeVar('_reduce__T')  # <T>
    @staticmethod
    def reduce(this_reduce: Flow[_reduce__T], operation: kotlin.jvm.functions.Function3[_reduce__S, _reduce__T, kotlin.coroutines.Continuation[_reduce__S], java.lang.Object], completion: kotlin.coroutines.Continuation[_reduce__S], /) -> java.lang.Object: ...
    _retry__T = typing.TypeVar('_retry__T')  # <T>
    @staticmethod
    def retry(this_retry: Flow[_retry__T], retries: int | java.jlong | java.lang.Long, predicate: kotlin.jvm.functions.Function2[java.lang.Throwable, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_retry__T]: ...
    _retryWhen__T = typing.TypeVar('_retryWhen__T')  # <T>
    @staticmethod
    def retryWhen(this_retryWhen: Flow[_retryWhen__T], predicate: kotlin.jvm.functions.Function4[FlowCollector[_retryWhen__T], java.lang.Throwable, int, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_retryWhen__T]: ...
    _runningReduce__T = typing.TypeVar('_runningReduce__T')  # <T>
    @staticmethod
    def runningReduce(this_runningReduce: Flow[_runningReduce__T], operation: kotlin.jvm.functions.Function3[_runningReduce__T, _runningReduce__T, kotlin.coroutines.Continuation[_runningReduce__T], java.lang.Object], /) -> Flow[_runningReduce__T]: ...
    _sample__T = typing.TypeVar('_sample__T')  # <T>
    @staticmethod
    def sample(this_sample: Flow[_sample__T], periodMillis: int | java.jlong | java.lang.Long, /) -> Flow[_sample__T]: ...
    _scan__T = typing.TypeVar('_scan__T')  # <T>
    _scan__R = typing.TypeVar('_scan__R')  # <R>
    @staticmethod
    def scan(this_scan: Flow[_scan__T], initial: _scan__R, operation: kotlin.jvm.functions.Function3[_scan__R, _scan__T, kotlin.coroutines.Continuation[_scan__R], java.lang.Object], /) -> Flow[_scan__R]: ...
    _scanFold__T = typing.TypeVar('_scanFold__T')  # <T>
    _scanFold__R = typing.TypeVar('_scanFold__R')  # <R>
    @staticmethod
    def scanFold(this_scanFold: Flow[_scanFold__T], initial: _scanFold__R, operation: kotlin.jvm.functions.Function3[_scanFold__R, _scanFold__T, kotlin.coroutines.Continuation[_scanFold__R], java.lang.Object], /) -> Flow[_scanFold__R]: ...
    _scanReduce__T = typing.TypeVar('_scanReduce__T')  # <T>
    @staticmethod
    def scanReduce(this_scanReduce: Flow[_scanReduce__T], operation: kotlin.jvm.functions.Function3[_scanReduce__T, _scanReduce__T, kotlin.coroutines.Continuation[_scanReduce__T], java.lang.Object], /) -> Flow[_scanReduce__T]: ...
    _single__T = typing.TypeVar('_single__T')  # <T>
    @staticmethod
    def single(this_single: Flow[_single__T], completion: kotlin.coroutines.Continuation[_single__T], /) -> java.lang.Object: ...
    _singleOrNull__T = typing.TypeVar('_singleOrNull__T')  # <T>
    @staticmethod
    def singleOrNull(this_singleOrNull: Flow[_singleOrNull__T], completion: kotlin.coroutines.Continuation[_singleOrNull__T], /) -> java.lang.Object: ...
    _skip__T = typing.TypeVar('_skip__T')  # <T>
    @staticmethod
    def skip(this_skip: Flow[_skip__T], count: int | java.jint | java.lang.Integer, /) -> Flow[_skip__T]: ...
    _startWith_0__T = typing.TypeVar('_startWith_0__T')  # <T>
    _startWith_1__T = typing.TypeVar('_startWith_1__T')  # <T>
    @typing.overload
    @staticmethod
    def startWith(this_startWith: Flow[_startWith_0__T], value: _startWith_0__T, /) -> Flow[_startWith_0__T]: ...
    @typing.overload
    @staticmethod
    def startWith(this_startWith: Flow[_startWith_1__T], other: Flow[_startWith_1__T], /) -> Flow[_startWith_1__T]: ...
    _subscribe_1__T = typing.TypeVar('_subscribe_1__T')  # <T>
    _subscribe_2__T = typing.TypeVar('_subscribe_2__T')  # <T>
    @typing.overload
    @staticmethod
    def subscribe(this_subscribe: Flow[java.lang.Object], /) -> None: ...
    @typing.overload
    @staticmethod
    def subscribe(this_subscribe: Flow[_subscribe_1__T], onEach: kotlin.jvm.functions.Function2[_subscribe_1__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> None: ...
    @typing.overload
    @staticmethod
    def subscribe(this_subscribe: Flow[_subscribe_2__T], onEach: kotlin.jvm.functions.Function2[_subscribe_2__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], onError: kotlin.jvm.functions.Function2[java.lang.Throwable, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> None: ...
    _subscribeOn__T = typing.TypeVar('_subscribeOn__T')  # <T>
    @staticmethod
    def subscribeOn(this_subscribeOn: Flow[_subscribeOn__T], context: kotlin.coroutines.CoroutineContext, /) -> Flow[_subscribeOn__T]: ...
    _switchMap__T = typing.TypeVar('_switchMap__T')  # <T>
    _switchMap__R = typing.TypeVar('_switchMap__R')  # <R>
    @staticmethod
    def switchMap(this_switchMap: Flow[_switchMap__T], transform: kotlin.jvm.functions.Function2[_switchMap__T, kotlin.coroutines.Continuation[Flow[_switchMap__R]], java.lang.Object], /) -> Flow[_switchMap__R]: ...
    _take__T = typing.TypeVar('_take__T')  # <T>
    @staticmethod
    def take(this_take: Flow[_take__T], count: int | java.jint | java.lang.Integer, /) -> Flow[_take__T]: ...
    _takeWhile__T = typing.TypeVar('_takeWhile__T')  # <T>
    @staticmethod
    def takeWhile(this_takeWhile: Flow[_takeWhile__T], predicate: kotlin.jvm.functions.Function2[_takeWhile__T, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_takeWhile__T]: ...
    _toCollection__C = typing.TypeVar('_toCollection__C')  # <C>
    @staticmethod
    def toCollection(this_toCollection: Flow[java.lang.Object], destination: _toCollection__C, completion: kotlin.coroutines.Continuation[_toCollection__C], /) -> java.lang.Object: ...
    _toList__T = typing.TypeVar('_toList__T')  # <T>
    @staticmethod
    def toList(this_toList: Flow[_toList__T], destination: java.util.List[_toList__T], completion: kotlin.coroutines.Continuation[java.util.List[_toList__T]], /) -> java.lang.Object: ...
    _toSet__T = typing.TypeVar('_toSet__T')  # <T>
    @staticmethod
    def toSet(this_toSet: Flow[_toSet__T], destination: java.util.Set[_toSet__T], completion: kotlin.coroutines.Continuation[java.util.Set[_toSet__T]], /) -> java.lang.Object: ...
    _transform__T = typing.TypeVar('_transform__T')  # <T>
    _transform__R = typing.TypeVar('_transform__R')  # <R>
    @staticmethod
    def transform(this_transform: Flow[_transform__T], transform: kotlin.jvm.functions.Function3[FlowCollector[_transform__R], _transform__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_transform__R]: ...
    _transformLatest__T = typing.TypeVar('_transformLatest__T')  # <T>
    _transformLatest__R = typing.TypeVar('_transformLatest__R')  # <R>
    @staticmethod
    def transformLatest(this_transformLatest: Flow[_transformLatest__T], transform: kotlin.jvm.functions.Function3[FlowCollector[_transformLatest__R], _transformLatest__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_transformLatest__R]: ...
    _transformWhile__T = typing.TypeVar('_transformWhile__T')  # <T>
    _transformWhile__R = typing.TypeVar('_transformWhile__R')  # <R>
    @staticmethod
    def transformWhile(this_transformWhile: Flow[_transformWhile__T], transform: kotlin.jvm.functions.Function3[FlowCollector[_transformWhile__R], _transformWhile__T, kotlin.coroutines.Continuation[bool], java.lang.Object], /) -> Flow[_transformWhile__R]: ...
    _unsafeTransform__T = typing.TypeVar('_unsafeTransform__T')  # <T>
    _unsafeTransform__R = typing.TypeVar('_unsafeTransform__R')  # <R>
    @staticmethod
    def unsafeTransform(this_unsafeTransform: Flow[_unsafeTransform__T], transform: kotlin.jvm.functions.Function3[FlowCollector[_unsafeTransform__R], _unsafeTransform__T, kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> Flow[_unsafeTransform__R]: ...
    _withIndex__T = typing.TypeVar('_withIndex__T')  # <T>
    @staticmethod
    def withIndex(this_withIndex: Flow[_withIndex__T], /) -> Flow[kotlin.collections.IndexedValue[_withIndex__T]]: ...
    _zip__T1 = typing.TypeVar('_zip__T1')  # <T1>
    _zip__T2 = typing.TypeVar('_zip__T2')  # <T2>
    _zip__R = typing.TypeVar('_zip__R')  # <R>
    @staticmethod
    def zip(this_zip: Flow[_zip__T1], other: Flow[_zip__T2], transform: kotlin.jvm.functions.Function3[_zip__T1, _zip__T2, kotlin.coroutines.Continuation[_zip__R], java.lang.Object], /) -> Flow[_zip__R]: ...

class LintKt(java.lang.Object):
    _conflate__T = typing.TypeVar('_conflate__T')  # <T>
    @staticmethod
    def conflate(this_conflate: StateFlow[_conflate__T], /) -> Flow[_conflate__T]: ...
    _distinctUntilChanged__T = typing.TypeVar('_distinctUntilChanged__T')  # <T>
    @staticmethod
    def distinctUntilChanged(this_distinctUntilChanged: StateFlow[_distinctUntilChanged__T], /) -> Flow[_distinctUntilChanged__T]: ...
    _flowOn__T = typing.TypeVar('_flowOn__T')  # <T>
    @staticmethod
    def flowOn(this_flowOn: StateFlow[_flowOn__T], context: kotlin.coroutines.CoroutineContext, /) -> Flow[_flowOn__T]: ...

_MutableStateFlow__T = typing.TypeVar('_MutableStateFlow__T')  # <T>
class MutableStateFlow(StateFlow[_MutableStateFlow__T], typing.Generic[_MutableStateFlow__T]):
    def getValue(self) -> _MutableStateFlow__T: ...
    def setValue(self, arg1: _MutableStateFlow__T, /) -> None: ...

_SafeFlow__T = typing.TypeVar('_SafeFlow__T')  # <T>
class SafeFlow(AbstractFlow[_SafeFlow__T], typing.Generic[_SafeFlow__T]):
    def __init__(self, block: kotlin.jvm.functions.Function2[FlowCollector[_SafeFlow__T], kotlin.coroutines.Continuation[kotlin.Unit], java.lang.Object], /) -> None: ...
    def collectSafely(self, collector: FlowCollector[_SafeFlow__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...

_StateFlow__T = typing.TypeVar('_StateFlow__T')  # <T>
class StateFlow(Flow[_StateFlow__T], typing.Generic[_StateFlow__T]):
    def getValue(self) -> _StateFlow__T: ...

_StateFlowImpl__T = typing.TypeVar('_StateFlowImpl__T')  # <T>
class StateFlowImpl(MutableStateFlow[_StateFlowImpl__T], kotlinx.coroutines.flow.internal.FusibleFlow[_StateFlowImpl__T], typing.Generic[_StateFlowImpl__T]):
    def __init__(self, initialValue: java.lang.Object | int | bool | float | str, /) -> None: ...
    def collect(self, collector: FlowCollector[_StateFlowImpl__T], completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def fuse(self, context: kotlin.coroutines.CoroutineContext, capacity: int | java.jint | java.lang.Integer, /) -> kotlinx.coroutines.flow.internal.FusibleFlow[_StateFlowImpl__T]: ...
    def getValue(self) -> _StateFlowImpl__T: ...
    def setValue(self, value: _StateFlowImpl__T, /) -> None: ...

class StateFlowKt(java.lang.Object):
    _MutableStateFlow__T = typing.TypeVar('_MutableStateFlow__T')  # <T>
    @staticmethod
    def MutableStateFlow(value: _MutableStateFlow__T, /) -> MutableStateFlow[_MutableStateFlow__T]: ...

class StateFlowSlot(java.lang.Object):
    def __init__(self) -> None: ...
    def allocate(self) -> bool: ...
    def awaitPending(self, completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
    def free(self) -> None: ...
    def makePending(self) -> None: ...
    def takePending(self) -> bool: ...

class ThrowingCollector(FlowCollector[java.lang.Object]):
    def __init__(self, e: java.lang.Throwable, /) -> None: ...
    def emit(self, value: java.lang.Object | int | bool | float | str, completion: kotlin.coroutines.Continuation[kotlin.Unit], /) -> java.lang.Object: ...
