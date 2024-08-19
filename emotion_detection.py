import requests

URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
headers={"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def emotion_detector(text_to_analyze: str):
    input_json = {"raw_document": {"text": text_to_analyze}}
    r = requests.post(URL, data=input_json, headers=headers)
    text = r.json()["text"]
    return text
