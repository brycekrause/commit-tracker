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
data = []
def getMonth(month):
    if month == "January":
        month = 1
    elif month == "February":
        month = 2
    elif month == "March":
        month = 3
    elif month == "April":
        month = 4
    elif month == "May":
        month = 5
    elif month == "June":
        month = 6
    elif month == "July":
        month = 7
    elif month == "August":
        month = 8
    elif month == "September":
        month = 9
    elif month == "October":
        month = 10
    elif month == "November":
        month = 11
    elif month == "December":
        month = 12

    return month

for child in children:
    if child.tag_name == "tool-tip":
        if "No " not in child.text:
            element = child.get_attribute('for').split('-')

            row = element[3]
            col = element[4]

            element_text = child.text.split(' ')

            month = element_text[3]
            month = getMonth(month)

            day = element_text[4].rstrip('th.')
            commits = element_text[0]

            info_dict = {'month': month, 'day': day, 'commits': commits}
            data.append(info_dict)

            print(f"{col}:{row}: {commits} commits on {month}/{day}")

info_dict = {'month': 6, 'day': 7, 'commits': 4}
data.append(info_dict)


data.sort(key=lambda x: (x['month'], x['day']))

for i in data:
    print(i)



driver.quit()