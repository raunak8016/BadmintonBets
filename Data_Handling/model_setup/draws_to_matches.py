import pandas as pd
import numpy as np
from datetime import datetime as dt
from handle_score import handle_score
from h2h import h2h
import datetime
import sys
sys.path.insert(0, "/python_scraping")

def next_weekday(d, weekday):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return d + datetime.timedelta(days_ahead) - datetime.timedelta(days=7)

def locate_ranking(name: str, week: datetime):
    try:
        week_str = week.strftime('%m/%d/%Y')
        print(week_str)
        ranking_df = pd.read_csv(r'C:\Users\rauna\BadmintonApp\Data_Handling\rankings.csv')
        ranking = ranking_df.loc[(ranking_df['Name'] == name.upper()) & (ranking_df['Ranking Week'] == week_str), 'Rank'].values[0]
        return ranking
    except:
        return 100

def draws_into_matches_32(path, tourn_date: str):

    draw_df = pd.read_csv(r'{0}\draw_info.csv'.format(path))
    seed_df = pd.read_csv(r'{0}\general_info.csv'.format(path))

    draw_arr = draw_df.values.T.tolist()
    print(draw_arr[1])
    nearest_ranking = next_weekday(dt.strptime(tourn_date, '%m/%d/%Y'), 1)
    print(nearest_ranking)
    ranking_df = pd.read_csv(r'C:\Users\rauna\BadmintonApp\Data_Handling\rankings.csv')

    match_df = pd.DataFrame(columns=['Player1', 'Player2', 'Player1_Rank', 'Player2_Rank', 'Player1_Seed', 'Player2_Seed', 'Player1_G1', 'Player1_G2', 'Player1_G3', 'Player2_G1', 'Player2_G2', 'Player2_G3', 'Player1_TPW', 'Player2_TPW', 'Player1_TPL', 'Player2_TPL', 'Player1_TSW', 'Player2_TSW', 'Player1p2_H2H', 'Player2p1_H2H', 'Winner'])

    for i, round in enumerate(draw_arr):
        if i == len(draw_arr) - 1:
            break
        if i == 0:
            for j in range(0,len(round),2):
                p1 = round[j]
                p2 = round[j+1]
                print(p1, p2)
                p1_rank = locate_ranking(p1, nearest_ranking)
                p2_rank = locate_ranking(p2, nearest_ranking)
                p1_seed = -1
                p2_seed = -1
                if p1 in seed_df['Players'].to_numpy():
                    p1_seed = seed_df.loc[seed_df['Players'] == p1, 'Seed'].values[0]
                if p2 in seed_df['Players'].to_numpy():
                    p2_seed = seed_df.loc[seed_df['Players'] == p2, 'Seed'].values[0]
                print(draw_arr[i+1][j+1])
                print(i)
                print(j)
                score = handle_score(draw_arr[i+1][j+1])

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
        #     p1_tgp = 0
        #     p2_tgp = 0
                [p1p2_h2h, p2p1_h2h] = h2h(p1, p2)
                winner = -1

                if draw_arr[i+1][j] == p1:
                    winner = 1
                elif draw_arr[i+1][j] == p2:
                    winner = 2
                
                for k, game in enumerate(score):
                    if k==0:
                        p1_g1 = game[0]
                        p2_g1 = game[1]
                    elif k==1:
                        p1_g2 = game[0]
                        p2_g2 = game[1]
                    elif k==2:
                        p1_g3 = game[0]
                        p2_g3 = game[1]

                p1_tpw = p1_g1 + p1_g2 + p1_g3
                p2_tpw = p2_g1 + p2_g2 + p2_g3

                p1_tpl = p2_g1 + p2_g2 + p2_g3
                p2_tpl = p1_g1 + p1_g2 + p1_g3

                if winner == 1:
                    if score[2][0] > 0:
                        p1_tsw = 2
                        p2_tsw = 1
                    else:
                        p1_tsw = 2
                        p2_tsw = 0
                elif winner == 2:
                    if score[2][1] > 0:
                        p1_tsw = 1
                        p2_tsw = 2
                    else:
                        p1_tsw = 0
                        p2_tsw = 2

                match_data = pd.Series([p1, p2, p1_rank, p2_rank, p1_seed, p2_seed, p1_g1, p1_g2, p1_g3, p2_g1, p2_g2, p2_g3, p1_tpw, p2_tpw, p1_tpl, p2_tpl, p1_tsw, p2_tsw, p1p2_h2h, p2p1_h2h, winner], index=['Player1', 'Player2', 'Player1_Rank', 'Player2_Rank', 'Player1_Seed', 'Player2_Seed', 'Player1_G1', 'Player1_G2', 'Player1_G3', 'Player2_G1', 'Player2_G2', 'Player2_G3', 'Player1_TPW', 'Player2_TPW', 'Player1_TPL', 'Player2_TPL', 'Player1_TSW', 'Player2_TSW', 'Player1p2_H2H', 'Player2p1_H2H', 'Winner'])
                match_df.loc[len(match_df)]= match_data
            continue
        for j in range(0,len(round),4):
            p1 = str(round[j])
            p2 = str(round[j+2])
            print(p1)
            if p1 == 'nan' or p2 == 'nan':
                break

            print(p1, p2)
            print(i)
            print(j)
            p1_rank = locate_ranking(p1, nearest_ranking)
            p2_rank = locate_ranking(p2, nearest_ranking)
            p1_seed = -1
            p2_seed = -1
            if p1 in seed_df['Players'].to_numpy():
                p1_seed = seed_df.loc[seed_df['Players'] == p1, 'Seed'].values[0]
            if p2 in seed_df['Players'].to_numpy():
                p2_seed = seed_df.loc[seed_df['Players'] == p2, 'Seed'].values[0]
            
            winner = -9

            sc_indx = 0
            if p1 in draw_arr[i+1]:
                sc_indx = draw_arr[i+1].index(p1)
                winner = 1
            elif p2 in draw_arr[i+1]:
                sc_indx = draw_arr[i+1].index(p2)
                winner = 2
            else:
                print(draw_arr[i+1])
                SystemExit("Player not found in draw")
            print(sc_indx)
            score = handle_score(draw_arr[i+1][sc_indx+1])

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
       #     p1_tgp = 0
       #     p2_tgp = 0
            [p1p2_h2h, p2p1_h2h] = h2h(p1, p2)

            if draw_arr[i+1][j] == p1:
                winner = 1
            elif draw_arr[i+1][j] == p2:
                winner = 2
            
            for k, game in enumerate(score):
                if k==0:
                    p1_g1 = game[0]
                    p2_g1 = game[1]
                elif k==1:
                    p1_g2 = game[0]
                    p2_g2 = game[1]
                elif k==2:
                    p1_g3 = game[0]
                    p2_g3 = game[1]

            p1_tpw = p1_g1 + p1_g2 + p1_g3
            p2_tpw = p2_g1 + p2_g2 + p2_g3

            p1_tpl = p2_g1 + p2_g2 + p2_g3
            p2_tpl = p1_g1 + p1_g2 + p1_g3

            if winner == 1:
                if score[2][0] > 0:
                    p1_tsw = 2
                    p2_tsw = 1
                else:
                    p1_tsw = 2
                    p2_tsw = 0
            elif winner == 2:
                if score[2][1] > 0:
                    p1_tsw = 1
                    p2_tsw = 2
                else:
                    p1_tsw = 0
                    p2_tsw = 2

            match_data = pd.Series([p1, p2, p1_rank, p2_rank, p1_seed, p2_seed, p1_g1, p1_g2, p1_g3, p2_g1, p2_g2, p2_g3, p1_tpw, p2_tpw, p1_tpl, p2_tpl, p1_tsw, p2_tsw, p1p2_h2h, p2p1_h2h, winner], index=['Player1', 'Player2', 'Player1_Rank', 'Player2_Rank', 'Player1_Seed', 'Player2_Seed', 'Player1_G1', 'Player1_G2', 'Player1_G3', 'Player2_G1', 'Player2_G2', 'Player2_G3', 'Player1_TPW', 'Player2_TPW', 'Player1_TPL', 'Player2_TPL', 'Player1_TSW', 'Player2_TSW', 'Player1p2_H2H', 'Player2p1_H2H', 'Winner'])
            match_df.loc[len(match_df)]= match_data
    match_df.to_csv(r'C:\Users\rauna\BadmintonApp\Data_Handling\testing\match_data.csv', index=False)
    return match_df
    


print(draws_into_matches_32(r'C:\Users\rauna\BadmintonApp\Data_Handling\tournament_data\training\YONEX SUNRISE India Open 2023', '1/17/2023'))