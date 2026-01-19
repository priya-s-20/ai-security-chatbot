import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
data = pd.read_csv("phishing_dataset.csv")

# Split data
X = data["text"]
y = data["label"]

# Convert text to numerical form
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train the ML model
model = MultinomialNB()
model.fit(X_vectorized, y)

# Save trained model and vectorizer
pickle.dump(model, open("phishing_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("✅ Phishing model trained successfully")
