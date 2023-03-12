import pandas as pd
import numpy as np
import datetime as dt
from handle_score import handle_score

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + dt.timedelta(days_ahead) - dt.timedelta(days=7)



def draws_into_matches_32(path, tourn_date: str):

    draw_df = pd.read_csv(r'{path}\draw_info.csv')
    seed_df = pd.read_csv(r'{path}\general_info.csv')

    draw_arr = draw_df.values.T.tolist()
    print(draw_arr)

    nearest_ranking = next_weekday(dt.datetime.strftime(tourn_date, '%m-%d-%Y'), 1)
    ranking_df = pd.read_csv(r'rankings.csv')
    seed_df

    for i, round in enumerate(draw_arr):
        if i == len(draw_arr) - 1:
            break

        for j in range(len(round)):
            p1 = round[j]
            p2 = round[j+1]
            p1_rank = ranking_df.loc[(ranking_df['Player'] == p1 & ranking_df['Date'] == nearest_ranking), 'Ranking']
            p2_rank = ranking_df.loc[(ranking_df['Player'] == p2 & ranking_df['Date'] == nearest_ranking), 'Ranking']
            p1_seed = -1
            p2_seed = -1
            if p1 in seed_df['Player'].to_numpy():
                p1_seed = seed_df.loc[seed_df['Player'] == p1, 'Seed']
            if p2 in seed_df['Player'].to_numpy():
                p2_seed = seed_df.loc[seed_df['Player'] == p2, 'Seed']
            score = handle_score(draw_arr[i+1][j])

            p1_g1 = 0
            p1_g2 = 0
            p1_g3 = 0
            p2_g1 = 0
            p2_g2 = 0
            p2_g3 = 0
            p1_tpw = 0
            p2_tpw = 0
            p1_tpl = 0
            p2_tpl = 0
            p1_tsw = 0
            p2_tsw = 0
            p1_tgp = 0
            p2_tgp = 0
            p1p2_h2h = 0
            p2p1_h2h = 0
            winner = -1

            if draw_arr[i+1][j] == p1:
                winner = 1
            elif draw_arr[i+1][j] == p2:
                winner = 2
            
            if winner == 1:


            j+=1




df = pd.read_csv(r'tournament_data\training\DAIHATSU Indonesia Masters 2023\draw_info.csv')
draws_into_matches_32(df)