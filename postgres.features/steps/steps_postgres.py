# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then
from hamcrest import assert_that, equal_to

@given('we have 2 integer values {a:d} and {b:d}')
def step_impl(context, a, b):
    context.a = a
    context.b = b

@when('call function for a test')
def step_impl(context):
    c = context.conn.cursor()
    c.execute("SELECT test_me(2,3)")
    result = c.fetchone()
    assert_that(5, equal_to(result[0]))

@when('call function for sum them')
def step_impl(context):
    c = context.conn.cursor()
    c.execute("SELECT test_me(%s,%s)", (context.a, context.b))
    result = c.fetchone()
    assert_that(context.a + context.b, equal_to(result[0]))

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
