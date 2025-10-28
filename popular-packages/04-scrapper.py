import requests
from bs4 import BeautifulSoup

url = 'https://stackoverflow.com/questions'
response = requests.get(url)
text = response.text

soup = BeautifulSoup(text, 'html.parser')

questions = soup.select(".s-post-summary")

# accessing a single attribute
# print(questions[0]['data-post-id'])
for question in questions:
    title = question.select_one(".s-post-summary--content-title").get_text()
    user = question.select_one(".s-user-card--link").get_text()
    print(f"{user.strip()} - Titulo: \n{title.strip()}")
