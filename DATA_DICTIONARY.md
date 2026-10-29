# Data dictionary and cleaning contract

Observation keys: fiscal_year for corporate history; location for FY25 datacenter clusters; (year,state) for EIA context. These are three separate tables with separate scopes.

| Field | Unit / meaning | Cleaning |
|---|---|---|
| fiscal_year | Microsoft FY ending June 30; integer | FY20 becomes 2020; not calendar year |
| electricity_mwh | MWh, annual electricity | Commas removed; not MW capacity or IT-only electricity |
| water_withdrawal_ml | ML drawn on site | 1 ML = 1,000,000 L = 1,000 m3 |
| water_consumption_ml | ML not discharged, corporate only | Preserve publisher restatements; reconcile withdrawal minus discharge |
| water_discharge_ml | ML discharged, corporate only | Never substitute for consumption |
| location | Metropolitan cluster, possibly multiple datacenters | ASCII spelling normalization; country standardized to United States |
| state | US two-letter state code | Explicit mapping; empty outside US |
| water_qualifier | reported / lt_1_ml | Auckland dash means <1 ML; keep numeric missing, not zero |
| withdrawal_l_per_kwh | L withdrawn / total electricity kWh | withdrawal_ml * 1000 / electricity_mwh; not WUE |
| year, sales_mwh | EIA calendar year, total retail MWh sold | Keep only Total Electric Industry; VA/IL/AZ/TX/WA; no summing provider subtotals |
| scope | Population and period boundary | Required in processed Microsoft tables |

Manual numeric excerpts come from Tables 5, 8, and 15; the PDF extraction is checked visually because extra columns (pool equivalents, non-potable share, replenishment) can be mistaken for withdrawals. Source rows are retained without outlier deletion. Annual history is from one 2026 vintage, not stitched across reports. Auckland has a bounded intensity 0 <= intensity < 1000/19465 L/kWh, not an estimated point. No missing values are imputed. No joining fiscal-year location values to calendar-year EIA sales for a percentage share.
