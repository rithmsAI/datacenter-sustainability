# First findings: growth, boundaries and uncertainty

Research question: what do public disclosures show about resource growth and location variation, and what can they support about sustainable infrastructure?

Microsoft corporate electricity rose from 10.77 million MWh in FY20 to 37.03 million MWh in FY25 (+243.8%). Water withdrawal rose from 6,794 to 13,266 ML (+95.3%); consumption rose from 3,990 to 8,170 ML (+104.8%). These are the 2026 fact sheet's restated corporate values, not a datacenter-only or AI-only series. Consumption equals withdrawals minus discharge in each annual row. Use the growth chart to compare relative changes while retaining separate units in the source table.

Corporate withdrawal per total electricity kWh decreases over this interval, even while absolute withdrawals increase. This is a descriptive ratio across changing operations. It is not WUE, proof of improved cooling, or a causal estimate of AI's impact.

The FY25 owned-datacenter disclosure contains 29 location clusters. Auckland's withdrawal is censored below 1 ML; the point ratio is left missing. Across the other 28 clusters, withdrawal intensity varies widely. Jakarta is about 3.79 L/kWh; Dublin about 0.014 L/kWh. These ratios are sensitive to climate, cooling, utilization, scope, estimates and small denominators. They do not identify the most sustainable location. Some underlying water estimates themselves use electricity and cooling type, so correlation between published columns is not independent validation.

Illustrative PUE scenarios show that a fixed 1,000 MWh IT workload needs 1,100 MWh at PUE 1.1 versus 1,600 MWh at PUE 1.6. The 500 MWh difference is total non-IT overhead difference, not a measured cooling saving. Lower PUE can coexist with increased total demand if IT workload grows.

EIA provides 80 calendar-year observations for AZ, IL, TX, VA and WA, 2010-2025. These are all-sector retail sales. The chart describes regional scale and trends; it does not attribute growth to datacenters or combine fiscal and calendar data into a Microsoft market share. LBNL context is kept in its own table and does not fill missing Microsoft values.

No ML model is fitted. A small aggregate panel cannot credibly support a cooling predictor. A future study needs measured facility-month IT energy, water consumption, source mix, weather, cooling type and local water-stress data, with temporal and geographic holdouts. Embodied hardware emissions, lifetime/reuse, upstream electricity water impacts and grid constraints are part of the sustainability question but are not quantified in this release.

Sources: Microsoft 2026 Environmental Data Fact Sheet, Tables 5, 8, 15 and definitions p26; EIA HS861 (October 7, 2026 release); Smith et al. 2026 LBNL-2001758. Full links, rights status, source hashes and exclusions: ../SOURCES.md and ../data/sources.json. Calculations: ../analysis.py; inputs: ../data/raw/; generated results: results.json. Nine tests pass and the notebook was executed on 2026-10-29.
