import pandas as pd
import requests

# --- API settings ---
APP_ID = '' #deleted due security reasons
APP_KEY = '' #deleted due security reasons
BASE_URL = "https://transportapi.com/v3/uk/bus/stop_timetables/{stop_id}.json"

# --- Parameters ---
stop_id = '490014051VC'

# --- Request timetable for one stop ---
url = BASE_URL.format(stop_id=stop_id)
params = {
    'app_id': APP_ID,
    'app_key': APP_KEY
    # No 'date' parameter – defaults to today
}

response = requests.get(url, params=params)

# --- Process the response ---
if response.status_code == 200:
    data = response.json()
    departures = []

    if 'departures' in data:
        for line in data['departures'].values():
            for service in line:
                departure_info = {
                    'line': service.get('line', ''),
                    'direction': service.get('direction', ''),
                    'aimed_departure_time': service.get('aimed_departure_time', ''),
                    'expected_departure_time': service.get('expected_departure_time', ''),
                    'operator': service.get('operator', ''),
                }
                departures.append(departure_info)

    # Create a table
    departures_df = pd.DataFrame(departures)

    # --- Filter: only show services going to Manchester ---
    birmingham_buses = departures_df[departures_df['direction'].str.contains('Manchester', case=False, na=False)]

    # Show the filtered result
    print(birmingham_buses)

else:
    print(f"Error {response.status_code}: {response.text}")
