from playwright.sync_api import Page
from utils.helpers import wait_for_visibility

class DuckDuckGoPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator("//input[@id='searchbox_input']")
        self.result_links = page.locator("//a[@data-testid='result-extras-url-link']")

    def navigate(self):
        self.page.goto("https://duckduckgo.com")

    def search(self, query: str):
        self.search_input.fill(query)
        self.search_input.press("Enter")
        wait_for_visibility(self.result_links.first)

    def is_result_visible(self, text: str) -> bool:
        links = self.result_links.all()
        for link in links:
            href = link.get_attribute("href")
            if href and text in href:
                return True
        return False
