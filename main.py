# 1) - 2 обучение
# 2 день - 2 часа
# 3 день - 3 часа
# 4 день - 2 часа + 1

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set options
# about:config


#DATA_FOR_BOOKING
login = "joffre@ebyjeans.com"
password = "Fufik_777176"
day = 5


def find_by_xpath(xpath: str):
    return WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))


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

create_request_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[4]/div[3]/button/div/span")
time.sleep(1)
create_request_btn.click()

wehicle_choice_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
wehicle_choice_btn.click()


SELECT_LOCATOR = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")
SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
SELECT_LOCATOR.send_keys(Keys.ENTER)

next_page_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
next_page_btn.click()

transport_type_btn = select_first_in_dropdown("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[3]/div[3]/div/div")
transport_kind_btn = select_first_in_dropdown("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[5]/div[3]/div/div")


copy_data_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[7]/div/label/span")
copy_data_btn.click()


next_page_btn2 = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")
next_page_btn2.click()

# DAY_BOOKING_PAGE


def day_choice(day: int):
    day_choice_window = find_by_xpath(
        "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[3]/div/div[1]/div/div[1]/div[3]/div/div[1]/div/input")
    day_choice_window.send_keys(day)


day_choice(day)


def inactive_checker(slot):
    if "slotInactive" in slot.get_attribute("class"):
        slot.click()
        create_btn = find_by_xpath("/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button")
        create_btn.click()
        print("slotInactive")
    if "slotDisabled" in slot.get_attribute("class"):
        print("slotDisabled")


def slots_booker():
    while True:
        all_slots = []
        for i in range(1, 24):
            try:
                xpath = f'//*[@id="lyt_slot_clone_{str(i)}"]'
                slot = WebDriverWait(browser, 1).until(EC.element_to_be_clickable((By.XPATH, xpath)))
                all_slots.append(slot)
                inactive_checker(slot)
            except:
                break
        print(len(all_slots))


slots_booker()















# if len(all_slots) > 0:
#     for slot in all_slots:
#         print(slot.get_attribute("id"))

# slot1 = find_by_xpath('//*[@id="lyt_slot_clone_1"]')
# slot2 = find_by_xpath('//*[@id="lyt_slot_clone_2"]')
# slot3 = find_by_xpath('//*[@id="lyt_slot_clone_3"]')
# slot4 = find_by_xpath('//*[@id="lyt_slot_clone_4"]')
# #
# #
# # print(slot1.get_attribute("id"), slot1.get_attribute("class"))
#
# block = find_by_xpath('//*[@id="lyt_slots"]')
# print(block.get_attribute("class"))













