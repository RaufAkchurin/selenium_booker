# 1) - 2 обучение
# 2 день - 2 часа
# 3 день - 3 часа
# 4 день - 2 часа + 1 + 1 + 1
# 5 день - 1  + 1 + 1


import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


#DATA_FOR_BOOKING
# login = "joffre@ebyjeans.com"
# password = "Fufik_777176"
# day = "04.11.2023"


#ALI_DATA
login = "a21616157@gmail.com"
password = "Salima.Salih0203"
day = "04.11.2023"


def find_by_xpath(xpath: str):
    return WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))


def select_first_in_dropdown(xpath: str):
    btn = find_by_xpath(xpath)
    btn.send_keys(Keys.ARROW_DOWN)
    btn.send_keys(Keys.ARROW_DOWN)
    btn.send_keys(Keys.ENTER)


def logging_by_email(login: str, password: str):
    login_window = find_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div[3]/div/div/input")
    login_window.send_keys(login)

    password_window = find_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[3]/div[3]/div/div/input")
    password_window.send_keys(password)

    enter = find_by_xpath("/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[5]/div[1]/button/div/span")
    time.sleep(2)
    enter.click()


option = webdriver.FirefoxOptions()
option.set_preference('dom.webnotifications.disabled', False)
option.set_preference('media.volume_scale', '0.0')


browser = webdriver.Firefox()
browser.get("https://srv-go.ru")

bugristoe = find_by_xpath("//div[@id='lyt_chk_clone_0']")
bugristoe.click()

logging_by_email(login=login, password=password)

# CREATE_REQUEST_WINDOW

def car_select():
    SELECT_LOCATOR = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
    SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
    SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
    # car_choice = find_by_xpath("/html/body/div[5]/div/div/div/div[1]/div/div/div[273]")
    # car_choice.click()
    SELECT_LOCATOR.send_keys(Keys.ENTER)


def create_request():
    create_request_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[4]/div[3]/button/div/span")
    time.sleep(1)
    create_request_btn.click()

    wehicle_choice_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
    wehicle_choice_btn.click()

    car_select()
    next_page_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
    next_page_btn.click()

    transport_type_btn = select_first_in_dropdown("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[3]/div/div")
    transport_kind_btn = select_first_in_dropdown("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div[3]/div/div")

    copy_data_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[7]/div/label/span")
    copy_data_btn.click()

    next_page_btn2 = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
    next_page_btn2.click()

# DAY_BOOKING_PAGE


def day_choice(day: datetime):
    day_choice_window = find_by_xpath(
        "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/input")
    day_choice_window.send_keys(Keys.CONTROL + 'a')  # Select all text
    day_choice_window.send_keys(Keys.BACK_SPACE)  # Delete the selected text
    day_choice_window.send_keys(day)


def inactive_checker(slot):
    if "slotInactive" in slot.get_attribute("class"):
        slot.click()
        xpath = "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button"
        create_btn = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        create_btn.click()
        return True
    else:
        return False


def search_empty():
    all_slots = []
    for j in range(14):
        print(f"1 loop {j} iteration")
        for i in range(1, 24):
            print(f"2 loop {i} iteration")
            try:
                xpath = f'//*[@id="lyt_slot_clone_{str(i)}"]'
                slot = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                all_slots.append(slot)
                if not inactive_checker(slot):
                    day_choice(day)
                    # print(len(all_slots), datetime.datetime.now())
                    continue
            except:
                break


def slots_booker():
    while True:
        create_request()
        day_choice(day)
        search_empty()


slots_booker()

#TODO: запуск несколько браузеров одновременно
#TODO: надо добавить проверку наличия элемента ввода даты
#TODO: если элемента нету - то запускать блок с созданием новой заявки
#TODO: добавить выбор автомобиля по данным




























