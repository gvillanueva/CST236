from behave import *
from source.speed_researcher import SpeedResearcher

@given(u'HDD speed of 1gb/s')
def step_impl(context):
    context.hdd_speed = 1

@given(u'HDD speed of 1000gb/s')
def step_impl(context):
    context.hdd_speed = 1000

@given(u'HDD speed of 0gb/s')
def step_impl(context):
    context.hdd_speed = 0

@given(u'HDD speed of 1001gb/s')
def step_impl(context):
    context.hdd_speed = 1001

@given(u'HDD speed of 1.948')
def step_impl(context):
    context.hdd_speed = 1.948

@when(u'selecting a hard drive with given speed')
def step_impl(context):
    context.system = SpeedResearcher()
    context.exception = None
    try:
        context.system.hdd_speed = context.hdd_speed
    except ValueError, e:
        context.exception = e

@then(u'set hard drive speed')
def step_impl(context):
    assert(context.system.hdd_speed == context.hdd_speed)

@then(u'raise ValueError')
def step_impl(context):
    assert(isinstance(context.exception, ValueError))