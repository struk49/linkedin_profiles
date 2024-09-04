import requests
from bs4 import BeautifulSoup

url = 'https://www.linkedin.com/in/some-profile/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

name = soup.find('h1').text
job_title = soup.find('h2').text

print(f'Name: {name}, Job Title: {job_title}')