# ml_model.py
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Pre-trained model (for demo, we train a model inside the function)
def train_model():
    classifier = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    training_data = [
    [10, 128, 0.8, 0.005,  110],   # Safe
    [20, 256, 0.75, 0.007,  120],  # Safe
    [15, 150, 0.9, 0.02,  180],     # Risky
    [25, 300, 0.85, 0.03,  160],    # Risky
    [5, 100, 0.95, 0.004,  100],   # Safe
    [30, 500, 0.5, 0.04,  200],      # Risky
    [35, 400, 0.6, 0.05,  220],      # Risky
    [12, 180, 0.85, 0.01,  115],    # Safe
]
    training_labels = [1, 1, 0, 0, 1, 0, 0, 1]  # Corresponding labels

    classifier.fit(training_data, training_labels)
    return classifier

def predict_security_risk(features, classifier):
    prediction = classifier.predict(features)
    prediction_proba = classifier.predict_proba(features)  # Get probabilities
    print(f"Prediction probabilities: {prediction_proba}")
    return prediction[0]  # Return 1 for safe, 0 for risky
