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
        element = child.get_attribute('for').split('-')
        
        row = element[3]
        col = element[4]

        element_text = child.text.split(' ')

        month = getMonth(element_text[3])

        if "th." in element_text[4]:
            day = element_text[4].rstrip('th.')
        elif "rd." in element_text[4]:
            day = element_text[4].rstrip('rd.')

        if element_text[0] == "No":
            commits = 0
        else:
            commits = element_text[0]
        info_dict = {'month': int(month), 'day': int(day), 'commits': int(commits)}
        
        print(f"{row}:{col} = {info_dict}")
        data.append(info_dict)

data.sort(key=lambda x: (x['month'], x['day']))
length = len(data)


for i in range(1, length):
    if data[i]['day'] == data[i-1]['day']+1:
        streak += 1
    else:
        streak = 1

print("Current streak: " + str(streak))


driver.quit()