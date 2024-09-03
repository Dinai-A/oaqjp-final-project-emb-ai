from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index_view():
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_view():
    text_to_analyze = request.args["textToAnalyze"]
    data = emotion_detector(text_to_analyze)
    response_str = (
        f"For the given statement, the system response is 'anger': {data['anger']}, 'disgust': {data['disgust']},"
        f" 'fear': {data['fear']}, 'joy': {data['joy']} and 'sadness': {data['sadness']}. "
        f"The dominant emotion is {data['dominant_emotion']}."
    )
    return response_str


if __name__ == "__main__":
    app.run(debug=True)
