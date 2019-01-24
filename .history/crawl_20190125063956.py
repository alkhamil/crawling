from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time
import datetime
import os

chrome_options = Options()
chrome_options.add_argument("--window-size=1366x768")
# path location driver
chrome_driver = 'C:/Data/Project/Github/crawling/driver/chromedriver.exe'
browser = webdriver.Chrome(
    chrome_options=chrome_options, executable_path=chrome_driver)

browser.get('https://twitter.com/login')
time.sleep(3)
browser.find_element_by_name(
    'session[username_or_email]').send_keys('alkhamilnaz@gmail.com')
time.sleep(3)
browser.find_element_by_name('session[password]').send_keys('sahabatnoah')
time.sleep(3)
browser.find_element_by_tag_name('button').click()
