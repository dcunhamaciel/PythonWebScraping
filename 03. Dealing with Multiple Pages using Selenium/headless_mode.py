from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas
import time

options = Options()
options.headless = True
options.add_argument('window-size=1920x1080')

website = 'https://www.audible.com/search'
path = 'D:\Instalacoes\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(path, options=options)
driver.get(website)
#driver.maximize_window()

banner = driver.find_element_by_id('notification-banner-message')
link = banner.find_element_by_xpath('./span/a')

link.click()

time.sleep(5)

container = driver.find_element_by_class_name('adbl-impression-container')
products = container.find_elements_by_xpath('.//li[contains(@class, "productListItem")]')

book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element_by_xpath('.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element_by_xpath('.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element_by_xpath('.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

frame_books = pandas.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length
})
frame_books.to_csv('books.csv', index=False)
