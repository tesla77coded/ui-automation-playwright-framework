import pytest
from utils.screenshot_helper import take_screenshot


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = item.funcargs.get("page", None)

        if page:
            test_name = item.name
            screenshot_path = take_screenshot(page, test_name)

            trace_path = f"reports/{test_name}_trace.zip"
            page.context.tracing.stop(path=trace_path)

            print(f"\nScreenshot saved: {screenshot_path}")
            print(f"Trace saved: {trace_path}")
