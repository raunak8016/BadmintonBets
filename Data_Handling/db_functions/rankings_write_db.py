from firebase import firebase
import pandas as pd

firebase = firebase.FirebaseApplication('https://badmintonbets-default-rtdb.firebaseio.com/', None)

rankings = pd.read_csv('rankings.csv').to_numpy().tolist()

def write_rankings_db(rankings):
    firebase.put('/','rankings',rankings)

write_rankings_db(rankings)