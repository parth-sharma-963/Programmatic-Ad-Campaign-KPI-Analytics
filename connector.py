from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as _sum, round as _round
import pandas as pd
from scipy import stats
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Initialize Spark
spark = SparkSession.builder \
    .appName("MIQ_KPI_Analytics") \
    .config("spark.driver.extraClassPath", "/path/to/mysql-connector-j-9.0.0.jar") \
    .getOrCreate()

# Read CSV with Spark
df_spark = spark.read.csv(
    "/Users/parthsharma/Downloads/MiQ/programmatic_ad_campaigns.csv",
    header=True,
    inferSchema=True
)

# Compute KPIs
kpi_df = df_spark.groupBy("campaign_id", "location", "device").agg(
    _round(_sum("clicks") / _sum("impressions"), 4).alias("CTR"),
    _round(_sum("cost") / _sum("clicks"), 4).alias("CPC"),
    _round((_sum("cost") / _sum("impressions")) * 1000, 4).alias("CPM"),
    _round(_sum("conversions") / _sum("clicks"), 4).alias("ConversionRate"),
    _round((_sum("revenue") - _sum("cost")) / _sum("cost"), 4).alias("ROI")
)

# Save KPI results (Spark requires a folder, not a single CSV file)
kpi_output_path = "/Users/parthsharma/Downloads/MiQ/kpi_results_spark"
kpi_df.coalesce(1).write.csv(kpi_output_path, header=True, mode="overwrite")

# Convert to Pandas for stats & plotting
df = kpi_df.toPandas()
numeric_cols = ['CTR', 'CPC', 'CPM', 'ConversionRate', 'ROI']
df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

print("✅ Data processed with PySpark")
print(df.head())

# A/B Test — CTR (Mobile vs Desktop)
mobile_ctr = df[df['device'] == 'Mobile']['CTR']
desktop_ctr = df[df['device'] == 'Desktop']['CTR']

t_stat, p_val = stats.ttest_ind(mobile_ctr, desktop_ctr, equal_var=False)
print("\n📊 A/B Test — CTR (Mobile vs Desktop)")
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_val:.4f}")
if p_val < 0.05:
    print("✅ Significant difference in CTR between Mobile and Desktop.")
else:
    print("❌ No significant difference in CTR between Mobile and Desktop.")

# Regression — ROI drivers
X = df[['CTR', 'CPC', 'CPM', 'ConversionRate']]
y = df['ROI']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
print("\n📈 Regression Results — ROI drivers")
print(model.summary())

# Visualization — CTR by Location
plt.figure(figsize=(10, 6))
df.groupby('location')['CTR'].mean().sort_values().plot(kind='bar')
plt.ylabel("Average CTR")
plt.title("Average CTR by Location")
plt.tight_layout()
plt.savefig("/Users/parthsharma/Downloads/MiQ/ctr_by_location_spark.png")
plt.close()

# Visualization — ROI by Device
plt.figure(figsize=(6, 4))
df.groupby('device')['ROI'].mean().plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
plt.ylabel("Average ROI")
plt.title("Average ROI by Device")
plt.tight_layout()
plt.savefig("/Users/parthsharma/Downloads/MiQ/roi_by_device_spark.png")
plt.close()

print("\n📂 Charts saved to /Users/parthsharma/Downloads/MiQ/")

# Stop Spark
spark.stop()
