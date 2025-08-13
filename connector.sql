/usr/local/mysql-9.3.0-macos15-arm64/bin/mysql --local-infile=1 -u root -p --batch -e "
USE ad_analytics;
SELECT 'campaign_id','location','device','CTR','CPC','CPM','ConversionRate','ROI'
UNION ALL
SELECT campaign_id, location, device,
       ROUND(SUM(clicks) / SUM(impressions), 4),
       ROUND(SUM(cost) / NULLIF(SUM(clicks), 0), 4),
       ROUND((SUM(cost) / SUM(impressions)) * 1000, 4),
       ROUND(SUM(conversions) / NULLIF(SUM(clicks), 0), 4),
       ROUND((SUM(revenue) - SUM(cost)) / NULLIF(SUM(cost), 0), 4)
FROM campaigns
GROUP BY campaign_id, location, device;
" | sed 's/\t/,/g' > /Users/parthsharma/Downloads/MiQ/kpi_results.csv
