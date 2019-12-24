from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
import sys
chrome_option = Options()
driver = webdriver.Chrome()
base_url="https://www.central.co.th/th/shopbybrand"

def setUp():
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(30)

f=open('url.txt','a')
setUp()
brand = len(driver.find_elements_by_xpath("//div[@class='_31Da6']/section")) 
for i in range (brand):
    brands = driver.find_elements_by_xpath(f"//div[@class='_31Da6']/section[{i+1}]/div[1]/div")
    for j in range(len(brands)):
        len_br = driver.find_elements_by_xpath(f"//div[@class='_31Da6']/section[{i+1}]/div[1]/div[{j+1}]/a")
        test=[br.get_attribute('href') for br in len_br]
        for k in test:
            f.write(f'{k}\n')

f.close()
driver.quit()
    