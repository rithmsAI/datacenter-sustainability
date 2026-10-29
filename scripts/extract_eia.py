from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def extract():
    raw=pd.read_excel(ROOT/'data/raw/eia_hs861_source.xlsx',sheet_name='Total Electric Industry',header=None)
    if raw.iloc[1,19]!='Sales' or raw.iloc[2,19]!='Megawatthours': raise ValueError('Source schema changed')
    data=raw.iloc[3:,[0,1,19]].copy(); data.columns=['year','state','sales_mwh']
    data.year=pd.to_numeric(data.year,errors='coerce')
    data=data[data.state.isin(['VA','IL','AZ','TX','WA']) & data.year.ge(2010)].copy()
    data.year=data.year.astype(int); data.sales_mwh=pd.to_numeric(data.sales_mwh,errors='raise')
    if data.duplicated(['year','state']).any() or not data.sales_mwh.gt(0).all(): raise ValueError('Invalid observations')
    if data.year.max()!=2025 or len(data)!=80: raise ValueError('Unexpected source vintage or completeness')
    return data.sort_values(['state','year']).reset_index(drop=True)
if __name__=='__main__': extract().to_csv(ROOT/'data/raw/eia_regional_sales.csv',index=False)
