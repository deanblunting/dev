from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

service = Service(executable_path="/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://summerofcode.withgoogle.com/archive/2023/organizations")
time.sleep(3)

search_box = driver.find_element(
    By.XPATH, '/html/body/app-root/app-layout/mat-sidenav-container/mat-sidenav-content[1]/div/div/main/app-organizations/app-orgs-grid/section[2]/div/div[1]/div[1]/app-search/div/input')
search_box.clear()  # Clear any pre-filled text
search_box.send_keys("python")
time.sleep(2)

org_elements = driver.find_elements(By.CLASS_NAME, "name")
org_count = len(org_elements)

for i in range(org_count):
    try:
        org_elements = driver.find_elements(By.CLASS_NAME, "name")
        org = org_elements[i]

        ActionChains(driver).move_to_element(org).click(org).perform()
        time.sleep(3)  # Wait for the organization page to load

        url = driver.find_element(By.CLASS_NAME, "link").text
        print(f"Organization: {org.text}")
        print(f"Link: {url.text}\n")

        driver.back()
        time.sleep(1)
    except Exception as e:
        print(f"Error at organization {i}: {e}")
        continue

driver.quit()
