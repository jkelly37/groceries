import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome("/Users/jackkelly/PycharmProjects/appiumTest/chromedriver")
driver.get("https://www.kingsoopers.com/scheduling?fulfillmentType=CurbSide")
emailText= driver.find_element_by_xpath('//*[@id="SignIn-emailInput"]')
emailText.send_keys("liam.propst@gmail.com")
passText = driver.find_element_by_xpath('//*[@id="SignIn-passwordInput"]')
passText.send_keys("Liam123321")
signInButton= driver.find_element_by_xpath('//*[@id="SignIn-submitButton"]')
signInButton.click()
#driver.implicitly_wait(20)
#time.sleep(20)
#ate= Select(driver.find_element_by_i("Date"))
print(driver.current_url)
while driver.current_url!="https://www.kingsoopers.com/scheduling?fulfillmentType=CurbSide":
    time.sleep(0.1)
print(driver.current_url)
time.sleep(3)
date=driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div[2]/div/div/div/div[1]/div/div[3]/div/form/div[1]/label/select')

for opt in date.find_elements_by_tag_name('option'):
    print("option: ",opt.text)
    if opt.text=="Friday, March 27th":
        print("toooo")
        opt.click()
