
from selenium import webdriver
driver = webdriver.Chrome("/Users/jackkelly/PycharmProjects/appiumTest/chromedriver")
driver.get("https://www.kingsoopers.com/signin?redirectUrl=/")
emailText= driver.find_element_by_xpath('//*[@id="SignIn-emailInput"]')
emailText.send_keys("liam.propst@gmail.com")
passText = driver.find_element_by_xpath('//*[@id="SignIn-passwordInput"]')
passText.send_keys("Liam123321")
signInButton= driver.find_element_by_xpath('//*[@id="SignIn-submitButton"]')

#driver.get("https://www.starbucks.com/menu")
#driver.get("https://www.starbucks.com/menu/product/2123074/iced?parent=%2Fdrinks%2Ficed-teas%2Ficed-green-teas")

#add_to_order_button= driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[1]/div/span/div/div/button')

#driver.get("https://www.starbucks.com/menu/store-locator")
print("we got here boys")
#store_locator_lookup=driver.find_element_by_name("place")
#store_locator_lookup.send_keys("chanhassen")
#store_like=driver.find_element_by_xpath('//*[@id="content"]/div[2]/section/div[1]/div/article[1]/div/div[2]/button/svg')