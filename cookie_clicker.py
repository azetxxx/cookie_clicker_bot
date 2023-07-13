from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def runClicker(seconds):
    timeout = time.time() + seconds
    cookie = driver.find_element(By.ID, "cookie")
    while True:
        cookie.click()
        if time.time() > timeout:
            break
    cps = getCPS()
    print(f"cps:", cps.text)


def getCurrFeats():
    feat_items = driver.find_elements(By.CSS_SELECTOR, "#store div")
    items_list = []

    for count, feat in enumerate(feat_items):
        get_str = feat.text
        feature_name = get_str.split("\n")[0].split(" - ")[0]
        feature_price = get_str.split("\n")[0].split(" - ")[-1]
        feature_price = feature_price.replace(",", "")
        if feature_price.isnumeric():
            feature_price = int(feature_price)
        items_list.append({'name': feature_name, 'price': feature_price})
        # print(get_str, end="\n\n")

    return(items_list[:-1])


def getCurrentScore():
    cookies_count = driver.find_element(By.ID, "money").text
    cookies_count = cookies_count.replace(",", "")
    return int(cookies_count)


def getCPS():
    cps = driver.find_element(By.ID, "cps")
    return cps


def buyFeature():
    curr_feats = getCurrFeats()
    curr_money = getCurrentScore()
    if any([feat['price'] < curr_money for feat in curr_feats]):
        print("Enough money")
        can_buy = [feat for feat in curr_feats if feat['price'] < curr_money]
        max_name, max_price = "", 0
        for feat in can_buy:
            if feat['price'] > max_price:
                max_name = feat['name']
                max_price = feat['price']
        buy_feat = driver.find_element(By.ID, "buy"+max_name)
        buy_feat.click()


def startBot(interval, total_time):
    for i in range(total_time // interval):
        runClicker(interval)
        buyFeature()

# ---------- Main Code ---------- #

driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")

startBot(5, 300)
