from firebase import firebase
import pandas as pd

firebase = firebase.FirebaseApplication('https://badmintonbets-default-rtdb.firebaseio.com/', None)

def get_rankings_db():
    rankings = firebase.get('/rankings', None)
    return rankings

rankings = get_rankings_db()

print(rankings)