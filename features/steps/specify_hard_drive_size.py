from behave import *
from source.speed_researcher import SpeedResearcher

@given('a hard drive size greater than 0 MB')
def step_impl(context):
    context.hdd_size = 200

@given('a hard drive size less than 0 MB')
def step_impl(context):
    context.hdd_size = -0.01

@given('a hard drive size of \'100 megabytes\'')
def step_impl(context):
    context.hdd_size = '100 megabytes'

@when('setting hard drive size')
def step_impl(context):
    context.system = SpeedResearcher()
    context.system.hdd_size = context.hdd_size

@then('change the hard drive size')
def step_impl(context):
    assert context.system.hdd_size == context.hdd_size

@then('do not change the hard drive size')
def step_impl(context):
    assert context.system.hdd_size == 0