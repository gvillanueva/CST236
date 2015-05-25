from behave import *
from source.speed_researcher import SpeedResearcher

@given('the city of \'Eugene\'')
def step_impl(context):
    context.city = 'Eugene'

@given('the city of \'Salem\'')
def step_impl(context):
    context.city = 'Salem'

@given('the city of 1.948')
def step_impl(context):
    context.city = 1.948

@given('a distance of 111 mi')
def step_impl(context):
    context.distance = 111

@when('\'Eugene\' does not already exist')
def step_impl(context):
    context.system = SpeedResearcher()
    oldDistance = context.system.distance
    context.system.setCity(context.city)

    # Assert that the distance hasn't changed. If it has, then Eugene already exists
    assert(context.system.distance == oldDistance)

@when('\'Salem\' already exists')
def step_impl(context):
    context.system = SpeedResearcher()
    oldDistance = context.system.distance
    context.system.setCity(context.city)

    # Assert that the distance has changed. If it hasn't, then Salem doesn't exist
    assert(context.system.distance != oldDistance)

@when('a new city is created for \'Salem\'')
def step_impl(context):
    context.rValue = context.system.addCity(context.city, context.distance)

@when('a new city is created for \'Eugene\'')
def step_impl(context):
    context.system.addCity(context.city, context.distance)

@when('adding a city for 1.948')
def step_impl(context):
    context.system = SpeedResearcher()
    context.rValue = context.system.addCity(context.city, context.distance)

@then('a city is added for \'Eugene\'')
def step_impl(context):
    context.system.setCity(context.city)
    assert(context.system.distance == context.distance)

@then('False is returned')
def step_impl(context):
    assert(context.rValue == False)

@then('no city is added')
def step_impl(context):
    oldDistance = context.system.distance
    context.system.setCity(context.city)

    # Assert that the distance has changed.
    assert(context.system.distance == oldDistance)

@then('the new city is added to the city file')
def step_impl(context):
    assert(context.city in context.system.cities)