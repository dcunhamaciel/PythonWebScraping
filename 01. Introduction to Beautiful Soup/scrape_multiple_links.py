from bs4 import BeautifulSoup
import requests
import time

website = 'https://subslikescript.com'
website_movies = f'{website}/movies'
result = requests.get(website_movies)
content = result.text

soup = BeautifulSoup(content, 'html.parser')

box = soup.find('article', class_='main-article')

links = []
for link in box.find_all('a', href=True):
    links.append(link['href'])

for link in links:
    website_movie = f'{website}{link}'

    result = requests.get(website_movie)
    content = result.text

    soup = BeautifulSoup(content, 'html.parser')

    box = soup.find('article', class_='main-article')

    title = box.find('h1').get_text()
    transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

    with open(f'{title}.txt', 'w')  as file:
        try:
            file.write(transcript)
        except:
            file.write('Erro!')

    time.sleep(1)
