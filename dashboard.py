import dash
from dash import dcc, html
import pandas as pd
from config import RAW_DATA_FILE

def create_dashboard():
    app = dash.Dash(__name__, title="Network Traffic Analyzer")

    def load_data():
        try:
            return pd.read_csv(RAW_DATA_FILE)
        except FileNotFoundError:
            return pd.DataFrame(columns=["Time", "Length"])

    data = load_data()

    app.layout = html.Div([
        html.H1("Network Traffic Dashboard"),
        dcc.Graph(
            id="traffic-chart",
            figure={
                "data": [
                    {"x": data["Time"], "y": data["Length"], "type": "line", "name": "Packet Length"}
                ],
                "layout": {"title": "Packet Length Over Time"}
            }
        )
    ])
    return app
