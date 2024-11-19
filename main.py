import requests 
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://github.com/brycekrause"

driver = webdriver.Firefox()
driver.get(url)

driver.implicitly_wait(5)

parent = driver.find_element(By.CLASS_NAME, 'js-calendar-graph') 
children = parent.find_elements(By.CSS_SELECTOR, "*")
for child in children:
    if child.tag_name == "tool-tip":
        print(f"{child.get_attribute('for')}: {child.text}")

driver.quit()