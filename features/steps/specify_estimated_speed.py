from behave import *
from source.speed_researcher import SpeedResearcher

@given('a speed between 0 and 200 MPH')
def step_impl(context):
    context.driving_speed = 25.5

@given('a speed greater than 200 MPH')
def step_impl(context):
    context.driving_speed = 100000.01

@given('a speed less than 0 MPH')
def step_impl(context):
    context.driving_speed = -0.01

@given('a speed of \'One hundred MPH\'')
def step_impl(context):
    context.driving_speed = 'One hundred MPH'

@when('setting speed')
def step_impl(context):
    context.system = SpeedResearcher()
    context.system.driving_speed = context.driving_speed

@then('change the speed setting')
def step_impl(context):
    assert context.system.driving_speed == context.driving_speed

@then('do not change the speed setting')
def step_impl(context):
    assert context.system.driving_speed == 0