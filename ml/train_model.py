import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import os

# load dataset
df = pd.read_csv("data/sample_transactions.csv")

# features
X = df[["amount", "hour", "device_change", "location_change"]]

# target
y = df["fraud"]

# split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# model
model = RandomForestClassifier()

model.fit(X_train, y_train)

# create models folder if missing
os.makedirs("models", exist_ok=True)

# save model
joblib.dump(model, "models/fraud_model.pkl")

print("Model trained and saved successfully.")