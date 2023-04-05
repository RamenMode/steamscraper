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
    
    driver.get("https://steamcommunity.com/market/listings/730/"+request)
    print(re.sub('[^a-zA-Z`]+', '', 'M4A1-S%20%7C%20Hyper%20Beast%20%28Minimal%20Wear%29'))
    article_elements = driver.find_element(By.ID, 'searchResultsRows')
    elements = article_elements.find_elements(By.CLASS_NAME, 'market_table_value')
    count = 1
    for element in elements:
        print("Item: ", count)
        print("Price: ", element.text)
        print("Resale: ")
    #element1 = element.find_element(By.CLASS_NAME, 'market_listing_price_with_fee').text
    #element2 = element.find_element(By.CLASS_NAME, 'market_listing_price market_listing_price_without_fee').text
    #print("Price: ", element1)
    #print("Resale Value: ", element2)
        count = count + 1
    print("Complete")


#options = Options()
#options.headless = True
#options.add_argument("--window-size=1920,1200")
DRIVER_PATH = '/path/to/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
wait = WebDriverWait(driver, 10)
#driver = webdriver.Chrome(options = options, executable_path=DRIVER_PATH)
request = "M4A1-S%20%7C%20Hyper%20Beast%20%28Minimal%20Wear%29"
get_data(request)
#select = Select(driver.find_element(By.CLASS_NAME, 'market_paging_pagelink'))
#select.select_by_value('202220')
#driver.find_element('id', 'search-button').click()
#driver.find_elements(By.CLASS_NAME, "result result--group-start")
#wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'result__code')))
#listClasses = [my_elem.text for my_elem in driver.find_elements(By.CLASS_NAME, "result__code")]
#json_object = json.dumps(listClasses)
#with open("NotreDameClasses.json", "w") as outfile:
    #outfile.write(json_object)
#driver.get_screenshot_as_file('./Screenshots/classes.png')
time.sleep(10)
driver.quit
