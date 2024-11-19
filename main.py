import requests 
from bs4 import BeautifulSoup
from selenium import webdriver 

url = "https://github.com/brycekrause" # Replace 'username' with the GitHub username 
response = requests.get(url) 
html_content = response.text 

soup = BeautifulSoup(html_content, 'html.parser') # Extract the number of repositories 

#element = soup.find('span', {'class': 'ml-2'})
#element = soup.find('td', {'class': 'ContributionCalendar-day'})

parent = soup.find('tbody')
#elements = soup.find_all(class_= 'ContributionCalendar-day')
#attributes = element.attrs

if parent:
    print('parent found')
    children = parent.find_all(class_= 'ContributionCalendar-day')
    for element in children:
        print(element)
#print(attributes)