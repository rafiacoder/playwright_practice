from playwright.sync_api import sync_playwright
import csv
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/", wait_until="domcontentloaded", timeout=10000)
    with open("output/quotes_data.csv", "w",encoding="utf-8") as f:
      writer = csv.writer(f)
      writer.writerow(["quotes","author"])
      try:
        while True:
         quotes = page.locator(".quote")
         quote_count = quotes.count()
         for i in range(quote_count):
           quote_text = quotes.nth(i).locator(".text").inner_text()
           author = quotes.nth(i).locator(".author").inner_text()
           writer.writerow([quote_text, author])
         next_button = page.locator(".next a")
         if next_button.count() > 0 and next_button.is_visible():
            next_button.click()
            page.wait_for_load_state("domcontentloaded")
         else:
           break
      except Exception as e:
       print(f"An error occurred: {e}")
      finally:
         browser.close()