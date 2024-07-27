import asyncio
import time

from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://divar.ir/s/iran/car/pride/111?sort=sort_date")
    await page.wait_for_timeout(2000)

    for i in range(36):
        print(i)
        await page.evaluate('''
            (async () => {
                for (let i = 0; i < 50; i++) {
                    window.scrollBy(0, window.innerHeight);
                    await new Promise(resolve => setTimeout(resolve, 200)); // Small delay to allow content to load
                }
            })();
        ''')
        try:
            await page.get_by_role("button", name="آگهی‌های بیشتر").click()
            await page.wait_for_timeout(25)
        except:
            pass

    time.sleep(100)

    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())