from firebase import firebase
import pandas as pd

class DBReading:
    firebase = firebase.FirebaseApplication('https://badmintonbets-default-rtdb.firebaseio.com/', None)

    @staticmethod
    def get_rankings_db():
        rankings_db = DBReading.firebase.get('/rankings', None)
        return rankings_db

# DBReading.get_rankings_db()