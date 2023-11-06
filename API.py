import datetime
import aiohttp
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import asyncio

from selenium_logic import central


def check_free(data, browser):
    for item in data:
        if item["free"] == True:
            print("i                             GET                                   FREE")
        else:
            print(item["free"], datetime.datetime.now())
            # index = data.index(item)
            # xpath = f'//*[@id="lyt_slot_clone_{str(index+1)}"]'
            # slot = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
            #
            # create_btn_xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div"
            # create_btn = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, create_btn_xpath)))
            # create_btn.click()
            #
            # create_btn_xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span"
            # create_btn = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, create_btn_xpath)))
            # create_btn.click()


async def fetch_data(url, browser):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                # check_free(data, browser)
                for item in data:
                    if item["free"] == True:
                        print("i                             GET                                   FREE")
            print(datetime.datetime.now())



async def main():
    # List of URLs you want to request data from
    urls = ["https://srv-go.ru/slots/e5bfbfd0-06b9-47c0-9e90-17255495a6ce/20231106/list.json"] * 1000

    # Create tasks for fetching data from each URL with a 0.5-second delay
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_data(url, browser=browser))
        tasks.append(task)
        await asyncio.sleep(0.25)


    # Execute the tasks concurrently
    results = await asyncio.gather(*tasks)

    # Process the results
    # for url, result in zip(urls, results):
    #     if result is not None:
    #         # print(datetime.datetime.now())
    #         print(f"Data from {url}: {result}")
    #     else:
    #         print(f"Request to {url} failed")


if __name__ == "__main__":
    browser = central()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())



