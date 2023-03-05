from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import pandas as pd
import itertools

# initialize the webdriver
driver = webdriver.Chrome()

# navigate to the webpage with the tournament bracket
driver.get("https://bwf.tournamentsoftware.com/sport/tournament/draw?id=A412AEC4-F2E1-4393-94E2-2BD344F220FA&draw=1")

t_name = driver.find_element(By.XPATH, '/html/body/form/div[3]/header/div[1]/div/div/div[2]/h2/span/span').text
start_date = driver.find_element(By.XPATH, '/html/body/form/div[3]/header/div[1]/div/div/div[2]/small[2]/span/span/time[1]').text

tournaments_list = pd.read_csv(r'tournament_data\tournaments_list_testing.csv')
tournament = pd.Series({'Name': t_name, 'Date': start_date})
tournaments_list = pd.concat([tournaments_list, tournament.to_frame().T], ignore_index=True)
tournaments_list.to_csv(r'tournament_data\tournaments_list_testing.csv', index=False)

newpath = r'tournament_data\testing\{0}'.format(t_name) 
if not os.path.exists(newpath):
    os.makedirs(newpath)

tourn_info = pd.DataFrame({'Tournament Name', 'Start Date', 'Players', 'Seed'})

# locate the tournament bracket table
bracket_table = driver.find_element(By.XPATH, "//table//tbody")

one = []

seeds = {}

# iterate over the rows in the table
for row in bracket_table.find_elements(By.TAG_NAME, 'tr'):
    index = 0
    for cell in row.find_elements(By.TAG_NAME, 'td'):
        if index <= 1:
            index += 1
            continue
        # if the cell is empty, skip it
        if cell.text == '' or cell.text == ' ' or cell.text == '  ':
            index += 1
            continue
        else:
            name = cell.text.strip()
            if name.__contains__(' ['):
                arr = name.split(' [')
                name = arr[0].strip()
                seed = arr[1].replace(']', '').strip()
                if seed.isdigit():
                    seeds[name] = int(seed)
            one.append(name)

# close the webdriver
driver.quit()

draw_info_path = newpath + "\draw_info.csv"
general_info_path = newpath + "\general_info.csv"
print(general_info_path)
# Create the DataFrame with equal length columns
draw_info = pd.DataFrame({'Draw': one})
draw_info.to_csv(draw_info_path, index=False)

tourn_info = pd.DataFrame(columns=['Tournament Name', 'Players', 'Seed'])
for entry in seeds.items():
    t_entry = pd.Series({'Tournament Name': t_name, 'Players': entry[0], 'Seed': entry[1]})
    tourn_info = pd.concat([tourn_info, t_entry.to_frame().T], ignore_index=True)
tourn_info.to_csv(general_info_path, index=False)

print(tourn_info)
