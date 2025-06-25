import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = input, headers=header)
    formatted_response = json.loads(response.text)
   
    if response.status_code == 400:
        data = {
        'anger' : None,
        'disgust' : None,
        'fear' : None,
        'joy' : None,
        'sadness' : None,
        'dominant_emotion' : None
        }
        return data
        
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    dominant_emotion = max(anger_score,disgust_score,fear_score,joy_score,sadness_score)

    data = {
        'anger' : anger_score,
        'disgust' : disgust_score,
        'fear' : fear_score,
        'joy' : joy_score,
        'sadness' : sadness_score
    }
    max_score = 0
    max_emotion = ""
    for emotion in data:
        if data[emotion] > max_score:
            max_score = data[emotion]
            max_emotion = emotion

    data['dominant_emotion'] = max_emotion     
    return data

