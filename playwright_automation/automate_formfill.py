from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/html/html_forms.asp", wait_until="domcontentloaded", timeout=10000)
    page.locator("[name='fname']").first.fill("rafia")
    page.locator("[name='lname']").first.fill("fayyaz")
    submit_button = page.locator("input[type='submit']").first
    submit_button.scroll_into_view_if_needed()
    submit_button.click()
    page.screenshot(path="form_submission.png")
    browser.close()