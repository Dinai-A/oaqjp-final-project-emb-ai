import requests

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze: str):
    input_json = {"raw_document": {"text": text_to_analyze}}
    r = requests.post(URL, json=input_json, headers=headers)
    data = r.json()["emotionPredictions"][0]["emotion"]
    dominant_emotion, max_score = None, 0
    for emotion_name, score in data.items():
        if score > max_score:
            max_score = score
            dominant_emotion = emotion_name
    data["dominant_emotion"] = dominant_emotion
    return data
