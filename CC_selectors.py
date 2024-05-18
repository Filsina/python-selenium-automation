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


#AMAZON HEADER
driver.find_element(By.CSS_SELECTOR,"a[href*='/ref=ap_frn_logo']")

#create account header
driver.find_element(By.CSS_SELECTOR,"h1[class*='a-spacing-small']")

#your name field
driver.find_element(By.CSS_SELECTOR,"[placeholder='First and last name']")

#enter phone number or email
driver.find_element(By.CSS_SELECTOR, "[name='email']")

#password
driver.find_element(By.CSS_SELECTOR,"input#ap_password")

#password check
driver.find_element(By.CSS_SELECTOR,"input#ap_password_check")

#continue button
driver.find_element(By.CSS_SELECTOR,"input#continue")

#conditions of use
driver.find_element(By.CSS_SELECTOR,"a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie']")

#privacy notice
driver.find_element(By.CSS_SELECTOR,"a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie']")

#Sign in
driver.find_element(By.CSS_SELECTOR,"a[class*='a-link-emphasis']")

