import os
import logging

from dotenv import load_dotenv
import pymysql
from flask import Flask, Response, json, request

app = Flask(__name__)

# Get variables from the .env file
dotenv = load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
# update environment just in case
# os.environ.update(dotenv)
# set globals
RDS_HOST = os.environ.get("DB_HOST")
RDS_PORT = int(os.environ.get("DB_PORT", 3306))
NAME = os.environ.get("DB_USERNAME")
PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

# we need to instantiate the logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def connect():
    try:
        cursor = pymysql.cursors.DictCursor
        conn = pymysql.connect(RDS_HOST,
                               user=NAME, passwd=PASSWORD,
                               db=DB_NAME,
                               port=RDS_PORT,
                               cursorclass=cursor,
                               connect_timeout=5)
        logger.info("SUCCESS: connection to RDS successful")
        return conn
    except Exception:
        logger.exception("Database Connection Error")


# here is how we are handling routing with flask:
@app.route('/')
def index():
    connect()
    return "Hello World!", 200


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        resp_dict = {'first_name': 'John',
                     'last_name': 'doe'}
    elif request.method == 'POST':
        data = request.form
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        resp_dict = {'first_name': first_name,
                     'last_name': last_name,
                     'email': email}
    return Response(json.dumps(resp_dict), 200)


# include this for local dev
if __name__ == '__main__':
    app.run()
