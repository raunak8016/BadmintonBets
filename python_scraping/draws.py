from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import pandas as pd

# initialize the webdriver
driver = webdriver.Chrome()

# navigate to the webpage with the tournament bracket
driver.get("https://bwf.tournamentsoftware.com/sport/tournament/draw?id=4310C928-4346-43FA-A82B-63F58544A4EA&draw=5")

name = driver.find_element(By.XPATH, '/html/body/form/div[3]/header/div[1]/div/div/div[2]/h2/span/span').text
start_date = driver.find_element(By.XPATH, '/html/body/form/div[3]/header/div[1]/div/div/div[2]/small[2]/span/span/time[1]').text

newpath = r'C:\Users\rauna\Python - Badminton Bets\tournament_data\{0}'.format(name) 
if not os.path.exists(newpath):
    os.makedirs(newpath)

tourn_info = pd.DataFrame({'Tournament Name', 'Start Date', 'Players', 'Seed'})

# locate the tournament bracket table
bracket_table = driver.find_element(By.XPATH, "//table//tbody")

one = []
two = [[]]
three = [[]]
four = [[]]
five = [[]]
six = [[]]
seven = [[]]

seeds = {}

# iterate over the rows in the table
for row in bracket_table.find_elements(By.TAG_NAME, 'tr'):
    index = 0
    for cell in row.find_elements(By.TAG_NAME, 'td'):
        if index < 1:
            index += 1
            continue
        # if the cell is empty, skip it
        if cell.text == '' or cell.text == ' ' or cell.text == '  ':
            index += 1
            continue
        # if the cell contains a match, add it to the list of matches
        elif cell.text.__contains__('21'):
            score = cell.text.strip()

            if index == 2:
                two[len(two)-1].append(score)
            elif index == 3:
                three[len(three)-1].append(score)
            elif index == 4:
                four[len(four)-1].append(score)
            elif index == 5:
                five[len(five)-1].append(score)
            elif index == 6:
                six[len(six)-1].append(score)
            elif index == 7:
                seven[len(seven)-1].append(score)
            index += 1
        else:
            name = cell.text.strip()
            if name.__contains__(' ['):
                arr = name.split(' [')
                name = arr[0].strip()
                seed = arr[1].replace(']', '').strip()
                if seed.isdigit():
                    seeds[name] = int(seed)
            if index == 1:
                one.append(name)
            elif index == 2:
                two.append([name])
            elif index == 3:   
                three.append([name])
            elif index == 4:
                four.append([name])
            elif index == 5:
                five.append([name])
            elif index == 6:
                six.append([name])
            elif index == 7:
                seven.append([name])
            index += 1

# close the webdriver
driver.quit()

print(two)
print(seeds)
