from playwright.async_api import async_playwright

async def reuse_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)

        # Load session file
        context = await browser.new_context(storage_state="session.json")

        page = await context.new_page()
        await page.goto("https://practice.expandtesting.com/secure")

        # Now you are already logged in!
        await page.screenshot(path="output/secure_page.png")

        await browser.close()

# Run this
import asyncio
asyncio.run(reuse_session())
