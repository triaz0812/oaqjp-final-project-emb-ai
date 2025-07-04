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

    #Get top-level emotion name value pairs and populate extracted dict
    extracted = {}
   '''Use get() method to avoid error or crashes. If no vaue returns default specified, i.e first instance list with empty dict and in second instance an empty dict'''

    emotions = formatted_response.get('emotionPredictions', [{}])[0].get('emotion', {})
    extracted.update(emotions)

    #Calculate dominant emotion
    '''Use max() method with key to find highest score. Avoids using manual loop and more efficient. Could use an if statement to check extracted is not empty for more stability. May add later'''

    dominant_emotion = max(extracted, key=extracted.get)
    extracted['dominant_emotion'] = dominant_emotion

    #Return result
    return extracted
   