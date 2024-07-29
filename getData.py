import asyncio
from playwright.async_api import Playwright, async_playwright

async def run(playwright: Playwright, url) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto(url)
    result = { "برند و تیپ":"", "نوع سوخت":"", "وضعیت موتور":"", "شاسی جلو":"", "شاسی عقب":"", "وضعیت بدنه":"", "مهلت بیمهٔ شخص ثالث":"" ,"گیربکس":"", "قیمت پایه":"", "کارکرد":"", "مدل (سال تولید)":"", "رنگ":"", "مکان":""}
    selectors = [
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.kt-page-title > div > div.kt-page-title__subtitle.kt-page-title__subtitle--responsive-sized",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > table",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(3)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(5)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(7)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(9)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(11)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(13)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(15)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(17)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(19)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(21)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(23)",
        "#app > div:nth-child(1) > div > div > main > article > div > div.kt-col-5 > section:nth-child(1) > div.post-page__section--padded > div:nth-child(25)"
    ]

    for i in range(0,len(selectors)):
        try:
            page.set_default_timeout(120)
            element = await page.locator(selectors[i]).inner_text()
            if i == 0:
                result["مکان"] = element.split("در ")[1]
            elif i == 1:
                datalist = element.split("\n")
                for i in range(3):
                    result[datalist[i].replace("\u200c"," ")] = datalist[i+3]
            else:
                datalist = element.split("\n\n")
                if datalist[0].replace("\u200c"," ") == "وضعیت شاسی ها":
                    result["شاسی جلو"] = datalist[1].replace("\u200c"," ")
                    result["شاسی عقب"] = datalist[1].replace("\u200c"," ")
                else:
                    result[datalist[0].replace("\u200c"," ")] = datalist[1].replace("\u200c"," ")
        except:
            pass

    await context.close()
    await browser.close()
    return result

