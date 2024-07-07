from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.image_utils import save_screenshot, match_template


def find_and_click(
    driver: WebDriver, template_path: str, scr_name: str, threshold: float = 0.3
) -> bool:
    screenshot = driver.get_screenshot_as_png()
    save_screenshot(screenshot, scr_name)

    if match_result := match_template(screenshot, template_path, threshold):
        click_x, click_y = match_result
        driver.tap([(click_x, click_y)])
        return True
    return False


def wait_and_click(driver: WebDriver, xpath: str, timeout: int = 10) -> None:
    element = WebDriverWait(driver, timeout).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )
    element.click()
    WebDriverWait(driver, timeout).until(
        EC.invisibility_of_element_located((By.XPATH, xpath))
    )
