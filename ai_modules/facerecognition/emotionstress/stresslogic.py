def get_stress_level(emotion):
    if emotion in ["Sad", "Stressed"]:
        return "High"
    elif emotion == "Neutral":
        return "Medium"
    else:
        return "Low"

