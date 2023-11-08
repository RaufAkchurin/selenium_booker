# # ALI_DATA
# login = "a21616157@gmail.com"
# password = "Salima.Salih0203"
# day = "07.11.2023"

# 1) - 2 обучение
# 2 день - 2 часа
# 3 день - 3 часа
# 4 день - 2 часа + 1 + 1 + 1
# 5 день - 1  + 1 + 1 +2
# 6 день - 3 + 3
# 7 день - 2


import datetime
import time
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def central():
    # ACCOUNT 2
    login = "oveta95@ymemphisa.com"
    password = "Adsmkdjwh341A-"
    day = "08.11.2023"

    def inactive_checker(slot):
        if "slotInactive" in slot.get_attribute("class"):
            slot.click()
            xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button"
            create_btn = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            create_btn.click()
            return True
        else:
            return False

    def find_by_xpath(xpath: str):
        return WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    def select_first_in_dropdown(xpath: str):
        btn = find_by_xpath(xpath)
        btn.send_keys(Keys.ARROW_DOWN)
        btn.send_keys(Keys.ARROW_DOWN)
        btn.send_keys(Keys.ARROW_DOWN)
        btn.send_keys(Keys.ENTER)

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



    option = webdriver.FirefoxOptions()
    option.page_load_strategy = "eager"
    option.set_preference('dom.webnotifications.disabled', False)
    option.set_preference('media.volume_scale', '0.0')
    # option.add_argument("--headless")
    option.add_argument('--enable-gpu')
    option.add_argument('--disable-blink-features=AutomationControlled')
    option.add_argument("--user-agent=Mozilla/5.0 (Linux; Android 13; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36")


    browser = webdriver.Firefox(options=option)
    browser.get("https://srv-go.ru")

    bugristoe = find_by_xpath("//div[@id='lyt_chk_clone_0']")
    bugristoe.click()

    logging_by_email(login=login, password=password)

    # CREATE_REQUEST_WINDOW

    def car_select():
        SELECT_LOCATOR = find_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
        SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
        SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
        SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
        # car_choice = find_by_xpath("/html/body/div[8]/div/div/div/div[1]/div/div/div[274]")
        # car_choice.click()
        SELECT_LOCATOR.send_keys(Keys.ENTER)

    def create_request():
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

        transport_type_btn = select_first_in_dropdown(
            "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[3]/div/div")
        transport_kind_btn = select_first_in_dropdown(
            "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div[3]/div/div")

        copy_data_btn = find_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[7]/div/label/span")
        copy_data_btn.click()

        next_page_btn2 = find_by_xpath(
            "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
        next_page_btn2.click()

    # DAY_BOOKING_PAGE

    def day_choice(day: datetime, first_mutch=False):
        xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/input"
        if first_mutch:
            day_choice_window = find_by_xpath(xpath)
        else:
            day_choice_window = browser.find_element(By.XPATH, xpath)
        day_choice_window.clear()
        day_choice_window.send_keys(day)


    def tupo_vse_knopki():
        for i in range(24):
            xpath = f'//*[@id="lyt_slot_clone_{str(i)}"]'
            try:
                btn = browser.find_element(By.XPATH, xpath)
                btn.click()
            except:
                pass
        print(datetime.datetime.now())

        create_btn_xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button"
        try:
            btn = browser.find_element(By.XPATH, create_btn_xpath)
            # btn = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, create_btn_xpath)))
            btn.click()
        except:
            print("TRY again")

    def slots_booker():
        while True:
            create_request()
            day_choice(day, first_mutch=True)
            for _ in range(250):
                day_choice(day)
                tupo_vse_knopki()

    slots_booker()




# TODO: Добавить подгрузку куки https://www.youtube.com/watch?v=q0pc7nJZchA
# TODO: надо добавить проверку наличия элемента ввода даты
# TODO: если элемента нету - то запускать блок с созданием новой заявки
# TODO: добавить выбор автомобиля по данным


# РАЗВИТИЕ В АВТОМАТИЗАЦИЮ
# TODO: сделать модуль, котоырй  будет регать автомобиль самостоятельно
# TODO: сделать модуль, котоырй  будет заходить с разных аккаунтов, парсить страницу с активными забронированными слотами и ложить в БД ОБЩУЮ
# TODO: подключить к ТГ БОТУ куда надо будет закидывать удостоверение, все данные о машине и инфо о заявке

