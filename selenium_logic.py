# # ALI_DATA
# account_id = 1
# login = "a21616157@gmail.com"
# password = "Salima.Salih0203"
# day = "07.11.2023"
from selenium.common import ElementNotInteractableException, TimeoutException, ElementClickInterceptedException

from speed_checker import speed_checker

account_id = 2
login = "oveta95@ymemphisa.com"
password = "Adsmkdjwh341A-"
day = "09.11.2023"

# 1) - 2 обучение
# 2 день - 2 часа
# 3 день - 3 часа
# 4 день - 2 часа + 1 + 1 + 1
# 5 день - 1  + 1 + 1 +2
# 6 день - 3 + 3
# 7 день - 4
# 8 day  -3
# 9 day - 2 + 2

import time
import datetime
import os
import pickle
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def central():
    def find_by_xpath(xpath: str):
        return WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def select_first_in_dropdown(xpath: str):
        btn = find_by_xpath(xpath)
        btn.send_keys(Keys.ARROW_DOWN)
        btn.send_keys(Keys.ARROW_DOWN)
        btn.send_keys(Keys.ARROW_DOWN)
        btn.send_keys(Keys.ENTER)

    def logging_main():
        if os.path.isfile(os.getcwd() + f"/cookies/{account_id}.pkl"):
            try:
                load_cookies()
            except:
                logging_by_email(login=login, password=password)
        else:
            logging_by_email(login=login, password=password)

    def cookies_save():
        time.sleep(5)
        pickle.dump(browser.get_cookies(), open(os.getcwd() + f"/cookies/{account_id}.pkl", "wb"))

    def load_cookies():
        browser.delete_all_cookies()
        cookies = pickle.load(open(os.getcwd() + f"/cookies/{account_id}.pkl", "rb"))
        for cookie in cookies:
            browser.add_cookie(cookie)
        browser.refresh()

    def logging_by_email(login: str, password: str):
        login_window = find_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div[3]/div/div/input")
        login_window.send_keys(login)

        password_window = find_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[3]/div[3]/div/div/input")
        password_window.send_keys(password)

        enter = find_by_xpath(
            "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[5]/div[1]/button/div/span")
        enter.click()
        cookies_save()

    def custom_chrome():
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.117 Safari/537.36"
        options = Options()
        options.add_argument(f"user-agent={user_agent}")

        service = Service(ChromeDriverManager(driver_version="118.0.5993.117").install())
        browser = webdriver.Chrome(service=service, options=options)
        wait = WebDriverWait(browser, 10, poll_frequency=1)

    def custom_firefox():
        option = webdriver.FirefoxOptions()
        option.page_load_strategy = "eager"
        option.set_preference('dom.webnotifications.disabled', False)
        option.set_preference('media.volume_scale', '0.0')
        # option.add_argument("--headless")
        option.add_argument('--enable-gpu')
        # option.add_argument('disable-blink-features=AutomationControlled')
        # option.add_argument("user-agent=Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0")
        browser = webdriver.Firefox(options=option)
        return browser

    def browser_with_options():
        browser = custom_firefox()
        browser.get("https://srv-go.ru")
        time.sleep(10)
        return browser

    browser = browser_with_options()
    bugristoe = find_by_xpath("//div[@id='lyt_chk_clone_0']")
    bugristoe.click()

    logging_by_email(login=login, password=password)
    # CREATE_REQUEST_WINDOW

    def car_select():
        SELECT_LOCATOR = find_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
        SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
        SELECT_LOCATOR.send_keys(Keys.ENTER)

    def create_request():
        try:
            create_request_btn = find_by_xpath(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[4]/div[3]/button/div/span")
            create_request_btn.click()

            wehicle_choice_btn = find_by_xpath(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
            wehicle_choice_btn.click()

            car_select()
            next_page_btn = find_by_xpath(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
            next_page_btn.click()

            select_first_in_dropdown(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[3]/div/div")
            select_first_in_dropdown(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div[3]/div/div")

            copy_data_btn = find_by_xpath(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[7]/div/label/span")
            copy_data_btn.click()

            next_page_btn2 = find_by_xpath(
                "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
            next_page_btn2.click()
        except ElementClickInterceptedException:
            browser.refresh()


    # DAY_BOOKING_PAGE

    def day_choice(day: datetime, first_mutch=False):
        try:
            xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/input"
            day_choice_window = find_by_xpath(xpath)
            day_choice_window.clear()
            day_choice_window.send_keys(day)
        except TimeoutException:
            browser.refresh()
            create_request()

    def tupo_vse_knopki():
        for i in range(24):
            xpath = f'//*[@id="lyt_slot_clone_{str(i)}"]'
            try:
                btn = browser.find_element(By.XPATH, xpath)
                btn.click()
            except:
                pass

        speed_checker(datetime.datetime.now())
        print(datetime.datetime.now())

        #TODO: попробовать такую логику - если нажалась кнопка - то не обновлять дату а дождаться активности
        # кнопки создания и нажать её сразу

        create_btn_xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button"

        try:
            btn = browser.find_element(By.XPATH, create_btn_xpath)
            btn.click()
        except:
            pass

    def slots_booker():
        while True:
            create_request()
            day_choice(day, first_mutch=True)
            for _ in range(250):
                try:
                    day_choice(day)
                    tupo_vse_knopki()
                except ElementNotInteractableException: # Когда машина забронирована, тут падает исключение, тк не может найти поле для ввода даты
                    create_request()
                    day_choice(day, first_mutch=True)

    slots_booker()


#TODO: избавитьсяот ошибок при бронировании
#TODO: автоматизировать создание машин
#TODO: МОдуль для сбора активных заявок



# TODO: надо добавить проверку наличия элемента ввода даты
# TODO: если элемента нету - то запускать блок с созданием новой заявки
# TODO: добавить выбор автомобиля по данным


# РАЗВИТИЕ В АВТОМАТИЗАЦИЮ
# TODO: подключить к ТГ БОТУ куда надо будет закидывать удостоверение, все данные о машине и инфо о заявке
