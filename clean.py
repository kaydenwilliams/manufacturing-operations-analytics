import pandas as pd

defect_log = pd.read_csv('data/raw/defect_log.csv')
downtime_log = pd.read_csv('data/raw/downtime_log.csv')
production_log = pd.read_csv('data/raw/production_log.csv')

# Standardize factory names across all files
defect_log['factory'] = defect_log['factory'].str.strip().str.lower()
downtime_log['factory'] = downtime_log['factory'].str.strip().str.lower()
production_log['factory'] = production_log['factory'].str.strip().str.lower()

factory_map = {
    'factory a': 'Factory A', 'factory_a': 'Factory A', 'fac-a': 'Factory A',
    'factory b': 'Factory B', 'factory_b': 'Factory B', 'fac-b': 'Factory B',
    'factory c': 'Factory C', 'factory_c': 'Factory C', 'fac-c': 'Factory C',
    'factory d': 'Factory D', 'factory_d': 'Factory D', 'fac-d': 'Factory D',
    'factory e': 'Factory E', 'factory_e': 'Factory E', 'fac-e': 'Factory E'
}

defect_log['factory'] = defect_log['factory'].map(factory_map)
downtime_log['factory'] = downtime_log['factory'].map(factory_map)
production_log['factory'] = production_log['factory'].map(factory_map)

# Standardize resolved column to Yes/No
downtime_log['resolved'] = downtime_log['resolved'].str.strip().str.lower()
resolved_map = {'yes': 'Yes', 'no': 'No'}
downtime_log['resolved'] = downtime_log['resolved'].map(resolved_map)

# Parse mixed date formats to datetime
defect_log['date'] = pd.to_datetime(defect_log['date'], dayfirst=True, format='mixed')
downtime_log['date'] = pd.to_datetime(downtime_log['date'], dayfirst=True, format='mixed')
production_log['date'] = pd.to_datetime(production_log['date'], dayfirst=True, format='mixed')

# Remove duplicate rows
defect_log = defect_log.drop_duplicates()
downtime_log = downtime_log.drop_duplicates()
production_log = production_log.drop_duplicates()

# Strip text suffix and convert units_produced to numeric
production_log['units_produced'] = production_log['units_produced'].astype(str).str.replace(' units', '', regex=False).str.strip()
production_log['units_produced'] = pd.to_numeric(production_log['units_produced'], errors='coerce')

# Remove impossible values
production_log = production_log[production_log['units_produced'] >= 0]
downtime_log = downtime_log[downtime_log['downtime_hours'] <= 24]

# Drop rows missing critical columns
defect_log = defect_log.dropna(subset=['factory', 'defect_count'])
downtime_log = downtime_log.dropna(subset=['factory', 'downtime_hours', 'cause'])
production_log = production_log.dropna(subset=['factory', 'units_produced'])

# Standardize capitalization in categorical columns
defect_log['defect_reason'] = defect_log['defect_reason'].str.title()
downtime_log['cause'] = downtime_log['cause'].str.title()
production_log['shift'] = production_log['shift'].str.title()

# Export cleaned files
defect_log.to_csv('data/cleaned/cleaned_defect_log.csv', index=False)
downtime_log.to_csv('data/cleaned/cleaned_downtime_log.csv', index=False)
production_log.to_csv('data/cleaned/cleaned_production_log.csv', index=False)