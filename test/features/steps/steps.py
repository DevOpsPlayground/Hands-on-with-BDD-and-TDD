from assertpy import assert_that
from behave import *

from src.Calculator import Calculator
from src.Operation import Operation


@given(u'I am a user of the Calculator App')
def step_impl(context):
    context.Calculator = Calculator()


@when(u'I enter {expression}')
def step_impl(context, expression):
    op = Operation(expression)
    context.output = context.Calculator.validate(op)


@then(u'The output is {expected}')
def step_impl(context, expected):
    assert_that(str(context.output)).is_equal_to(expected)
