import time

from selenium import webdriver
driver = webdriver.Chrome("/Users/jackkelly/PycharmProjects/appiumTest/chromedriver")
driver.implicitly_wait(1)
driver.get("https://www.starbucks.com/account/signin?ReturnUrl=%2F")
time.sleep(0.5)
loginemailText =driver.find_element_by_xpath('//*[@id="username"]')
loginPasswordText =driver.find_element_by_xpath('//*[@id="password"]')

loginemailText.send_keys("jacklaxjk@gmail.com")
time.sleep(0.5)
loginPasswordText.send_keys("Lacrosse22!")

login_button = driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div/div[1]/form/div[6]/div/span/div/button')
login_button.click()
time.sleep(5)
driver.close()

#driver.get("https://www.starbucks.com/menu")
#driver.get("https://www.starbucks.com/menu/product/2123074/iced?parent=%2Fdrinks%2Ficed-teas%2Ficed-green-teas")

#add_to_order_button= driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/span/div/div/button')

#driver.get("https://www.starbucks.com/menu/store-locator")
print("we got here boys")
#store_locator_lookup=driver.find_element_by_name("place")
#store_locator_lookup.send_keys("chanhassen")
#store_like=driver.find_element_by_xpath('//*[@id="content"]/div[2]/section/div[1]/div/article[1]/div/div[2]/button/svg')