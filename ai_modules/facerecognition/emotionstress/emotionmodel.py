import random

def predict_emotion(face_features):
    emotions = ["Neutral", "Happy", "Sad", "Stressed"]
    return random.choice(emotions)

