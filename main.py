import asyncio
import logging
import getUrls
import getData
from playwright.async_api import async_playwright
from SQLMangment import create_database, add_record

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def fetch_links(url):
    async def main():
        async with async_playwright() as playwright:
            return await getUrls.run(playwright, url)

    return asyncio.run(main())


def fetch_data(url):
    async def main():
        async with async_playwright() as playwright:
            return await getData.run(playwright, url)

    return asyncio.run(main())


if __name__ == "__main__":
    try:
        with open("carurls.txt", "r") as f:
            for url in f:
                try:
                    # Fetch the list of URLs from the given page URL
                    urlList = fetch_links(url.strip())
                    table_name = url.split("https://divar.ir/s/iran/car/")[1]

                    # Create the database table
                    create_database("divar", table_name)

                    for page_url in urlList:
                        try:
                            # Fetch data from each page URL
                            data = fetch_data("https://divar.ir" + page_url["href"])

                            # Add the fetched data to the database
                            add_record(db_name="divar", table_name=table_name,
                                       brand_type=data["برند و تیپ"], fuel_type=data["نوع سوخت"],
                                       engine_status=data["وضعیت موتور"], front_chassis=data["شاسی جلو"],
                                       rear_chassis=data["شاسی عقب"], body_status=data["وضعیت بدنه"],
                                       insurance_deadline=data["مهلت بیمهٔ شخص ثالث"], gearbox=data["گیربکس"],
                                       base_price=data["قیمت پایه"], mileage=data["کارکرد"],
                                       model_year=data["مدل (سال تولید)"], color=data["رنگ"],
                                       location=data["مکان"], url=page_url["href"])
                        except Exception as e:
                            logging.error(f"Error fetching data for URL {page_url['href']}: {e}")
                except Exception as e:
                    logging.error(f"Error fetching links for URL {url.strip()}: {e}")
    except Exception as e:
        logging.critical(f"Error opening carurls.txt: {e}")
