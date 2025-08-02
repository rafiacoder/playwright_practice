from playwright.async_api import async_playwright
import asyncio
async def save_login_session():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()

        page = await context.new_page()
        await page.goto("https://practice.expandtesting.com/login")

        await page.fill("#username", "practice")
        await page.fill("#password", "SuperSecretPassword!")
        await page.click("button[type='submit']")

        await page.wait_for_url("**/secure")

        # Save session
        await context.storage_state(path="session.json")
        await browser.close()
asyncio.run(save_login_session())
