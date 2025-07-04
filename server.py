''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#initiate flask app
app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def emot_detector():
    '''function retrieves the text input and checks for errors'''
    # Retrieve text from request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass text to emotion detector function and store response
    response = emotion_detector(text_to_analyze)
    # Extract individual emotion scores and dominant emotion
    anger = response.get('anger')
    disgust = response.get('disgust')
    fear = response.get('fear')
    joy = response.get('joy')
    sadness = response.get('sadness')
    dominant_emotion = response.get('dominant_emotion')

    # Create formatted output string
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."
    )

    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel'''
    return render_template('index.html')

if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
