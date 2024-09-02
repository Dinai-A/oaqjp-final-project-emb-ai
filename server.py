from flask import Flask

app = Flask(__name__)


@app.route("/emotionDetector")
def emotionDetector():
    return "some text"
