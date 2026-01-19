import pickle

# Load trained model and vectorizer
model = pickle.load(open("phishing_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def detect_phishing(message):
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)

    if prediction[0] == 1:
        return "⚠️ WARNING: This looks like a PHISHING message. Do NOT click links or share OTPs."
    else:
        return "✅ This message appears SAFE."
