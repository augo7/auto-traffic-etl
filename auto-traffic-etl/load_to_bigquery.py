import os
from google.cloud import bigquery
import pandas as pd

client = bigquery.Client()

dataset_id = 'i35_traffic'  
table_id = 'flow_segments'      

# Read the CSV saved by transform step
df = pd.read_csv('traffic_data_cleaned.csv')

# Load DataFrame to BigQuery
job = client.load_table_from_dataframe(df, f"{dataset_id}.{table_id}")
job.result()  # Wait for job to complete

print(f"✅ Loaded {job.output_rows} rows into {dataset_id}.{table_id}")