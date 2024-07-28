import asyncio
from getUrls import run
from playwright.async_api import async_playwright

def fetch_links(url):
    async def main():
        async with async_playwright() as playwright:
            return await run(playwright,url)
    return asyncio.run(main())

if __name__ == "__main__":
    pass
    # url = "https://divar.ir/s/iran/car/ford"
    # links = fetch_links(url)
    # for link in links:
    #     print(link)
