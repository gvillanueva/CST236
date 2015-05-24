from behave import *
from source.speed_researcher import SpeedResearcher

@given('the city of Salem')
def step_impl(context):
    context.city = 'Salem'

@given('a network speed of 100 MBps')
def step_impl(context):
    context.net_speed = 100

@given('a network speed of 1 MBps')
def step_impl(context):
    context.net_speed = 1

@given('a hard drive size of 10 MB')
def step_impl(context):
    context.hdd_size = 10

@given('a hard drive size of 1000000 MB')
def step_impl(context):
    context.hdd_size = 1000000

@given('a hard drive size of 2215.38461538461 MB')
def step_impl(context):
    context.hdd_size = 2215.38461538461

@when('compare is requested')
def step_impl(context):
    context.system = SpeedResearcher()
    context.system.setCity(context.city)
    context.system.net_speed = context.net_speed
    context.system.driving_speed = 65.0# Assume a typical highway speed, since it is not specified
    context.system.hdd_size = context.hdd_size

@when('network is faster')
def step_impl(context):
    assert context.system.calcDrivingMBps() < context.system.net_speed

@when('driving is faster')
def step_impl(context):
    assert context.system.calcDrivingMBps() > context.system.net_speed

@when('methods are equal')
def step_impl(context):
    assert context.system.calcDrivingMBps() == context.system.net_speed

@then('return -1')
def step_impl(context):
    assert context.system.compare() == -1

@then('return 1')
def step_impl(context):
    assert context.system.compare() == 1

@then('return 0')
def step_impl(context):
    assert context.system.compare() == 0
