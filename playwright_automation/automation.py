from playwright.sync_api import sync_playwright
with sync_playwright() as p:
   browser= p.chromium.launch(headless=False)
   context= browser.new_context()
   page= context.new_page()
   page.goto("https://www.python.org/")
   page.locator("[name='q']").fill("loop")
   page.locator("[name='submit']").click()
   page.wait_for_selector(".list-recent-events")
   page.screenshot(path="searchresult.png")
   browser.close()
