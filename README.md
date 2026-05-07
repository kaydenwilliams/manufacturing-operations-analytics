# Manufacturing Operations Analysis

## Overview
A manufacturer exports data from three ERP systems — production logs, defect reports, and downtime incidents. The goal is to identify which factories underperform, what causes defects, and where production time is being lost.

## Tools
Python, pandas, Tableau

## Dataset
Three synthetic ERP export CSVs with intentional data quality issues:
- production_log.csv — 1,860 rows — daily production output per factory per product line
- defect_log.csv — 1,245 rows — defect reports per batch per factory
- downtime_log.csv — 935 rows — downtime incidents per factory

## Data Cleaning
Raw files contained mixed date formats (4 variations), inconsistent factory name formats, duplicates, numbers stored as text, impossible values (negative production output, downtime over 24 hours), missing values in critical columns, and inconsistent capitalization throughout.

## Business Questions
1. Which factories underperform?
2. What causes defects?
3. Where is production time being lost?

## Key Findings
- Factory D is the clear underperformer — lowest production output at 102 avg daily units vs 252–257 for top factories, highest defect rate at 17.3% (3x the 5.6% avg of other factories), and most downtime at 1,347 hours — more than double every other factory
- Material Defect (3,564) and Assembly Error (3,344) are the leading defect causes across all factories
- Equipment Failure drives the most downtime at 690 hours across 155 incidents, with Scheduled Maintenance close behind at 681 hours across 153 incidents

## File Structure
manufacturing-operations-analytics/
├── data/
│   ├── raw/
│   └── cleaned/
├── clean.py
├── explore.py
├── analysis.py
├── executive_summary.pdf
└── README.md

**Tableau Dashboard**
https://public.tableau.com/app/profile/kayden.williams2622/viz/ManufacturingOperationsDashboard/Dashboard1

## Business Recommendations
- Factory D: prioritize an operational audit of Factory D before increasing production targets. Running more units through a factory with a 17.3% defect rate will generate more defective output, not more good output. Fix the defect problem first.
- Defects: Material Defect and Assembly Error together account for nearly 47% of all defects. Investigate supplier quality for materials and review assembly line training and procedures. These are two different root causes requiring two different interventions.
- Equipment: Equipment Failure is the top unplanned downtime cause at 690 hours across 155 incidents. Recommend a preventive maintenance schedule to catch failures before they cause downtime. Scheduled Maintenance at 681 hours is already planned — the goal is to shift more downtime from unplanned to planned.
- Factory C: defect rate of 16.6% is nearly as bad as Factory D but production output is the highest. That means Factory C is producing a lot of defective units. Flag this as a secondary priority.
