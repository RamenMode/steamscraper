# Code to scrape Notre Dame classes from ND Path

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import time
import re


def get_data(request):

    driver.get(request)
    time.sleep(200)
    print(re.sub('[^a-zA-Z`]+', '', request))
    article_floats = driver.find_elements(By.ID, "market_action_popup_itemactions")
    for article in article_floats:
        print(article)
    article_elements = driver.find_element(By.ID, 'searchResultsRows')
    element = article_elements.find_elements(
        By.CLASS_NAME, 'market_table_value')
    count = 1
    for ele in element:
        price_no_fee = ele.find_element(
            By.CLASS_NAME, 'market_listing_price_with_fee')
        try:
            arrayIndexes = []
            price_fee = int(
                ''.join(c for c in price_no_fee.text if c.isdigit()))/1.15
            for i in range(0, len(price_no_fee.text)):
                if not price_no_fee.text[i].isdigit():
                    arrayIndexes.append(i)
            characters = ''.join(c for c in price_no_fee.text if not c.isdigit())
            price_fee = str(price_fee)
            for x in range(0, len(arrayIndexes)):
                price_fee = price_fee[:arrayIndexes[x]] + \
                    characters[x] + price_fee[arrayIndexes[x]:]
        except:
            price_fee = 99999999999
            characters = 99999999999
        print(characters)
        while (price_fee[len(price_fee)-1] != '.'):
            price_fee = price_fee[:len(price_fee)-1]
        price_fee = price_fee[:len(price_fee)-1]
        print("Price: ", price_no_fee.text)
        print("Resale: ", price_fee)
    print("Complete")

chrome_options = Options()
chrome_options.add_extension('~/Downloads/Steam-Inventory-Helper.crx')
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(options = chrome_options, executable_path=DRIVER_PATH)
wait = WebDriverWait(driver, 10)
f = open('./weapons.json')
data = json.load(f)
for weapon in data["weapons"]:
    for link in weapon["links"]:
        get_data(link)
# for weapon in data:

# select = Select(driver.find_element(By.CLASS_NAME, 'market_paging_pagelink'))
# select.select_by_value('202220')
# driver.find_element('id', 'search-button').click()
# driver.find_elements(By.CLASS_NAME, "result result--group-start")
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result__code')))
# listClasses = [my_elem.text for my_elem in driver.find_elements(By.CLASS_NAME, "result__code")]
# json_object = json.dumps(listClasses)
# with open("NotreDameClasses.json", "w") as outfile:
    # outfile.write(json_object)
# driver.get_screenshot_as_file('./Screenshots/classes.png')
# time.sleep(10)
driver.quit

# element1 = element.find_element(By.CLASS_NAME, 'market_listing_price_with_fee').text
# element2 = element.find_element(By.CLASS_NAME, 'market_listing_price market_listing_price_without_fee').text
# print("Price: ", element1)
# print("Resale Value: ", element2)
