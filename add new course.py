from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time 

webdriver_directory='C:/Program Files (x86)/chromedriver.exe'
# initialize the Chrome driver
driver = webdriver.Chrome(webdriver_directory)
driver.get("https://advising-portal.vercel.app/signin/admin")
driver.maximize_window()

#Authentication
try: 
    driver.find_element(By.ID, "email").send_keys('root@root.com')
    driver.find_element(By.ID, "password").click()
    driver.find_element(By.ID, "password").send_keys('root')
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div[1]/div/button').click()
    
except:
    print("Authentication Error")
    driver.close()
time.sleep(3)

#Go to manage courses
try:
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/button').click()
    driver.find_element(By.XPATH,'/html/body/div[3]/div[2]/div[2]/div/div/div/div[1]').click()

    print('Manage Course Page Found')
except:
    print("Manage Course Page not Found")
    driver.close()


driver.find_element(By.XPATH,'').click()

# #Delete A course
# try:
#     driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div[2]/div/table/tbody/tr[1]/td[8]/div/button[2]').click()
#     print('Course Deleted')
# except:
#     print("Can't delete course")

# #Add A new course
# try:
#     time.sleep(3)
#     driver.find_element(By.ID, "code").send_keys('CHE109')
#     driver.find_element(By.ID, "title").send_keys('Engineering Chemistry')
#     driver.find_element(By.ID, "maxSeat").send_keys('40')
#     driver.find_element(By.ID, "takenSeat").send_keys('0')
#     driver.find_element(By.ID, "creditReq").send_keys('25')
#     driver.find_element(By.ID, "section").send_keys('1')
#     driver.find_element(By.ID, "room").send_keys('702')
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[1]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[1]/select/option[2]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[2]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[2]/select/option[5]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[3]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[3]/select/option[5]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[4]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[1]/div[4]/select/option[7]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[1]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[1]/select/option[4]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[2]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[2]/select/option[5]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/label[6]/span[1]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[3]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[3]/select/option[1]').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[4]/select').click()
#     driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div/section/div/div/div[2]/div[4]/select/option[3]').click()
#     print('Course Added')
# except:
#     print("Can't Add course")

