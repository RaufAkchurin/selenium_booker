import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Set options
# about:config

def logging_by_email(login: str, password: str):
    login_window = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div[3]/div/div/input")))
    login_window.send_keys(login)

    password_window = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[3]/div[3]/div/div/input")))
    password_window.send_keys(password)

    enter = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[5]/div[1]/button/div/span")))
    time.sleep(2)
    enter.click()

option = webdriver.FirefoxOptions()
option.set_preference('dom.webnotifications.disabled', False)
option.set_preference('media.volume_scale', '0.0')

browser = webdriver.Firefox()
browser.get("https://srv-go.ru")

bugristoe = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='lyt_chk_clone_0']")))
bugristoe.click()

login = "joffre@ebyjeans.com"
password = "Fufik_777176"

logging_by_email(login=login, password=password)

#CREATE_REQUEST
from selenium.webdriver.support.select import Select
create_request_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[1]/div[2]/div/div[4]/div[3]/button/div/span")))
time.sleep(1)
create_request_btn.click()

wehicle_choice_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")))
wehicle_choice_btn.click()


SELECT_LOCATOR = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[1]/div/div[2]/div[3]/div/div")))
SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
SELECT_LOCATOR.send_keys(Keys.ARROW_DOWN)
SELECT_LOCATOR.send_keys(Keys.ENTER)

next_page_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")))
next_page_btn.click()


copy_data_btn = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[7]/div/label/span")))
copy_data_btn.click()

next_page_btn2 = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
    "/html/body/div[1]/div/div/div/div[3]/div[2]/div/div[2]/div[2]/div[3]/div[3]/div[1]/div[2]/div[2]/button/div/span")))
next_page_btn2.click()





