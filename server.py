""" Server to analyze emotions """
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route('/emotionDetector')
def emotion_analyzer():
    """Detects the emotion in a text"""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    analysis = (
    f"For the given statement, the system response is "
    f"'anger': {response['anger']}, "
    f"'disgust': {response['disgust']}, "
    f"fear: {response['fear']}, "
    f"joy: {response['joy']}, "
    f"sadness: {response['sadness']}. "
    f"The dominant emotion is {response['dominant_emotion']}"
    )

    return analysis
 
@app.route('/')
def render_index_page():
    """Renders the index page"""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(port=5000)
