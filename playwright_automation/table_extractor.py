from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://the-internet.herokuapp.com/tables", wait_until="domcontentloaded", timeout=10000)
    page.locator("#table1")
    rows = page.locator("#table1 tr")
    rows_count = rows.count()
    for i in range(rows_count):
        cells = rows.nth(i).locator("td,th")
        cells_count = cells.count()
        rows_data = [cells.nth(j).inner_text() for j in range(cells_count)]
        print(rows_data)

    browser.close()