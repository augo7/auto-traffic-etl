import pandas as pd
import json

# Load your JSON file (replace 'traffic_data.json' with your filename)
df = pd.read_json('traffic_data.json', lines=True)

# Handle missing timestamps or location data
df = df.dropna(subset=['timestamp', 'latitude', 'longitude'])

# Normalize time zones (assuming UTC, adjust as needed)
df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)

# Extract day and hour info
df['day'] = df['timestamp'].dt.date
df['hour'] = df['timestamp'].dt.hour

# Group by region (e.g., segment_label) or time period (e.g., hour)
grouped = df.groupby(['segment_label', 'hour']).agg({
    'current_speed': 'mean',
    'free_flow_speed': 'mean',
    'confidence': 'mean'
}).reset_index()

# Optionally: Cluster congested zones (using k-means)
from sklearn.cluster import KMeans

coords = df[['latitude', 'longitude']]
kmeans = KMeans(n_clusters=3, random_state=0).fit(coords)
df['zone_cluster'] = kmeans.labels_

# Save cleaned and transformed data
df.to_csv('traffic_data_cleaned.csv', index=False)
grouped.to_csv('traffic_data_grouped.csv', index=False)

print("✅ Saved grouped traffic data to traffic_data_grouped.csv")