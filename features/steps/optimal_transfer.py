from behave import *
from source.speed_researcher import SpeedResearcher

@given('the city of Salem')
def step_impl(context):
    context.city = 'Salem'

@given('a speed of 100 MBps')
def step_impl(context):
    context.net_speed = 100

@given('a speed of 1 MBps')
def step_impl(context):
    context.net_speed = 1

@given('a hard drive size of 10 MB')
def step_impl(context):
    context.hdd_size = 10

@given('a hard drive size of 10000 MB')
def step_impl(context):
    context.hdd_size = 10000

@given('a hard drive size of 2400 MB')
def step_impl(context):
    context.hdd_size = 2400

@when('compare is requested')
def step_impl(context):
    context.system = SpeedResearcher()
    context.system.city = context.city
    context.system.net_speed = context.net_speed
    context.system.hdd_size = context.hdd_size

@when('network is faster')
def step_impl(context):
    # We assume speed and speed units to be 60 MPH, or 1/60 miles per second
    assert context.system.net_speed > context.system.hdd_size * (context.system.distance / 216000)

@when('driving is faster')
def step_impl(context):
    assert context.system.net_speed < context.system.hdd_size * (context.system.distance / 216000)

@when('methods are equal')
def step_impl(context):
    assert context.system.net_speed == context.system.hdd_size * (context.system.distance / 216000)

@then('return -1')
def step_impl(context):
    assert context.system.compare() == -1

@then('return 1')
def step_impl(context):
    assert context.system.compare() == 1

@then('return 0')
def step_impl(context):
        assert context.system.compare() == 0
