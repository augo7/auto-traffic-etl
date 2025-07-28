from dotenv import load_dotenv
import os
from google.cloud import bigquery
from google.api_core.exceptions import Conflict
import time
import requests
from datetime import datetime


load_dotenv()

api_key = os.getenv("TRAFFIC_API_KEY")

if api_key is None:
    print("Error: TRAFFIC_API_KEY is not set in the environment variables.")
else:
    print("TRAFFIC_API_KEY is set successfully.")

if not api_key:
    raise ValueError("TRAFFIC_API_KEY is not set in the environment variables.")

# I-35 coordinates through Austin
i35_coords = [
    (30.4489, -97.6788),  # North
    (30.3683, -97.7004),
    (30.3183, -97.6981),
    (30.2672, -97.7431),
    (30.2412, -97.7396),
    (30.1632, -97.7606),
    (30.1192, -97.7611),  # South
]

traffic_data = []

for lat, lon in i35_coords:
    print(f"Getting data for I-35 point ({lat}, {lon})")
    #api call (request)
    url = f"https://api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/json?point={lat}%2C{lon}&key={api_key}"   
    response = requests.get(url)

    if response.status_code == 200: # 2xx means last request was successful
        data = response.json() #6
        flow_segment = data.get("flowSegmentData", {})
        traffic_data.append({
            "latitude": flow_segment.get("coordinates", {}).get("coordinate", [{}])[0].get("latitude"),
            "longitude": flow_segment.get("coordinates", {}).get("coordinate", [{}])[0].get("longitude"),
            "current_speed": flow_segment.get("currentSpeed"),
            "free_flow_speed": flow_segment.get("freeFlowSpeed"),
            "confidence": flow_segment.get("confidence"),
            "timestamp": flow_segment.get("timestamp") or datetime.utcnow().isoformat(),
            "segment_label": flow_segment.get("segmentLabel") or "unknown"
        })
    else:
        print(f"Error fetching data for ({lat}, {lon}): {response.status_code}")
    
    time.sleep(0.5)  # Prevent rate limit issues

print(f"\n✅ Collected traffic data for {len(traffic_data)} I-35 segments.")

import json

with open('traffic_data.json', 'w') as f:
    for record in traffic_data:
        json.dump(record, f)
        f.write('\n')


print("✅ Saved traffic data to traffic_data.json")


