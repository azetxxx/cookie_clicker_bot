from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def runClicker(seconds, cps):
    timeout = time.time() + seconds
    cookie = driver.find_element(By.ID, "cookie")
    while True:
        cookie.click()
        if time.time() > timeout:
            break
    print(f"cps:", cps.text)


def checkStore():
    feat_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    items_list = []

    for count, feat in enumerate(feat_items):
        get_str = feat.text
        feature_name = get_str.split("\n")[0].split(" - ")[0]
        feature_price = get_str.split("\n")[0].split(" - ")[-1]
        feature_price = feature_price.replace(",", "")
        items_list.append({'name': feature_name, 'price': feature_price})
        # print(get_str, end="\n\n")

    return(items_list[:-1])



# ---------- Main Code ---------- #

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

# Get score "clicks per minute"
cps = driver.find_element(By.ID, "cps")


runClicker(5, cps)
print(checkStore())
