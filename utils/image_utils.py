from pathlib import Path
from typing import Tuple

import cv2
import numpy as np
from config import SCREENSHOTS_ROOT, UI_ELEMENTS_ROOT


def save_screenshot(screenshot: bytes, filename: str) -> None:
    SCREENSHOTS_ROOT.mkdir(parents=True, exist_ok=True)
    screenshot_path = get_scr_path(filename)
    screenshot_image = cv2.imdecode(
        np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR
    )
    cv2.imwrite(str(screenshot_path), screenshot_image)


def match_template(
    screenshot: bytes, template_path: str, threshold: float = 0.3
) -> Tuple[int, int] | None:
    screenshot_image = cv2.imdecode(
        np.frombuffer(screenshot, np.uint8), cv2.IMREAD_COLOR
    )
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)

    if template is None:
        raise FileNotFoundError(f"Template image not found: {template_path}")

    result = cv2.matchTemplate(screenshot_image, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    if max_val > threshold:
        click_x = max_loc[0] + template.shape[1] // 2
        click_y = max_loc[1] + template.shape[0] // 2
        return click_x, click_y
    return None


def get_scr_path(scr_filename: str) -> Path:
    return SCREENSHOTS_ROOT / scr_filename


def get_ui_element_path(ui_element_filename: str) -> Path:
    return UI_ELEMENTS_ROOT / ui_element_filename
