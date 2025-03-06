import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
import joblib
import os

# Load your dataset
data = pd.read_csv('resume_labels.csv')  # Update this path if needed

# Read resumes from the Uploaded_Resumes folder
resumes = []
for filename in data['filename']:
    file_path = os.path.join('uploads', 'Uploaded_Resumes', filename)  # Update this path
    with open(file_path, 'r', encoding='utf-8') as file:
        resumes.append(file.read())

# Add resume text to the DataFrame
data['resume_text'] = resumes

# Feature extraction
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data['resume_text'])
y = data['label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Instantiate base models for the VotingClassifier
logreg = LogisticRegression(max_iter=1000)
rf = RandomForestClassifier(n_estimators=100)
nb = MultinomialNB()

# Instantiate the VotingClassifier with the base models
voting_model = VotingClassifier(estimators=[
    ('logreg', logreg),
    ('rf', rf),
    ('nb', nb)
], voting='hard')

# Train the Voting Classifier
voting_model.fit(X_train, y_train)

# Evaluate the model on the test set
accuracy = voting_model.score(X_test, y_test)
print(f'Voting Classifier Accuracy: {accuracy * 100:.2f}%')

# Save the model and vectorizer
os.makedirs('model', exist_ok=True)
joblib.dump(voting_model, 'model/resume_voting_model.pkl')
joblib.dump(vectorizer, 'model/vectorizer.pkl')

print("Voting Classifier setup complete, model saved.")
