import time
from typing import Optional

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import UI_ELEMENTS_ROOT
from utils.driver_utils import find_and_click, wait_and_click

STORE_ACTIVITY = ".StoreActivity"
PLAY_BTN_FILENAME = "main_menu_play_btn.png"
MAIN_MENU_SCR_FILENAME = "main_menu_scr.png"
OK_BUTTON_XPATH = "//android.widget.Button[@text='OK']"
GAME_VIEW_CLASS = "android.view.View"


def find_play_button(
    driver, max_attempts: int = 3, threshold: float = 0.3
) -> Optional[bool]:
    play_button_path = UI_ELEMENTS_ROOT / PLAY_BTN_FILENAME
    assert play_button_path.exists(), f"File {play_button_path} not found"

    for _ in range(max_attempts):
        if found := find_and_click(
            driver,
            str(play_button_path),
            scr_name=MAIN_MENU_SCR_FILENAME,
            threshold=threshold,
        ):
            return found
        driver.implicitly_wait(2)
    return None


def test_launch_app(driver):
    assert driver is not None, "Driver is not initialized"
    assert (
        driver.current_activity == STORE_ACTIVITY
    ), "The app did not launch with the main activity"

    try:
        wait_and_click(driver, OK_BUTTON_XPATH, timeout=20)
    except TimeoutError:
        raise AssertionError("TimeoutError: OK button not found")

    assert find_play_button(driver), "Play button not found or not visible"

    game_screen = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, GAME_VIEW_CLASS))
    )
    assert game_screen.is_displayed(), "Game did not load after pressing Play button"

    time.sleep(5)
