import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Format input JSON
    input_data = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send POST request to Watson NLP API
    response = requests.post(url, headers=headers, json=input_data)

    # Convert the response text to JSON format
    response_json = response.json()

    if response.status_code == 200:
        # Extract emotions and their scores
        emotions = response_json['emotionPredictions'][0]['emotion']
        
        # Find the dominant emotion (highest score)
        dominant_emotion = max(emotions, key=emotions.get)
        
        # Return the required output format
        return {
            'anger': emotions['anger'],
            'disgust': emotions['disgust'],
            'fear': emotions['fear'],
            'joy': emotions['joy'],
            'sadness': emotions['sadness'],
            'dominant_emotion': dominant_emotion
        }
    else:
        return f"Error: {response.status_code} - {response.text}"