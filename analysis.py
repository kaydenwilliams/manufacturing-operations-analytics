import pandas as pd

cleaned_defect_log = pd.read_csv('data/cleaned/cleaned_defect_log.csv')
cleaned_downtime_log = pd.read_csv('data/cleaned/cleaned_downtime_log.csv')
cleaned_production_log = pd.read_csv('data/cleaned/cleaned_production_log.csv')

# Business Question 1: Which factories underperform?
# Total and average daily units produced per factory to identify low performers
factory_output = cleaned_production_log.groupby('factory').agg(
    Units_Per_Factory=('units_produced', 'sum'),
    Avg_Daily_Units=('units_produced', 'mean')
).sort_values('Units_Per_Factory', ascending=False)
print(factory_output)

# Business Question 2: What causes defects?
# Total defect count grouped by defect reason
defect_causes = cleaned_defect_log.groupby('defect_reason').agg(
    Count_by_Reason=('defect_count', 'sum')
).sort_values('Count_by_Reason', ascending=False)
print(defect_causes)

# Calculate defect rate per row as a percentage of batch size
cleaned_defect_log['defect_rate'] = cleaned_defect_log['defect_count'] / cleaned_defect_log['batch_size'] * 100

# Average defect rate by factory to identify which factories have the worst quality
defect_rate = cleaned_defect_log.groupby('factory').agg(
    Avg_Defect_Rate=('defect_rate', 'mean')
).sort_values('Avg_Defect_Rate', ascending=False)
print(defect_rate)

# Business Question 3: Where is production time being lost?
# Total downtime hours and incident count by cause to identify the biggest sources of lost time
downtime_by_cause = cleaned_downtime_log.groupby('cause').agg(
    Hours_by_Cause=('downtime_hours', 'sum'),
    Incidents_per_Cause=('downtime_hours', 'count')
).sort_values('Hours_by_Cause', ascending=False)
print(downtime_by_cause)

# Total downtime hours by factory
downtime_by_factory = cleaned_downtime_log.groupby('factory').agg(
    Downtime_by_Factory=('downtime_hours', 'sum')
).sort_values('Downtime_by_Factory', ascending=False)
print(downtime_by_factory)