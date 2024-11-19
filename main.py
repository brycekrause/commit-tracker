import requests 
from selenium.webdriver.common.by import By
from selenium import webdriver

url = "https://github.com/brycekrause"

driver = webdriver.Firefox()
driver.get(url)

driver.implicitly_wait(5)

parent = driver.find_element(By.CLASS_NAME, 'js-calendar-graph') 
children = parent.find_elements(By.CSS_SELECTOR, "*")
streak = 0
for child in children:
    if child.tag_name == "tool-tip":
        if "No " not in child.text:
            element = child.get_attribute('for').split('-')
            row = element[3]
            col = element[4]
            element_text = child.text.split(' ')
            month = element_text[3]
            day = element_text[4].rstrip('th.')
            commits = element_text[0]
            #all = {
            #    {'date': date},
            #    {'row': element[3]},
            #    {'col': element[4]}
            #}
            print(f"{col}:{row}: {commits} commits on {month} {day}th")



driver.quit()