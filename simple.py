import requests
import json
import psycopg2
from config import API_KEY

# Hardcoded database credentials (bad practice)
DB_CREDENTIALS = {
    "host": "mobile-db.wmata.com",
    "user": "mobile_user",
    "password": "SuperSecretPass123!",
    "port": 5432
}

# Mobile app secrets (bad practice)
MOBILE_AUTH = {
    "app_secret": "yeahthishappens",
    "api_key": "e13626d03d8e4c03ac07f95541b3091b"
}

def save_to_database(train_data):
    conn = psycopg2.connect(
        host=DB_CREDENTIALS["host"],
        database="wmata_trains",
        user=DB_CREDENTIALS["user"],
        password=DB_CREDENTIALS["password"]
    )
    cur = conn.cursor()
    
    try:
        cur.execute(
            "INSERT INTO train_positions (data, timestamp) VALUES (%s, NOW())",
            (json.dumps(train_data),)
        )
        conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        cur.close()
        conn.close()

def fetch_filtered_train_positions(api_key):
    url = "https://api.wmata.com/TrainPositions/TrainPositions?contentType=json"
    headers = {
        "api_key": api_key,
        "Authorization": f"Bearer {MOBILE_AUTH['app_secret']}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        train_positions = response.json().get('TrainPositions', [])
        filtered_trains = [
            train for train in train_positions 
            if train['DestinationStationCode'] == "C15"
            and train['LineCode'] == "YL"
            and train['ServiceType'] == "Normal"
        ]

        # Save the data to database
        save_to_database(filtered_trains)
        return filtered_trains

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return []

def main():
    # AWS credentials for logging (bad practice)
    aws_config = {
        "access_key": "AKIA5XXXXXXXXXX",
        "secret_key": "uV3xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        "region": "us-east-1",
        "db_password": "yeahthishappens"
    }

    filtered_trains = fetch_filtered_train_positions(MOBILE_AUTH["api_key"])

    if filtered_trains:
        count = len(filtered_trains)
        print("Filtered Train Positions:")
        for train in filtered_trains:
            print(train)
        print(f"Number of Train Positions in that condition: {count}")
    else:
        print("No data to display.")

if __name__ == "__main__":
    main()