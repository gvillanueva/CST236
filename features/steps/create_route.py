from behave import *
from source.speed_researcher import SpeedResearcher

@given(u'an instantiated research system')
def step_impl(context):
    context.system = SpeedResearcher()

@given(u'a route of 4 cities')
def step_impl(context):
    context.route = ['Portland', 'Sherwood', 'Woodburn', 'Salem']

@given(u'all cities in the route exist')
def step_impl(context):
    for city in context.route:
        assert(city in context.system.cities)

@given(u'no adjacent elements are the same city')
def step_impl(context):
    for x in xrange(0, len(context.route) - 1):
        assert(context.route[x] != context.route[x+1])

@given(u'a route of 11 cities')
def step_impl(context):
    context.route = ['Portland', 'Sherwood', 'Woodburn', 'Canby', 'Portland', 'Sherwood', 'Woodburn', 'Canby', 'Portland', 'Sherwood', 'Woodburn']

@given(u'a route of no cities')
def step_impl(context):
    context.route = []

@given(u'a route of 3 cities, containing an unknown city')
def step_impl(context):
    context.route = ['Portland', None, 'Sherwood']

@given(u'a route of 2 of the same cities')
def step_impl(context):
    context.route = ['Salem', 'Salem']

@when(u'requesting the system to use our route')
def step_impl(context):
    context.rValue = context.system.setRoute(context.route)

@then(u'True is returned')
def step_impl(context):
    context.rValue = True
