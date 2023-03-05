from flask import Flask
from db_functions.db_reading import DBReading

app = Flask(__name__)

@app.route('/rankings')

def rankings():
    return {'rankings': DBReading.get_rankings_db()}

@app.route('/rankings/<int:rank>')

def rankings_rank():
    return {'rankings': DBReading.get_rankings_db()}

if __name__ == '__main__':
    app.run(debug=True)