import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


@when('open login page')
def step_impl(context):
    context.driver.get("https://amwell.com/loginConsumer.htm")


@when('enter username "{email}" and password "{pwd}"')
def step_impl(context, email, pwd):
    context.driver.find_element(By.XPATH, "//input[@id='username']").send_keys(email)
    context.driver.find_element(By.XPATH, "//input[@id='password']").send_keys(pwd)


@when('click login button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//button[@id='loginBtn']").click()
    time.sleep(5)


@then('user must successfully log in')
def step_impl(context):
    status = context.driver.find_element(By.XPATH,
                                         "//span[@id='logoutSpan']/a[contains(text(),'Account')]").is_displayed()
    assert status is True


@then('user shouldn\'t successfully log in')
def step_impl(context):
    status = context.driver.find_element(By.XPATH,
                                         "//span[@id='logoutSpan']/a[contains(text(),'Account')]").is_displayed()
    assert status is False
