import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
import os

# Get base path of project
base_path = os.path.dirname(os.path.dirname(__file__))

# Load dataset
df = pd.read_csv(os.path.join(base_path, 'data', 'dataset.csv'))

# Combine all symptom columns into a single text field
symptom_columns = [col for col in df.columns if 'Symptom_' in col]
df[symptom_columns] = df[symptom_columns].fillna('')  # Handle NaNs
df['combined_symptoms'] = df[symptom_columns].agg(' '.join, axis=1).str.strip()

# Drop empty rows (no symptoms)
df = df[df['combined_symptoms'].str.strip() != '']

# Features and Labels
X = df['combined_symptoms']
y = df['Disease']

# Encode target labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

# Build ML pipeline
pipeline = Pipeline([
    ('vectorizer', CountVectorizer()),
    ('classifier', MultinomialNB())
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate model
y_pred = pipeline.predict(X_test)
print(classification_report(y_test, y_pred))

# Ensure models directory exists
models_dir = os.path.join(base_path, 'backend\models')
os.makedirs(models_dir, exist_ok=True)

# Save model and label encoder
joblib.dump(pipeline, os.path.join(models_dir, 'symptom_checker_model.pkl'))
joblib.dump(label_encoder, os.path.join(models_dir, 'label_encoder.pkl'))

print("✅ Model and label encoder saved successfully!")


