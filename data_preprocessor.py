import pandas as pd
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import RAW_DATA_FILE, PREPROCESSED_DATA_FILE

def preprocess_data():
    print(f"Loading raw data from {RAW_DATA_FILE}...")
    try:
        # Load the raw data
        raw_data = pd.read_csv(RAW_DATA_FILE)
        
        # Check column names
        print(f"Columns in raw data: {raw_data.columns}")
        
        # Verify 'Time' column exists and process it
        if 'Time' not in raw_data.columns:
            raise ValueError("'Time' column is missing in raw data.")
        
        # Preprocess time column for time delta calculation
        raw_data['Time'] = pd.to_datetime(raw_data['Time'], errors='coerce')
        if raw_data['Time'].isnull().all():
            raise ValueError("All values in 'Time' column are invalid timestamps.")

        # Calculate time deltas in seconds
        raw_data['time_delta'] = raw_data['Time'].diff().dt.total_seconds().fillna(0)
        
        # Preprocess packet length
        raw_data['packet_length'] = raw_data['Length'].fillna(0).astype(int)

        # Save preprocessed data
        raw_data.to_csv(PREPROCESSED_DATA_FILE, index=False)
        print(f"Preprocessed data saved to {PREPROCESSED_DATA_FILE}.")
    except FileNotFoundError:
        print(f"Error: {RAW_DATA_FILE} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    preprocess_data()
