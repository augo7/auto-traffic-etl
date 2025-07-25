<<<<<<< HEAD
🚦 Auto Traffic ETL: Scalable Pipeline with Python & BigQuery
This project showcases a real-world ETL (Extract, Transform, Load) pipeline that ingests, cleans, and analyzes public traffic and urban mobility data. By integrating open data sources (such as Austin Open Data, NYC Mobility APIs, or Google Maps Traffic Layer) with Python’s robust data processing capabilities and Google BigQuery’s scalable cloud infrastructure, this pipeline is purpose-built for uncovering traffic patterns, bottlenecks, and regional mobility trends.

Through modular design, cloud integration, and automation, this project lays the foundation for continuous data operations, urban analytics, and smart city initiatives.

🔍 Project Highlights
🔗 Public API Integration
Extracts real-time or historical traffic data (CSV or JSON) from open datasets and mobility APIs. Supports dynamic querying and geo-based filtering.

🧹 Data Cleaning & Transformation
Uses pandas to handle missing timestamps, fix malformed records, normalize time zones, and extract day/time indicators. Optionally clusters data by intersection, region, or traffic zone.

🏗️ BigQuery Integration
Loads structured traffic datasets into BigQuery for fast querying, visualization, and scalable storage. Ideal for time-series or spatial analysis.

📊 Analytical Capabilities
Enables complex SQL queries to detect:

Traffic volume trends over time

Peak congestion hours per region/street

Comparisons across neighborhoods

Percent change calculations using SQL window functions

🛠️ Technologies & Tools
Technology	Purpose
Python	Core language for scripting & ETL logic
Pandas	Data wrangling, time-based grouping
BigQuery	Cloud-based data warehouse for querying
Public Traffic APIs	Source of real-time or archived mobility data
GitHub/Git	Version control and collaboration
dotenv	Securely manage API credentials
GitHub Actions / cron	Automate ETL execution

📂 Project Structure
bash
Copy
Edit
auto-traffic-etl/
├── extract_data.py         # API calls to fetch traffic/mobility data
├── transform_data.py       # Data cleaning & timestamp/region normalization
├── load_to_bigquery.py     # Loads processed data into BigQuery tables
├── scheduler.yaml          # GitHub Actions workflow for automatic ETL
├── .env                    # Stores API keys (excluded from version control)
├── .gitignore              # Prevents secrets and cache files from being pushed
├── README.md               # Project documentation
└── requirements.txt        # Dependencies (pandas, google-cloud-bigquery, etc.)
🚀 How to Use
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/auto-traffic-etl.git
cd auto-traffic-etl
Configure your API credentials in a .env file:

env
Copy
Edit
API_KEY=your_api_key
PROJECT_ID=your_gcp_project_id
DATASET_NAME=traffic_data
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the ETL pipeline sequentially:

bash
Copy
Edit
python extract_data.py
python transform_data.py
python load_to_bigquery.py
Automate with GitHub Actions or cron:

Modify scheduler.yaml to define how often the ETL runs (e.g., daily at midnight)

Push the workflow to your GitHub repo’s .github/workflows/ directory

GitHub will automatically execute the pipeline on your defined schedule
(alternatively, use a local cron job for on-premise scheduling)

Analyze the data in BigQuery using SQL:
Examples:

Identify the top 10 most congested intersections by hour

Rank neighborhoods by traffic increase over time

Use LAG() and PARTITION BY to calculate weekly traffic percent change

👨‍💻 About Me
I am a passionate Computer Science student attending Texas State University, actively building expertise in data analytics and engineering. This project is a part of my journey of hands-on experience with APIs, data transformation, cloud platforms, and secure coding practices — foundational skills essential for modern data-driven organizations.
