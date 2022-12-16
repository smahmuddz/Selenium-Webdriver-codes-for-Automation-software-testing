from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time 
 
# initialize the Chrome driver
driver = webdriver.Chrome('C:/Program Files (x86)/chromedriver.exe')
driver.get("https://advising-portal.vercel.app/signin")
driver.maximize_window()

#Go to Admin Login Page
try:
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[3]/button[2]").click()
    print('Succesfully redirected to admin login page')
except:
    print("Cannot redirect to admin login page")
    driver.close()
time.sleep(5)

#Authentication
try:
    driver.find_element(By.ID, "email").send_keys("root@root.com")
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys("root")
    print('Authentication Succesful')
except:
    print("Authentication Error")
    driver.close()
time.sleep(5)

