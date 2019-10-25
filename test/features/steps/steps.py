from src.calculator import Calculator
from src.operation import Operation
from behave import given, when, then


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
