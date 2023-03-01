from selenium import webdriver
import datetime
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
today = datetime.date.today()

url = 'https://bwf.tournamentsoftware.com/ranking/category.aspx?id=33436&category=472&C472FOC=&p=1&ps=100'
driver = webdriver.Chrome('./chromedriver.exe')


def getRankings(url):
    driver.get(url)
  #  driver.find_element(By.XPATH, '/html/body/div/div/div/main/form/div[1]/button[1]/span').click()

    #df = pd.DataFrame(columns=['Ranking Week', 'Rank', 'Name', 'Country', 'Points', 'Tournaments', 'Member ID'])
    df = pd.read_csv('rankings.csv')
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/p/div/a').click()
    print("started")
    all_dates = [x for x in driver.find_elements(By.XPATH, '/html/body/form/div[3]/div[3]/p/div/div/ul/li')]
    driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/p/div/a').click()

    print("next")
    for i in range(150, 200):
        chosen_date = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/p/div/a').click()
        choose_new = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/p/div/div/ul/li[{0}]'.format(i)).click()

        set_100 = Select(driver.find_element(By.ID, "_pagesize"))
        set_100.select_by_value('100')

        table = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody')
        rows=table.find_elements(By.TAG_NAME, 'tr')
        count = 1
        for row in rows:
            if count == 1 or count == 2:
                count += 1
                continue
            elif count >= 102:
                break
            ranking_week = row.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/p/div/a/span').text
            ranking = row.find_element(By.CLASS_NAME, 'rank').text
            name_el = row.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[{0}]/td[5]'.format(count))
            name = name_el.find_elements(By.TAG_NAME, 'a')[0].text
            country = row.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[{0}]/td[4]'.format(count)).text
            tourn = row.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[{0}]/td[9]'.format(count)).text
            points = row.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[{0}]/td[8]'.format(count)).text
            member_id = row.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[{0}]/td[7]'.format(count)).text
                    #ranking = row.get_attribute('innerHTML')(By.CLASS_NAME, 'rank').text
            count += 1
            
            new_row = pd.DataFrame([[ranking_week, ranking, name, country, points, tourn, member_id]], columns=['Ranking Week', 'Rank', 'Name', 'Country', 'Points', 'Tournaments', 'Member ID'])
           # print(new_row)
            df = pd.concat([df, new_row], ignore_index=True)

    return df
df = getRankings(url)
df.to_csv('rankings.csv', index=False)
# df = pd.DataFrame(rankings, columns=['Rank', 'Name', 'Country', 'Points', 'Tournaments'])
