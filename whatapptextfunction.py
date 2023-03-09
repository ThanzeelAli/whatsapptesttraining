from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome("C:\chromedriver1\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(40)
driver.implicitly_wait(5)

#search box function
e=driver.find_element(By.XPATH,"//div[@title='Search input textbox']")
e.click()
e.send_keys("mech family")
e.send_keys(Keys.ENTER)

#message send function
c=driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
c.click()
c.send_keys("hi guys,how are you")
driver.implicitly_wait(5)
c.send_keys(Keys.ENTER)
driver.implicitly_wait(5)
driver.close()