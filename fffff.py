import flask
import requests
import pymysql

app = flask.Flask(__name__)
app.config['DEBUG'] = True
@app.route('/',methods=['GET'])

def home():
    return 'bye world'

if __name__ == '__main__':
    app.run()