from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch edge browser')
def launch_browser(context):
    context.driver = webdriver.Edge()
    context.driver.maximize_window()


@when('open amwell home page')
def get_home_page(context):
    context.driver.get("https://patients.amwell.com/")


@then('verify the logo of the home page')
def verifyLogo(context):
    logo = context.driver.find_element(By.XPATH, "//div/a/img[1]").is_displayed()
    assert logo is True


@then('close browser')
def close_browser(context):
    context.driver.close()


@when('click on sign in button')
def click_login(context):
    context.driver.find_element(By.XPATH, '//div/ul[2]//li/a[contains(text(),"LOG IN")]').click()


@then('verify url of the login page')
def verify_url(context):
    url = "https://amwell.com/loginConsumer.htm"
    context.driver.switch_to.window(context.driver.window_handles[1])
    assert context.driver.current_url == url


