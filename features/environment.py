import os
import logging
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.helpers import take_screenshot
from behave.model_core import Status


logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

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
    # Save trace
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    scenario_name = scenario.name.replace(" ", "_").replace("/", "_")
    trace_filename = f"{timestamp}_{scenario_name}.zip"
    trace_path = os.path.join(context.traces_dir, trace_filename)

    context.context.tracing.stop(path=trace_path)

    logger.info(f"[TRACE] {trace_filename} saved")
    logger.info(f"[STATUS] {scenario.name} => {scenario.status}")

    if scenario.status == Status.failed:
        screenshot_name = f"{timestamp}_{scenario_name}"
        take_screenshot(context.page, name=screenshot_name, folder="reports/failures")

    context.page.close()
    context.context.close()

def after_all(context):
    context.browser.close()
    context.playwright.stop()