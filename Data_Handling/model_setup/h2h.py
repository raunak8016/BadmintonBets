from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import datetime as dt

def h2h(p1, p2):
    try:
        driver = webdriver.Chrome()

        # navigate to the webpage with the tournament bracket
        driver.get("https://bwf.tournamentsoftware.com/ranking/headtohead.aspx?id=209B123F-AA87-41A2-BC3E-CB57133E64CC")

        driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[3]/td[2]/input[2]').send_keys(p1)
        driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[3]/td[4]/input[2]').send_keys(p2)

        driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[4]/td/input').click()

        p1_wins = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[5]/td/table[1]/tbody/tr[6]/td[1]').text
        p2_wins = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[5]/td/table[1]/tbody/tr[6]/td[2]').text

        # make changes
        # table = driver.find_element(By.XPATH, '/html/body/form/div[3]/div[3]/table/tbody/tr[5]/td/table[2]/tbody')
        # rows=table.find_elements(By.TAG_NAME, 'tr')

        # for row in rows:
        #     date_str = row.find_element(By.CLASS_NAME, 'plannedtime').text
        #     date_str = date_str[3:]
        #     date_match = dt.datetime.strptime(date_str, ' %m/%d/%Y')
        #     print(date_match)
        #     # if date_match > date:
        #     #     sc = row.find_element(By.TAG_NAME, 'span')
        #     #     sc = sc.find_elements(By.TAG_NAME, 'span')
        #     #     for game in rows:
        #     #         print(game.text)

        # close the webdriver
        driver.quit()
    except:
        p1_wins = 0
        p2_wins = 0
    return [p1_wins, p2_wins]

