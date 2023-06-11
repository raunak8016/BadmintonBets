import pandas as pd
import numpy as np
from draws_to_matches import draws_into_matches_32
import os

def create_matches_csv():
    path = r'C:\Users\rauna\BadmintonApp\Data_Handling\match_data_train.csv'
    df = pd.DataFrame(columns=['Match Year', 'Match Stage', 'Time Duration', 
    'P1', 'P1 Country', 'P1 Ranking', 'P1 Seed', 
    'P2', 'P2 Country', 'P2 Ranking', 'P2 Seed', 
    'P1 Points First Set', 'P1 Points Second Set', 'P1 Points Third Set',
    'P2 Points First Set', 'P2 Points Second Set', 'P2 Points Third Set',
    'P1 Total Points Won', 'P2 Total Points Won', 'P1 Total Points Lost', 'P2 Total Points Lost',
    'P1 Total Sets Won', 'P2 Total Sets Won', 'P1 Total Game Points', 'P2 Total Game Points',
    'P1 vs P2 Head to Head', 'P2 vs P1 Head to Head',
    'Winner'])
    df.to_csv(path, index=False)

create_new_matches = False
if create_new_matches:
    create_matches_csv()

def insert_match_data():
    match_data_train = pd.read_csv(r'match_data_train.csv')
    all_tournaments = pd.read_csv(r'C:\Users\rauna\BadmintonApp\Data_Handling\tournament_data\tournaments_list_training.csv')
    tourn_names = all_tournaments['Name'].to_numpy()
    tourn_dates = all_tournaments['Date'].to_numpy()
    print(tourn_names)
    for tourn_name in tourn_names:
        path = r'C:\Users\rauna\BadmintonApp\Data_Handling\tournament_data\training\{0}'.format(tourn_name)
        print(path)
        print(all_tournaments.loc[all_tournaments['Name']=='PETRONAS Malaysia Open 2023', 'Date'])
        match_data = draws_into_matches_32(path, all_tournaments.loc[all_tournaments['Name']==tourn_name, 'Date'].values[0])
        pd.concat([match_data_train, match_data], ignore_index=True)
       # match_data_train = pd.concat([match_data_train, match_data], ignore_index=True)
        match_data_train.to_csv(r'match_data_train.csv', index=False)

insert_match_data()






