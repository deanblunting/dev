from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://summerofcode.withgoogle.com/archive/2023/organizations/django-software-foundation-8o")

time.sleep(3)

link = driver.find_element(By.CLASS_NAME, "bd")
print("Link for org:", link.text)
time.sleep(5)

driver.quit()
