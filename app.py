from flask import Flask, Response, json

app = Flask(__name__)


# here is how we are handling routing with flask:
@app.route('/')
def index():
    return "Hello World!", 200


@app.route('/user', methods=['GET'])
def user():
    resp_dict = {'first_name': 'John',
                 'last_name': 'doe'}
    return Response(json.dumps(resp_dict), 200)


# include this for local dev
if __name__ == '__main__':
    app.run()
