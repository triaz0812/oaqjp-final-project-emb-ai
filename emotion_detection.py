import requests
import json

def emotion_detector(text_to_analyse):
    #Path to emotion analysis api
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    #Set headers with required model id for 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    #Create dict object with text to be analysed
    myobj =  { "raw_document": { "text": text_to_analyse } }

    #Make POST request to API with content obj and headers
    response = requests.post(url, json=myobj, headers=header)

    #Parse API response
    formatted_response = json.loads(response.text)

    #Return result
    return formatted_response