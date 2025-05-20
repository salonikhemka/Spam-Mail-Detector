import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load dataset
df = pd.read_csv('spam_data.csv')

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(df['email'], df['label'], test_size=0.3, random_state=42)

# Vectorizer and model
count_vectorizer = CountVectorizer(stop_words='english')
X_train_counts = count_vectorizer.fit_transform(X_train)

model = MultinomialNB()
model.fit(X_train_counts, y_train)

# Save vectorizer and model
pickle.dump(count_vectorizer, open('count_vectorizer_v2.pickle', 'wb'))
pickle.dump(model, open('spam_detector_v2.pickle', 'wb'))

print("Model and vectorizer saved!")

# Test accuracy
X_test_counts = count_vectorizer.transform(X_test)
print("Test Accuracy:", model.score(X_test_counts, y_test))
