import joblib
import numpy as np

model = joblib.load("models/fraud_model.pkl")

def predict_transaction(amount, hour, device_change, location_change):

    features = np.array([[amount, hour, device_change, location_change]])

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    return prediction, round(probability,2)