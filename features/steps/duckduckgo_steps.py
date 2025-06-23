from behave import given, when, then
from pages.duckduckgo_page import DuckDuckGoPage
from utils.helpers import take_screenshot

@given("I open the browser and go to DuckDuckGo")
def step_open_duckduckgo(context):
    context.ddg = DuckDuckGoPage(context.page)
    context.ddg.navigate()

@when('I search for "{query}"')
def step_search_query(context, query):
    context.ddg.search(query)

@then('I should see "{text}" in the results')
def step_verify_result(context, text):
    assert context.ddg.is_result_visible(text)