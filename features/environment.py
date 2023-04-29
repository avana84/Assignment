from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
import os

def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """

    # context.browser = webdriver.Safari()
    context.driver = webdriver.Chrome(executable_path="chromedriver")



    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)



def before_scenario(context, scenario):
    browser_init(context, scenario.name)


def before_step(context, step):
    pass


def after_step(context, step):
    pass


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()