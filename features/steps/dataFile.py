from behave import *
from source.datafile import DataFile

@given('a path to valid file')
def step_impl(context):
    context.path = 'valid.txt'

@given('a path to invalid file')
def step_impl(context):
    context.path = 'invalid.txt'

@given('a path to missing file')
def step_impl(context):
    context.path = ''

@when('reading the file')
def step_impl(context):
    data = DataFile(context.path)
    context.result = data.read()
    pass

@then('return the parsed data')
def step_impl(context):
    assert context.result is not None

@then('return None')
def step_impl(context):
    assert context.result is None
