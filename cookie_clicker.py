from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cps = driver.find_element(By.ID, "cps")

def runClicker(seconds, cps):
    timeout = time.time() + seconds
    while True:
        cookie = driver.find_element(By.ID, "cookie")
        cookie.click()
        if time.time() > timeout:
            break
    print(f"cps:", cps.text)


runClicker(5, cps)
