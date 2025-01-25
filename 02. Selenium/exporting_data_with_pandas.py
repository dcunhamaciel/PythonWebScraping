from selenium import webdriver
import pandas

website = 'https://www.adamchoi.co.uk/overs/detailed'
path = 'D:\Instalacoes\chromedriver-win64\chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get(website)

all_matches_button = driver.find_element_by_xpath('//label[@analytics-event="All matches"]')
all_matches_button.click()

matches = driver.find_elements_by_tag_name('tr')

date_list = []
home_team_list = []
score_list = []
away_team_list = []

for match in matches:
    try:
        date = match.find_element_by_xpath('./td[1]').text
        home_team = match.find_element_by_xpath('./td[3]').text
        score = match.find_element_by_xpath('./td[4]').text
        away_team = match.find_element_by_xpath('./td[5]').text

        date_list.append(date)
        home_team_list.append(home_team)
        score_list.append(score)
        away_team_list.append(away_team)
    except:
        pass
    else:
        print(home_team_list[-1])

driver.quit()

data_frame = pandas.DataFrame({
    'date': date_list,
    'home_team': home_team_list,
    'score': score_list,
    'away_team': away_team_list
})
data_frame.to_csv('football_data.csv', index=False)
