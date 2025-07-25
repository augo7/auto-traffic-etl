# auto-traffic-etl

🚦 Traffic ETL Pipeline – BigQuery Automation

This project automates the extraction, transformation, and loading (ETL) of real-time or historical traffic data from public APIs into a Google BigQuery dataset. It’s built as a professional-grade portfolio project to showcase data engineering, automation, and traffic analytics skills.

🎯 Project Objectives

Build an automated ETL pipeline using Python

Extract traffic or urban mobility data from:

Austin Open Data

NYC Open Data

Google Maps Traffic Layer

Clean and transform the data using pandas

Load cleaned data into Google BigQuery

Set up daily or weekly automatic data refreshes using GitHub Actions or a scheduled script

🔁 ETL Structure

1. Extract

Connect to public traffic APIs

Pull data in JSON or CSV format

(Optionally) store raw data locally or in cloud storage

2. Transform

Use Python + pandas to:

Handle missing timestamps or GPS data

Normalize time zones and extract day/time

Group by region or time intervals

(Optional) Cluster or geotag high-traffic zones

3. Load

Upload cleaned datasets into a BigQuery table

Append or overwrite data based on freshness

📊 Data Analysis Goals

Use BigQuery SQL to explore and answer:

What are the peak traffic times by area or day of the week?

How does congestion evolve over time?

Which intersections consistently experience high volume?

Leverage SQL window functions for:

Rolling averages

Percent change

Traffic volume rankings

⏱️ Bonus: Scheduled Automation

Set up a scheduled process to:

Fetch new traffic data on a daily or weekly basis

Automatically transform and load into BigQuery

Tools: GitHub Actions or Python + cron

🧰 Tech Stack

Python (pandas, requests, google-cloud-bigquery)

Google BigQuery

GitHub Actions (CI/CD automation)

Public traffic data in JSON or CSV
