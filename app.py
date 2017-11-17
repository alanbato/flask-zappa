from flask import Flask, Response, json, request

app = Flask(__name__)


# here is how we are handling routing with flask:
@app.route('/')
def index():
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
