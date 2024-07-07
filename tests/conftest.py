import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="module")
def driver():
    capabilities = dict(
        platformName=os.getenv("PLATFORM_NAME"),
        automationName=os.getenv("AUTOMATION_NAME"),
        deviceName=os.getenv("DEVICE_NAME"),
        appPackage=os.getenv("APP_PACKAGE"),
        appActivity=os.getenv("APP_ACTIVITY"),
        language=os.getenv("LANGUAGE"),
        locale=os.getenv("LOCALE"),
    )

    capabilities_options = UiAutomator2Options().load_capabilities(capabilities)
    driver = webdriver.Remote(os.getenv("REMOTE_URL"), options=capabilities_options)

    yield driver
    driver.quit()
