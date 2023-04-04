from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
     return "Welcome to Flask app in docker container"

app.run(host="0.0.0.0",port=5000)