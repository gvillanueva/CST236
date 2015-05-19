from behave import *
from source.speed_researcher import SpeedResearcher

@given('a speed between 0 and 100,000 MBps')
def step_impl(context):
    context.net_speed = 25.5

@given('a speed greater than 100,000 MBps')
def step_impl(context):
    context.net_speed = 100000.01

@given('a speed less than 0 MBps')
def step_impl(context):
    context.net_speed = -0.01

@given('a speed of \'One hundred MBps\'')
def step_impl(context):
    context.net_speed = 'One hundred MBps'

@when('setting speed')
def step_impl(context):
    context.system = SpeedResearcher()
    context.system.net_speed = context.net_speed

@then('change the speed setting')
def step_impl(context):
    assert context.system.net_speed == context.net_speed

@then('do not change the speed setting')
def step_impl(context):
    assert context.system.net_speed == 0