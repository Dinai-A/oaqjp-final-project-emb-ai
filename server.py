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
    data = emotion_detector(text_to_analyze)
    if text_to_analyze:
        return (response_str.format(*data.values()), 200)
    else:
        return ("Invalid text! Please try again!", 400)


if __name__ == "__main__":
    app.run(debug=True)
