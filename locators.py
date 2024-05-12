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

#logo image  By XPATH
driver.find_element(By.XPATH,"//a[@href='/ref=ap_frn_logo']")
#email field BY ID
driver.find_element(By.ID, 'ap_email')
#continue by XPATH
driver.find_element(By.XPATH,"//input[@aria-labelledby='continue-announce']")
#By XPATH condit of use
driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")
#By XPATH privacy notice
driver.find_element(By.XPATH,"//a[text()='Privacy Notice']")
#shop amaz busss by ID
driver.find_element(By.ID, 'ab-sign-in-ingress-link')
#creat account by ID
driver.find_element(By.ID, 'createAccountSubmit')
#forgot your pass by ID:
driver.find_element(By.ID, 'auth-fpp-link-bottom')
#Other issue by ID:
driver.find_element(By.ID, 'ap-other-signin-issues-link')

