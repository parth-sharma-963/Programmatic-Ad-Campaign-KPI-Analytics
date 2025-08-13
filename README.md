<<<<<<< HEAD
KPI Analytics Project
Overview
This project performs data analysis on programmatic ad campaigns to measure campaign performance and uncover insights for improving ROI. It leverages PySpark for data processing, Pandas for analysis, and statistical methods and visualizations to derive actionable conclusions.

Features
Load campaign data from CSV files.

Compute Key Performance Indicators (KPIs):

CTR (Click-Through Rate)

CPC (Cost per Click)

CPM (Cost per Thousand Impressions)

Conversion Rate

ROI (Return on Investment)

Conduct A/B testing to compare CTR between Mobile and Desktop campaigns.

Perform OLS regression to identify which KPIs drive ROI.

Generate visualizations:

Average CTR by location

Average ROI by device type

Requirements
Python 3.12+

PySpark

Pandas

SciPy

Statsmodels

Matplotlib

Java JDK 17 (for PySpark)

Installation
Clone the repository:

bash
Copy
Edit
git clone <your-repo-url>
cd MiQ
Create and activate a virtual environment:

bash
Copy
Edit
python3 -m venv env
source env/bin/activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Ensure Java 17 is installed and available:

bash
Copy
Edit
brew install openjdk@17
export JAVA_HOME="/opt/homebrew/opt/openjdk@17"
export PATH="$JAVA_HOME/bin:$PATH"
Usage
Place your input CSV files in the project directory:

programmatic_ad_campaigns.csv

kpi_results.csv (optional)

Run the analysis script:

bash
Copy
Edit
python connector.py
Output:

KPIs calculated and saved via PySpark.

A/B test results (CTR: Mobile vs Desktop).

Regression analysis results identifying ROI drivers.

Charts saved as PNG images in the project folder.

Project Structure
graphql
Copy
Edit
MiQ/
│
├─ connector.py          # Main analysis script
├─ programmatic_ad_campaigns.csv  # Input campaign data
├─ kpi_results.csv       # Optional historical KPI data
├─ ctr_by_location.png   # Visualization output
├─ roi_by_device.png     # Visualization output
└─ requirements.txt      # Python dependencies
Insights & Results
CTR Comparison (Mobile vs Desktop): No statistically significant difference.

ROI Regression:

CTR and ConversionRate positively impact ROI.

CPM slightly reduces ROI.

CPC not significant.

Visualizations provide quick insights into top-performing locations and devices.

Skills Demonstrated
PySpark data processing

Pandas data cleaning

Statistical testing (A/B testing, t-test)

Regression modeling with Statsmodels

Data visualization with Matplotlib

End-to-end analytical workflow for marketing data

Author
Parth Sharma

=======
# Programmatic-Ad-Campaign-KPI-Analytics
>>>>>>> 5e63473cda2d9147b6870812ac551e3891d470ed
