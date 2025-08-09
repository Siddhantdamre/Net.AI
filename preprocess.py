import pandas as pd
from config import RAW_DATA_FILE, PREPROCESSED_DATA_FILE

def preprocess_data():
    try:
        data = pd.read_csv(RAW_DATA_FILE)
    except FileNotFoundError:
        print(f"File {RAW_DATA_FILE} not found. Capture traffic first.")
        return

    # Example preprocessing: Remove null values
    data = data.dropna()
    data.to_csv(PREPROCESSED_DATA_FILE, index=False)
    print(f"Preprocessed data saved to {PREPROCESSED_DATA_FILE}")

if __name__ == "__main__":
    preprocess_data()
