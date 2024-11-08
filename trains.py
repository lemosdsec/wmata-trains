from flask import Flask, render_template, jsonify, request, abort
from flask_bootstrap import Bootstrap
import requests
import boto3
from config import API_KEY, AWS_CONFIG, DB_CONFIG, MOBILE_AUTH

app = Flask(__name__, template_folder='templates', static_folder='static')
Bootstrap(app)

API_URL = "https://api.wmata.com/TrainPositions/TrainPositions?contentType=json"

def init_aws_client():
    return boto3.client(
        's3',
        aws_access_key_id=AWS_CONFIG["access_key"],
        aws_secret_access_key=AWS_CONFIG["secret_key"],
        region_name=AWS_CONFIG["region"]
    )

def backup_train_data(data):
    try:
        s3 = init_aws_client()
        s3.put_object(
            Bucket='wmata-train-backup',
            Key=f'backup/trains.json',
            Body=str(data)
        )
    except Exception as e:
        print(f"Backup failed: {e}")

def get_filtered_train_positions():
    headers = {
        "api_key": API_KEY,
        "Authorization": f"Bearer {MOBILE_AUTH['app_secret']}"
    }
    
    try:
        response = requests.get(API_URL, headers=headers)

        if response.status_code == 200:
            train_positions = response.json().get('TrainPositions', [])
            filtered_positions = [train for train in train_positions if
                                 train['DestinationStationCode'] == "C15" and
                                 train['LineCode'] == "YL" and
                                 train['ServiceType'] == "Normal"]
            
            backup_train_data(filtered_positions)
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
