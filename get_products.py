from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from time import sleep
options = Options()
options.add_argument('--headless')
options.add_argument("--disable-notifications")
url = open('url.txt').read().splitlines()
products=open('products.csv','a')
# products.write('name,price,img,link')

def convert_price(msg):
	new_msg=msg.split('฿')
	price = new_msg[1].split(',')
	new_price=''
	for i in price:
		new_price+=i
	return new_price

for k in range(707,len(url)):
	driver = webdriver.Chrome(chrome_options=options)
	driver.maximize_window()
	driver.get(url[k])
	# print(url[k])
	print(f'index:{k}')
	driver.implicitly_wait(30)
	sleep(1)
	number_pages = len(driver.find_elements_by_xpath("//ul[@class='paginationWrap']/li"))
	if number_pages<=0:
		driver.quit()
		continue
	last_page=int(driver.find_element_by_xpath(f"//ul[@class='paginationWrap']/li[{number_pages-1}]").text)
	for j in range(last_page):
		items = len(driver.find_elements_by_xpath(f"//*[@id='layout']/div[5]/div/div[3]/div[1]/div[1]/div[2]/div"))
		print(f"page:{j+1}")
		for i in range(items):
			name_temp = driver.find_element_by_xpath(f"//*[@id='layout']/div[5]/div/div[3]/div[1]/div[1]/div[2]/div[{i+1}]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]/h4[1]").text
			name=''
			for l in name_temp:
				if l==',':
					name+=' '
				else:
					name+=l
			link = driver.find_element_by_xpath(f"//*[@id='layout']/div[5]/div/div[3]/div[1]/div[1]/div[2]/div[{i+1}]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/a[1]").get_attribute('href')
			price_temp = driver.find_element_by_xpath(f"//*[@id='layout']/div[5]/div/div[3]/div[1]/div[1]/div[2]/div[{i+1}]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]").text
			# print(price_temp)
			try:
				img = driver.find_element_by_xpath(f"//*[@id='layout']/div[5]/div/div[3]/div[1]/div[1]/div[2]/div[{i+1}]/div/div/div/div[1]/div/div[1]/a/span/img").get_attribute('src')
				price = convert_price(price_temp)
				products.write(f'{name},{price},{img},{link}\n')
			except:
				pass
		print(f'got {items} items')
		
		if j+1!=last_page:
			try:
				print('go to next page')
				driver.find_element_by_xpath(f"//li[@class='nextArrow']").click()
			except:
				try:
					print('pop up is opened')
					driver.find_element_by_xpath(f"//a[@id='ematic_closeExitIntentOverlay_3_x_1']").click()
				except:
					driver.quit()
					break
				
		driver.implicitly_wait(30)
		sleep(1)		
	driver.quit()
