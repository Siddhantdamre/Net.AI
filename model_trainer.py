import sys
import os
import pandas as pd
from sklearn.ensemble import IsolationForest
import pickle

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import PREPROCESSED_DATA_FILE, MODEL_FILE

def train_model():
    print(f"Loading preprocessed data from {PREPROCESSED_DATA_FILE}...")
    try:
        # Load the preprocessed data
        data = pd.read_csv(PREPROCESSED_DATA_FILE)
        
        # Check the columns in the data
        print("Columns in preprocessed data:", data.columns)
        
        # Convert 'time_delta' from timedelta to total seconds (if it's in string format)
        data['time_delta'] = pd.to_timedelta(data['time_delta'], errors='coerce').dt.total_seconds()
        
        # Check for any NaN or invalid values in 'time_delta' and fill with 0 if necessary
        data['time_delta'] = data['time_delta'].fillna(0)
        
        # Prepare features (using 'packet_length' and 'time_delta' for anomaly detection)
        features = data[['packet_length', 'time_delta']]
        
        # Initialize and train the model
        model = IsolationForest(contamination=0.1)  # Adjust contamination as needed
        model.fit(features)
        
        # Save the trained model
        with open(MODEL_FILE, 'wb') as model_file:
            pickle.dump(model, model_file)
        
        print(f"Model trained and saved to {MODEL_FILE}.")
    except FileNotFoundError:
        print(f"Error: {PREPROCESSED_DATA_FILE} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    train_model()
