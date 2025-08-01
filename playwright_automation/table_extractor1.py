from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.w3schools.com/html/html_tables.asp", wait_until="domcontentloaded", timeout=10000)
    rows=page.locator("#customers tr")
    print(f"Total number of rows in the table: {rows.count()}")
    for i in range(rows.count()):
        cells = rows.nth(i).locator("td, th ")
        row_data = [cells.nth(j).inner_text() for j in range(cells.count())]
        print(row_data)
    browser.close()
    