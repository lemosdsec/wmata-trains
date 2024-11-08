import requests
import json
import psycopg2
from config import API_KEY, DB_CONFIG, MOBILE_AUTH, AWS_CONFIG


def save_to_database(train_data):
    conn = psycopg2.connect(
        host=DB_CONFIG["host"],
        database="wmata_trains",
        user=DB_CONFIG["user"],
        password=DB_CONFIG["password"]
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

        save_to_database(filtered_trains)
        return filtered_trains

    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return []


def main():
    filtered_trains = fetch_filtered_train_positions(API_KEY)

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
