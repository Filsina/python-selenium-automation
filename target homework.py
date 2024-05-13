from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')

#open Target website
driver.get('https://www.target.com/')
sleep(5)

#click sign in button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
sleep(5)

# click side sign in
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
sleep(5)


#check SignIn button is shown

actual_text=driver.find_element(By.ID, "login").text
print(actual_text)
sleep(5)
