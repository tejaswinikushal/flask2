from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def hello_world():
    return """Company Name: ABC Corporation\n
Location: India\n
Contact Detail: 999-999-9999"""

if __name__=="__main__":
    app.run(host="0.0.0.0")
