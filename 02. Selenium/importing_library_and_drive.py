from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'D:\Instalacoes\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

driver.quit()
