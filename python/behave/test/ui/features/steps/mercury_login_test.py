from behave import given, when, then
from selenium import webdriver

from app.ui import page


@given(u'mercury web app is running')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://staging-app.chromeriver.com/login")
    context.login_page = page.LoginPage(context.driver)


@when(u'enter valid username')
def step_impl(context):
    context.login_page.enter_username("ka_normal")


@when(u'enter valid password')
def step_impl(context):
    context.login_page.enter_password("11river11")


@when(u'enter valid company id')
def step_impl(context):
    context.login_page.enter_company_id("www.cfa.com")


@when(u'click login')
def step_impl(context):
    context.login_page.click_login()


@then(u'login should be successful')
def step_impl(context):
    pass
