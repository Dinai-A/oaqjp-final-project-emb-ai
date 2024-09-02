import unittest
from EmotionDetection import emotion_detector


class TestEmotionDetection(unittest.TestCase):

    def test_dominant_joy(self):
        data = emotion_detector("I am glad this happened")
        self.assertEqual("joy", data["dominant_emotion"])

    def test_dominant_anger(self):
        data = emotion_detector("I am really mad about this")
        self.assertEqual("anger", data["dominant_emotion"])

    def test_dominant_disgust(self):
        data = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual("disgust", data["dominant_emotion"])

    def test_dominant_sadness(self):
        data = emotion_detector("I am so sad about this")
        self.assertEqual("sadness", data["dominant_emotion"])

    def test_dominant_fear(self):
        data = emotion_detector("I am really afraid that this will happen")
        self.assertEqual("fear", data["dominant_emotion"])


if __name__ == '__main__':
    unittest.main()
