import requests 
from bs4 import BeautifulSoup 
url = "https://github.com/brycekrause" # Replace 'username' with the GitHub username 
response = requests.get(url) 
html_content = response.text 

soup = BeautifulSoup(html_content, 'html.parser') # Extract the number of repositories 

repo_count = soup.find('span', {'class': 'Counter'}).text 
print(f"Number of repositories: {repo_count}")