from flask import Flask, render_template, jsonify, request, abort
from flask_bootstrap import Bootstrap
import requests
from config import API_KEY

app = Flask(__name__, template_folder='templates', static_folder='static')
Bootstrap(app)

API_URL = "https://api.wmata.com/TrainPositions/TrainPositions?contentType=json"

def get_filtered_train_positions():
    headers = {"api_key": API_KEY}
    try:
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            train_positions = response.json().get('TrainPositions', [])
            filtered_positions = [train for train in train_positions if
                                 train['DestinationStationCode'] == "C15" and
                                 train['LineCode'] == "YL" and
                                 train['ServiceType'] == "Normal"]
            return filtered_positions
        else:
            return []
    except requests.exceptions.RequestException as e:
        app.logger.error(f"API request failed: {e}")
        return []

@app.route('/')
def show_train_positions():
    filtered_positions = get_filtered_train_positions()
    total_count = len(filtered_positions)
    return render_template('train_display.html', train_positions=filtered_positions, total_count=total_count)

@app.route('/update_train_positions')
def update_train_positions():
    filtered_positions = get_filtered_train_positions()
    return jsonify(filtered_positions)

if __name__ == "__main__":
    app.run(debug=True)
