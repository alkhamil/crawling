from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os

chrome_options = Options()
chrome_options.add_argument("--window-size=1366x768")
chrome_driver = 'C:/Data/Project/Aissat_app/driver/chromedriver.exe'
browser = webdriver.Chrome(
    chrome_options=chrome_options, executable_path=chrome_driver)

browser.get('https://twitter.com/')
row = browser.find_elements_by_tag_name('tr')
for rows in row:
    columns = rows.find_elements_by_tag_name('span')
    print(columns[1].get_attribute(
        'innerHTML') + ' - ' + columns[4].get_attribute(
        'innerHTML'))
browser.quit()
