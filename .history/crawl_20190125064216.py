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
browser.find_element_by_class_name(
    'js-username-field').send_keys('alkhamilnaz@gmail.com')
browser.find_element_by_class_name(
    'js-password-field').send_keys('sahabatnoah')
browser.find_element_by_tag_name('button').click()
