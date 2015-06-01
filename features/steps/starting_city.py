from behave import *
from source.speed_researcher import SpeedResearcher

@given(u'the starting city of \'Portland\'')
def step_impl(context):
    context.starting_city = 'Portland'

@given(u'the starting city of \'Tacna\'')
def step_impl(context):
    context.starting_city = 'Tacna'

@given(u'the starting city of 1.948')
def step_impl(context):
    context.starting_city = 1.948

@when(u'the system is created')
def step_impl(context):
    context.system = None
    context.exception = None
    try:
        context.system = SpeedResearcher(starting_city=context.starting_city)
    except ValueError, e:
        context.exception = e

@then(u'SpeedResearcher constructor returns SpeedResearcher instance')
def step_impl(context):
    assert(isinstance(context.system, SpeedResearcher))

@then(u'SpeedResearcher constructor raises ValueError')
def step_impl(context):
    assert(isinstance(context.exception, ValueError))

