import requests
from config import API_KEY

def fetch_filtered_train_positions(api_key):
    url = "https://api.wmata.com/TrainPositions/TrainPositions?contentType=json"
    headers = {"api_key": api_key}

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
