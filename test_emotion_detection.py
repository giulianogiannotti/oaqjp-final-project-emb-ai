import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        joy_dominant_emotion = emotion_detector("I am glad this happened")['dominant_emotion']
        self.assertEqual(joy_dominant_emotion, 'joy')

        anger_dominant_emotion = emotion_detector("I am really mad about this")['dominant_emotion']
        self.assertEqual(anger_dominant_emotion, 'anger')

        disgust_dominant_emotion = emotion_detector("I feel disgusted just hearing about this")['dominant_emotion']
        self.assertEqual(disgust_dominant_emotion, 'disgust')

        sadness_dominant_emotion = emotion_detector("I am so sad about this")['dominant_emotion']
        self.assertEqual(sadness_dominant_emotion, 'sadness')

        fear_dominant_emotion = emotion_detector("I am really afraid that this will happen")['dominant_emotion']
        self.assertEqual(fear_dominant_emotion, 'fear')

unittest.main()        