import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import user

#s = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome()
link = 'https://uygulama.parasut.com/324616/hizmet-ve-urunler'
driver.get(link)
username = user.username
password = user.password

driver.find_element(By.ID, "user_email").send_keys(username)
driver.find_element(By.ID, "user_password").send_keys(password)

driver.find_element(By.NAME, "commit").click()
time.sleep(3)
for j in range(1,31):
    #DÖNGÜ
    print(j)
    driver.get(f'https://uygulama.parasut.com/324616/hizmet-ve-urunler?sayfa={j-1}')
    time.sleep(3)
    for i in range(1, 14):
        iframe = driver.find_element(By.XPATH, "//html//body//div[2]//iframe")
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, f"//html//body//div[3]//main//div[2]//div[2]//div[2]//table//div[{i}]").click()
        #DELAY
        time.sleep(1)
        #DÜZENLE BUTTON
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[3]//a").click()
        #DELAY
        time.sleep(3)
        #KDV OPTION
        #element = WebDriverWait(driver, 10).until(
         #   EC.presence_of_element_located((By.XPATH, "//*[last()]"))
        #)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").click()
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_UP)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ARROW_DOWN)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[2]//div[2]//fieldset//div[1]//div[1]//div[1]//div[1]//div[1]").send_keys(Keys.ENTER)
        time.sleep(1)
        driver.find_element(By.XPATH, "//html//body//div[3]//main//div[3]//div[1]//div[1]//div[1]//div[1]//fieldset//div[1]//div[2]//div[1]//button[1]").click()
        # DELAY
        time.sleep(2)
        driver.get(f'https://uygulama.parasut.com/324616/hizmet-ve-urunler?sayfa={j-1}')
        #DELAY
        time.sleep(2)
    #New Page
    iframe = driver.find_element(By.XPATH, "//html//body//div[2]//iframe")
    driver.switch_to.frame(iframe)
    driver.find_element(By.XPATH, "//html//body//div[3]//main//div[2]//div[2]//div[3]//ul//li[last()]//a").click()
    driver.switch_to.default_content()
    time.sleep(2)




