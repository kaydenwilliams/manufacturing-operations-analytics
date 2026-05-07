import pandas as pd

defect_log = pd.read_csv('defect_log.csv')
downtime_log = pd.read_csv('downtime_log.csv')
production_log = pd.read_csv('production_log.csv')

print(defect_log.shape)
print(downtime_log.shape)
print(production_log.shape)

print(defect_log.columns.tolist())
print(downtime_log.columns.tolist())
print(production_log.columns.tolist())

print(defect_log.head())
print(downtime_log.head())
print(production_log.head())