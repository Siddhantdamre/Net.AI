from app.api import create_api
from app.dashboard import create_dashboard

if __name__ == "__main__":
    # Run Flask API
    app = create_api()
    app.run(port=5000, debug=True)

    # Run Dashboard
    dashboard = create_dashboard()
    dashboard.run_server(port=8050, debug=True)
