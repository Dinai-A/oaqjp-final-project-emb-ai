from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index_view():
    return render_template('index.html')


@app.route("/emotionDetector")
def emotion_detector_view():
    response_str = (
        "For the given statement, the system response is "
        "'anger': {}, 'disgust': {}, 'fear': {}, 'joy': {} and 'sadness': {}. "
        "The dominant emotion is {}."
    )

    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze:
        data = emotion_detector(text_to_analyze)
        return (response_str.format(**data), 200)
    else:
        return (response_str.format(*(None for i in range(6))), 400)


if __name__ == "__main__":
    app.run(debug=True)
