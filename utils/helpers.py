import os
from playwright.sync_api import expect


def wait_for_visibility(locator, timeout=10000):
    """
    Waits explicitly for a locator to become visible.
    """
    expect(locator).to_be_visible(timeout=timeout)
    
def take_screenshot(page, name="screenshot", folder="reports/failures"):
    """
    Takes a full-page screenshot and saves it under the given folder.
    """
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, f"{name}.png")
    page.screenshot(path=path, full_page=True)

def wait_and_click(locator, timeout=5000):
    locator.wait_for(timeout=timeout)
    locator.click()

def wait_and_fill(locator, text, timeout=5000):
    locator.wait_for(timeout=timeout)
    locator.fill(text)