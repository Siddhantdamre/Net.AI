import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle
from config import PREPROCESSED_DATA_FILE, MODEL_FILE

def train_anomaly_detector():
    try:
        data = pd.read_csv(PREPROCESSED_DATA_FILE)
    except FileNotFoundError:
        print(f"File {PREPROCESSED_DATA_FILE} not found. Preprocess data first.")
        return

    features = ["Length"]  # Use packet length as an example
    X = data[features]

    model = IsolationForest(contamination=0.1, random_state=42)
    model.fit(X)

    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {MODEL_FILE}")

if __name__ == "__main__":
    train_anomaly_detector()
