from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import os
import pandas as pd
import itertools

def write_draw(url):
    # initialize the webdriver
    driver = webdriver.Chrome()
    # navigate to the webpage with the tournament bracket
    driver.get(url)

    name = driver.find_element(By.XPATH, '/html/body/form/div[3]/header/div[1]/div/div/div[2]/h2/span/span').text
    start_date = driver.find_element(By.XPATH, '/html/body/form/div[3]/header/div[1]/div/div/div[2]/small[2]/span/span/time[1]').text

    tournaments_list = pd.read_csv(r'tournament_data\tournaments_list_training.csv')
    tournament = pd.Series({'Name': name, 'Date': start_date})
    tournaments_list = pd.concat([tournaments_list, tournament.to_frame().T], ignore_index=True)
    tournaments_list.to_csv(r'tournament_data\tournaments_list_training.csv', index=False)

    newpath = r'tournament_data\training\{0}'.format(name) 
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

    draw_info_path = newpath + "\draw_info.csv"
    general_info_path = newpath + "\general_info.csv"

    max_length = max(len(x) for x in [one, two, three, four, five, six, seven])


    # Flatten the 2D lists using itertools.chain.from_iterable
    two = list(itertools.chain.from_iterable(two))
    three = list(itertools.chain.from_iterable(three))
    four = list(itertools.chain.from_iterable(four))
    five = list(itertools.chain.from_iterable(five))
    six = list(itertools.chain.from_iterable(six))
    seven = list(itertools.chain.from_iterable(seven))

    # Fill in missing values with NaN using pandas.Series.fillna
    one += [float('nan')] * (max_length - len(one))
    two += [float('nan')] * (max_length - len(two))
    three += [float('nan')] * (max_length - len(three))
    four += [float('nan')] * (max_length - len(four))
    five += [float('nan')] * (max_length - len(five))
    six += [float('nan')] * (max_length - len(six))
    seven += [float('nan')] * (max_length - len(seven))

    # Create the DataFrame with equal length columns
    draw_info = pd.DataFrame({'Round 1': one, 'Round 2': two, 'Quarter Finals': three, 'Semi Finals': four, 'Finals': five, 'Winner': six})
    draw_info.to_csv(draw_info_path, index=False)

    tourn_info = pd.DataFrame({'Tournament Name': name, 'Start Date': start_date, 'Players': seeds.keys, 'Seed': seeds.values}, index=[0])
    tourn_info.to_csv(general_info_path, index=False)

urls = ['https://bwf.tournamentsoftware.com/sport/tournament/draw?id=4310C928-4346-43FA-A82B-63F58544A4EA&draw=5', 
        'https://bwf.tournamentsoftware.com/sport/tournament/draw?id=9C81DC2E-84E0-4A1A-8C20-EFB1B8CB03F2&draw=1',
        'https://bwf.tournamentsoftware.com/sport/tournament/draw?id=4B835D01-8FB0-41D6-B78E-53ED68D9E9A9&draw=2',
        'https://bwf.tournamentsoftware.com/sport/tournament/draw?id=DB34957F-2E70-43B3-A935-8E98EE0EA6BF&draw=2']

for url in urls:
    write_draw(url)
