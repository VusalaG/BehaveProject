from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch edge browser')
def launch_browser(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


@when('open amwell home page')
def get_home_page(context):
    context.driver.get("https://amwell.com/loginConsumer.htm")



@then('verify that logo presence on the page')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//*[@id='navMenu']//a[contains(text(),'Home')]").is_displayed()
    assert logo is True


@then('close browser')
def close_browser(context):
    context.driver.close()
