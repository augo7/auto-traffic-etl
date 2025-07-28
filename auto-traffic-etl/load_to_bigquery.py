import os
from google.cloud import bigquery
from transform_data import df

client = bigquery.Client()

# Define your BigQuery dataset and table
dataset_id = 'your_dataset_id'
table_id = 'your_table_id'

# Load DataFrame to BigQuery
job = client.load_table_from_dataframe(df, f"{dataset_id}.{table_id}")
