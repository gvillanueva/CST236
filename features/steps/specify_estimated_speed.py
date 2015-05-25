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

@given('a preset driving speed of \'Porsche\'')
def step_impl(context):
    context.driving_speed = 'Porsche'

@given('a preset driving speed of \'Bus\'')
def step_impl(context):
    context.driving_speed = 'Bus'

@given('a preset driving speed of \'Cement Truck\'')
def step_impl(context):
    context.driving_speed = 'Cement Truck'

@given('a preset driving speed of \'Laden Swallow\'')
def step_impl(context):
    context.driving_speed = 'Laden Swallow'

@when('setting speed')
def step_impl(context):
    context.system = SpeedResearcher()
    context.system.driving_speed = context.driving_speed

@then('change the speed setting')
def step_impl(context):
    assert context.system.driving_speed == context.driving_speed

@then('change the speed to 200')
def step_impl(context):
    assert context.system.driving_speed == 200

@then('change the speed to 65')
def step_impl(context):
    assert context.system.driving_speed == 65

@then('change the speed to 45')
def step_impl(context):
    assert context.system.driving_speed == 45

@then('change the speed to 24')
def step_impl(context):
    assert context.system.driving_speed == 24

@then('do not change the speed setting')
def step_impl(context):
    assert context.system.driving_speed == 0
