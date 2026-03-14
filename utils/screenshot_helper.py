import os
from datetime import datetime


def take_screenshot(page, test_name: str):
    os.makedirs("reports/screenshots", exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = f"reports/screenshots/{test_name}_{timestamp}.png"

    page.screenshot(path=file_path)

    return file_path
