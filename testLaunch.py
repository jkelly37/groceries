import time
from selenium import webdriver
driver = webdriver.Chrome("/Users/jackkelly/PycharmProjects/appiumTest/chromedriver")
driver.get("https://www.kingsoopers.com/scheduling?fulfillmentType=CurbSide")
emailText= driver.find_element_by_xpath('//*[@id="SignIn-emailInput"]')
emailText.send_keys("liam.propst@gmail.com")
passText = driver.find_element_by_xpath('//*[@id="SignIn-passwordInput"]')
passText.send_keys("Liam123321")
signInButton= driver.find_element_by_xpath('//*[@id="SignIn-submitButton"]')
signInButton.click()
time.sleep(5)
date= driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[3]/div/form/div[1]/label/select/option[3]')
date.click()
print("we got here boys")
