import logging
from behave import given, when, then
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@given('I open the browser and go to DuckDuckGo')
def step_open_duckduckgo(context):
    context.page.goto("https://duckduckgo.com")

    try:
        context.page.wait_for_selector("input#searchbox_input", timeout=10000, state="visible")
        logger.info("🔍 DuckDuckGo search box detected.")
    except PlaywrightTimeoutError:
        logger.error("❌ DuckDuckGo search box not found.")
        context.page.screenshot(path="error_no_search_box.png")
        raise

@when('I search for "{term}"')
def step_search_term(context, term):
    try:
        search_box = context.page.query_selector("input#searchbox_input")
        search_box.fill(term)
        search_box.press("Enter")
        logger.info(f"✅ Search for '{term}' submitted.")
        context.search_term = term
    except Exception as e:
        logger.exception("❌ Error while performing the search.")
        context.page.screenshot(path="error_search_fail.png")
        raise

@then('I should see "{expected}" in the results')
def step_verify_result(context, expected):
    try:
        context.page.wait_for_selector("#links", timeout=10000)
        context.page.wait_for_selector(f"a:has-text('{expected}')", timeout=10000)
        logger.info(f"✅ Link containing '{expected}' found in the results.")
    except PlaywrightTimeoutError:
        logger.warning(f"⚠️ Direct match for '{expected}' not found. Trying fallback text...")
        try:
            context.page.wait_for_selector(f"text={expected}", timeout=5000)
            logger.info(f"✅ Fallback: text '{expected}' found in the results.")
        except Exception as e:
            logger.exception("❌ Final fallback failed. No matching result.")
            context.page.screenshot(path="error_no_results.png")
            raise