account_id = 2
login = "oveta95@ymemphisa.com"
password = "Adsmkdjwh341A-"
day = "08.11.2023"

import os
import pickle
import time




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#BROWSER

service = Service(ChromeDriverManager(driver_version="118.0.5993.117").install())
browser = webdriver.Chrome(service=service)
wait = WebDriverWait(browser, 10, poll_frequency=1)


browser.get("https://srv-go.ru")

def load_cookies():
    time.sleep(5)
    print("its cookies bro, im sorry")
    print(browser.get_cookies())
    pickle.dump(browser.get_cookies(), open(os.getcwd() + f"/cookies/{account_id}.pkl", "wb"))



def find_by_xpath(xpath: str):
    return WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath)))

bugristoe = find_by_xpath("//div[@id='lyt_chk_clone_0']")
bugristoe.click()


login_window = find_by_xpath(
    "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[2]/div[3]/div/div/input")
login_window.send_keys(login)

password_window = find_by_xpath(
    "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[3]/div[3]/div/div/input")
password_window.send_keys(password)

enter = find_by_xpath(
    "/html/body/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div[4]/div[2]/div/div/div[5]/div[1]/button/div/span")
enter.click()


load_cookies()

