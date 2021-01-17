from flask import Flask
from flask import request
app = Flask(__name__)

# http://localhost:5000/home --> Base URL

@app.route("/home")
def index():
    return "Hello Falsk"

@app.route("/users/<user_id>", methods = ["GET","POST", "PUT","DELETE"])
def parameter(user_id):
    if request.method == "GET":
        return "GET method"

    elif request.method == "POST":
        data = request.form
        return data

    elif request.method == "PUT":


        return "PUT method"

    elif request.method == "DELETE":
        return "DELETE method"

    else:
        return "Not allowed method"

app.run(host='localhost', port=5000) # 0.0.0.0 = localhost