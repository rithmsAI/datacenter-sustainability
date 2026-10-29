# Provenance and reuse

Accessed 2026-10-29. Machine-readable source registry: data/sources.json. It preserves original URLs, period/scope, source locators, retrieval dates, SHA-256 hashes for downloaded Microsoft and EIA files, and reuse status. The numeric CSV excerpts and cleaning code are versionable inputs. A hash verifies the exact downloaded vintage; it does not establish accuracy or a license.

## Microsoft

[2026 report landing page](https://www.microsoft.com/en-us/corporate-responsibility/topics/sustainability/report/) links to the [2026 Environmental Data Fact Sheet](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf). Tables 5/8 supply corporate energy/water (printed pp6/7); Table 15 supplies datacenter locations (p25); definitions are on p26. Values were transcribed into numeric excerpts and visually checked against rendered tables. No explicit open-data license was identified: public availability is not an open license. The full corporate PDF is not redistributed in this package. Retain attribution and verify terms before redistributing more source material. Microsoft retains rights in its report.

The 2026 sheet reports FY25 and restates earlier years. Its corporate boundary includes operational changes/acquisitions; do not interpret growth as purely AI-driven. Table 15 covers owned datacenters under management/operational control, with specified exclusions; it is not all leased capacity. Section 2 (including location data) is outside Deloitte's review. Some water values use estimates informed by electricity/cooling technology, which limits independent correlation claims. Auckland's dash means <1 ML, not zero. Water consumption is available for corporate totals, not for individual Table 15 locations. Replenishment is not subtracted from withdrawals.

## EIA regional context

[Current historical-state data page](https://www.eia.gov/electricity/data/state/) links to [HS861 2010- workbook](https://www.eia.gov/electricity/data/state/xls/861/HS861%202010-.xlsx), released October 7, 2026, final annual data through 2025. Use Total Electric Industry, TOTAL Sales (MWh), five states, 2010-2025. The original public-domain workbook is included. Rebuild the extracted CSV with `python scripts/extract_eia.py`. Follow [EIA reuse guidance](https://www.eia.gov/about/copyrights_reuse.php), acknowledge publisher/date, and preserve third-party exceptions.

Older guessed filenames sales_annual.xlsx and sales_annual.xls returned stale datasets ending 2020 and 2014; neither is an input to the final analysis. Do not infer vintage from a filename. This project checks actual headers, years, unique keys and units. State total sales are context only; no Microsoft share is calculated across fiscal and calendar years.

## DOE / LBNL context

Smith, S.J. et al. (2026), [United States Data Center Energy Usage Report: 2025 Update](https://www.energy.gov/documents/united-states-data-center-energy-usage-report-2025-update), LBNL-2001758, [DOI](https://doi.org/10.71468/P1RP4F). CC BY 4.0 is stated on the eScholarship cover. It estimates 192 TWh for 2024 and national aggregate PUE of 1.55 in 2018 and 1.45 in 2024. These contextual estimates remain separate from Microsoft observations; full underlying inputs include proprietary market data. This June 2026 publication is newer than the December 2024 report. Never splice older estimates into its revised series without labeling vintages.

## Reproduction boundary

Offline reproduction regenerates derived tables/charts from the shipped source excerpts. It does not independently reproduce publishers' estimates. To audit transcription, fetch the original PDF, compare its SHA-256 to sources.json, and inspect the cited tables and definitions. There is no automated PDF parser pretending that visually ambiguous columns are reliable. Neither project selects a blanket open-source/data license for you.
