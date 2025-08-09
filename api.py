from flask import Flask, jsonify, request
import pandas as pd
import pickle
from config import RAW_DATA_FILE, MODEL_FILE

def create_api():
    app = Flask(__name__)

    try:
        with open(MODEL_FILE, "rb") as f:
            model = pickle.load(f)
    except FileNotFoundError:
        model = None

    @app.route("/packets", methods=["GET"])
    def get_packets():
        try:
            data = pd.read_csv(RAW_DATA_FILE)
            return data.to_json(orient="records")
        except FileNotFoundError:
            return jsonify({"error": "No captured data found."}), 404

    @app.route("/predict", methods=["POST"])
    def predict():
        payload = request.json
        features = payload.get("features", [])
        if not features or model is None:
            return jsonify({"error": "Invalid request or model not found"}), 400

        prediction = model.predict([features])
        return jsonify({"prediction": "Normal" if prediction[0] == 1 else "Anomaly"})

    return app
