import pickle
import pandas as pd
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import MODEL_FILE, PREPROCESSED_DATA_FILE

def detect_anomalies():
    print(f"Loading model from {MODEL_FILE}...")
    try:
        # Load the trained model
        with open(MODEL_FILE, 'rb') as f:
            model = pickle.load(f)
        
        # Load the data for anomaly detection
        print(f"Loading data from {PREPROCESSED_DATA_FILE}...")
        data = pd.read_csv(PREPROCESSED_DATA_FILE)
        
        # Perform anomaly detection
        print("Detecting anomalies...")
        predictions = model.predict(data[['packet_length', 'time_delta']])
        
        # Mark anomalies
        data['anomaly'] = predictions
        
        # Save the results
        result_file = "data/anomaly_results.csv"
        data.to_csv(result_file, index=False)
        print(f"Anomaly detection completed. Results saved to {result_file}.")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    detect_anomalies()

results = pd.read_csv('data/anomaly_results.csv')
print(results.head())