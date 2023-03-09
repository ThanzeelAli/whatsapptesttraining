from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome("C:\chromedriver1\chromedriver.exe")
driver.get("https://web.whatsapp.com/")
time.sleep(40)
driver.implicitly_wait(5)
e=driver.find_element(By.XPATH,"//div[@title='Search input textbox']")
e.click()
e.send_keys("mech family")
e.send_keys(Keys.ENTER)
c=driver.find_element(By.XPATH,"//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")
c.click()
c.send_keys("hi guys,how are you")
driver.implicitly_wait(5)
c.send_keys(Keys.ENTER)

#upload function
driver.find_element(By.XPATH,"//span[@data-testid='clip']").click()
driver.implicitly_wait(2)
p=driver.find_element(By.XPATH,"//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
p.click()
file=input("enter the fail path")
driver.implicitly_wait(10)
p.send_keys(file)
p.send_keys(Keys.ENTER)
driver.close()