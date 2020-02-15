from behave import given, when, then
from app.calculator import calculator


@given(u'calculate app is running')
def step_impl(context):
    context.c = calculator.Calculator()


@when(u'calling add function to add {x} and {y}')
def step_impl(context, x, y):
    context.result = context.c.addition(int(x), int(y))


@when(u'calling subtraction function to subtract {x} and {y}')
def step_impl(context, x, y):
    context.result = context.c.subtraction(int(x), int(y))


@when(u'calling multiplication function to multiply {x} and {y}')
def step_impl(context, x, y):
    context.result = context.c.multiplication(int(x), int(y))


@when(u'calling division function to divide {x} and {y}')
def step_impl(context, x, y):
    context.result = context.c.division(int(x), int(y))


@then(u'calculate app should return {exp_res}')
def step_impl(context, exp_res):
    assert context.result == int(exp_res)