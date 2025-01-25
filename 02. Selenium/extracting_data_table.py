from selenium import webdriver

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'D:\Instalacoes\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements_by_tag_name('tr')

date = []
home_team = []
score = []
away_team = []

for match in matches:
    try:
        date.append(match.find_element_by_xpath('./td[1]').text)
        home_team.append(match.find_element_by_xpath('./td[3]').text)
        score.append(match.find_element_by_xpath('./td[4]').text)
        away_team.append(match.find_element_by_xpath('./td[5]').text)
    except:
        pass
    else:
        print(home_team[-1])

driver.quit()
