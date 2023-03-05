import pandas as pd
import numpy as np


def create_matches_csv():
    path = r'C:\Users\rauna\BadmintonApp\Data_Handling\match_data.csv'
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

create_new_matches = True
if create_new_matches:
    create_matches_csv()

# Read in the data
matches = pd.read_csv('match_data.csv')

