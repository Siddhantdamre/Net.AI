import os
import subprocess

def run_pipeline():
    try:
        print("Step 1: Capturing packets...")
        subprocess.run(["python", "scripts/traffic_capturer.py"], check=True)

        print("\nStep 2: Preprocessing data...")
        subprocess.run(["python", "scripts/data_preprocessor.py"], check=True)

        print("\nStep 3: Training the model...")
        subprocess.run(["python", "scripts/model_trainer.py"], check=True)

        print("\nStep 4: Detecting anomalies...")
        subprocess.run(["python", "scripts/anomaly_detector.py"], check=True)

        print("\nPipeline completed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    run_pipeline()
