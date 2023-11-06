import datetime

import aiohttp
import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio


async def click_element_async(driver, element_xpath):
    try:
        element = await driver.wait.until(
            EC.element_to_be_clickable((By.XPATH, element_xpath))
        )
        await element.click()
    except Exception as e:
        print(f"Error clicking element: {e}")


async def check_free(data):
    for item in data:
        if not item["free"]:
            index = data.index(item)
            xpath = f'//*[@id="lyt_slot_clone_{str(index+1)}"]'
            slot = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                await check_free(data)
                print(datetime.datetime.now())
                return data
            else:
                return None


async def main():
    # List of URLs you want to request data from
    urls = ["https://srv-go.ru/slots/e5bfbfd0-06b9-47c0-9e90-17255495a6ce/20231109/list.json"] * 5

    # Create tasks for fetching data from each URL
    tasks = [fetch_data(url) for url in urls]

    # Execute the tasks concurrently
    results = await asyncio.gather(*tasks)

    # Process the results
    for url, result in zip(urls, results):
        if result is not None:
            print(f"Data from {url}: {result}")
        else:
            print(f"Request to {url} failed")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

