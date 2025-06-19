import os
from playwright.sync_api import sync_playwright

def before_all(context):
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=False)
    context.traces_dir = "traces"
    os.makedirs(context.traces_dir, exist_ok=True)

def before_scenario(context, scenario):
    context.context = context.browser.new_context()
    context.page = context.context.new_page()
    context.context.tracing.start(
        screenshots=True,
        snapshots=True,
        sources=True,
        title=scenario.name
    )

def after_scenario(context, scenario):
    trace_path = f"{context.traces_dir}/{scenario.name.replace(' ', '_')}.zip"
    context.context.tracing.stop(path=trace_path)
    context.page.close()
    context.context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()
