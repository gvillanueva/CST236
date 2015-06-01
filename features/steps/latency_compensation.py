from behave import *
from source.speed_researcher import SpeedResearcher

@given(u'network latency of 90ms')
def step_impl(context):
    context.network_latency = 90

@given(u'network latency of 0ms')
def step_impl(context):
    context.network_latency = 0

@given(u'network latency of -10ms')
def step_impl(context):
    context.network_latency = -10

@given(u'network latency of 100,000ms')
def step_impl(context):
    context.network_latency = 100000

@given(u'network latency of 100,001ms')
def step_impl(context):
    context.network_latency = 100001

@given(u'network latency of 1.948ms')
def step_impl(context):
    context.network_latency = 1.948

@when(u'network latency is specified as given value')
def step_impl(context):
    context.system = SpeedResearcher()
    context.exception = None
    try:
        context.system.network_latency = context.network_latency
    except ValueError, e:
        context.exception = e

@when(u'old network latency is 10ms')
def step_impl(context):
    context.old_network_latency = 10

@then(u'change network latency to given value')
def step_impl(context):
    assert(context.system.network_latency == context.network_latency)

@then(u'do not change network latency')
def step_impl(context):
    assert(context.system.network_latency != context.network_latency)

@then(u'raise a ValueError')
def step_impl(context):
    assert(isinstance(context.exception, ValueError))