from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas
import time

options = Options()
options.headless = False
#options.add_argument('window-size=1920x1080')

website = 'https://www.audible.com/search'
path = 'D:\Instalacoes\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(path, options=options)
driver.get(website)
driver.maximize_window()

banner = driver.find_element_by_id('notification-banner-message')
link = banner.find_element_by_xpath('./span/a')

link.click()

time.sleep(5)

pagination = driver.find_element_by_xpath('//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements_by_tag_name('li')
last_page = int(pages[-2].text)

current_page = 1

book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    time.sleep(2)

    container = driver.find_element_by_class_name('adbl-impression-container')
    products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

    for product in products:
        book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

    current_page += 1

    try:
        next_page = driver.find_element_by_xpath('//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()

frame_books = pandas.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length
})
frame_books.to_csv('books.csv', index=False)
