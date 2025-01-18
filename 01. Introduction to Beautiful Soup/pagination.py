from bs4 import BeautifulSoup
import requests
import time
import os

website = 'https://subslikescript.com'
website_movies = f'{website}/movies?page='

result = requests.get(website_movies)
content = result.text
soup = BeautifulSoup(content, 'html.parser')

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = int(pages[-2].text)

links = []

for page in range(1, last_page + 1):
    if page > 10:
        break

    if page > 1:
        website_movies_page = f'{website_movies}{page}'
        result = requests.get(website_movies_page)
        content = result.text
        soup = BeautifulSoup(content, 'html.parser')

    box = soup.find('article', class_='main-article')

    links.clear()
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    directory = f'files\\page_{page}'

    if not os.path.exists(directory):
        os.mkdir(directory)

    for link in links:
        website_movie = f'{website}{link}'

        result = requests.get(website_movie)
        content = result.text

        soup = BeautifulSoup(content, 'html.parser')

        box = soup.find('article', class_='main-article')

        title = box.find('h1').get_text()
        transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

        with open(f'{directory}\\{title}.txt', 'w')  as file:
            try:
                file.write(transcript)
            except:
                file.write('Erro!')

        time.sleep(1)
