🚦 Traffic Data Pipeline: Automated ETL with Python & BigQuery
This project delivers a scalable, automated ETL (Extract, Transform, Load) pipeline for collecting, processing, and analyzing real-time urban traffic data. Using public mobility APIs, Python’s data stack, and Google BigQuery, the pipeline is designed to reflect real-world data engineering practices and support time-based traffic analytics at city scale.

By incorporating API integration, automated scheduling, and cloud warehousing, this project enables streamlined data ingestion and intelligent traffic insights across geographic and temporal dimensions.

🔍 Project Highlights

API Integration & Data Extraction:
Connects to open mobility APIs (e.g. Austin Open Data, NYC Open Data) to pull traffic data in structured formats (JSON/CSV), with flexibility for expanding to additional urban regions.

Data Transformation:
Cleans and organizes traffic data using Python and Pandas—handling missing timestamps, normalizing time zones, and engineering features like time of day, weekday, and geographic zones.

Cloud Data Warehousing:
Loads the transformed datasets into Google BigQuery, enabling fast, scalable querying for trend analysis and congestion insights.

Scheduling & Automation:
Implements a scheduled update system using GitHub Actions (or cron), automating daily or weekly pulls and refreshes to keep BigQuery tables up-to-date without manual intervention.

Analytical Insight:
Supports complex SQL queries to identify peak congestion windows, compare traffic volumes across neighborhoods, and track changes in urban flow over time using window functions and ranking.

🛠️ Technologies & Tools

Technology	Purpose
Python	Core language for data ingestion and processing
Pandas	Data wrangling and time-based feature engineering
Public Traffic APIs	Sources of real-time or historical traffic data
Google BigQuery	Cloud-scale storage and SQL analytics
GitHub Actions	CI/CD and scheduled job automation
.env + dotenv	Secure management of API keys and configs
Git & GitHub	Version control and collaboration

📂 Project Structure

extract_traffic.py — Connects to the selected public traffic API(s) and retrieves data

transform_data.py — Cleans, processes, and reshapes raw data using Pandas

load_to_bigquery.py — Uploads the final dataset to Google BigQuery

.env — Secure file storing API credentials (excluded from GitHub)

.gitignore — Prevents sensitive or unnecessary files from being committed

README.md — Full documentation for understanding and replicating the project

🚀 How to Use This Project

Clone the repository to your local machine.

Set up your .env file with any required API keys (if applicable).

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the ETL pipeline sequentially:

bash
Copy
Edit
python extract_traffic.py  
python transform_data.py  
python load_to_bigquery.py
Use BigQuery SQL to analyze traffic patterns, identify high-traffic regions, or visualize trends across time windows.
