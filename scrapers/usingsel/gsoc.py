from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://summerofcode.withgoogle.com/archive/2023/organizations")

time.sleep(3)
driver.find_element(
    By.XPATH, "/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/div[1]/div[1]/app-search/div/input").send_keys("python")

orgs1 = driver.find_elements(By.CLASS_NAME, "name")

for org in orgs1:
    print(org.text)

time.sleep(5)
driver.quit()
