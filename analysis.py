"""Offline descriptive analysis. Paths are relative to this file, not the shell."""
from pathlib import Path
import json
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent

def withdrawal_intensity(water_ml, electricity_mwh):
    water=np.asarray(water_ml,dtype=float); energy=np.asarray(electricity_mwh,dtype=float)
    if not np.isfinite(energy).all() or (energy<=0).any():
        raise ValueError('Electricity must be finite and positive')
    if np.isinf(water).any() or (water<0).any():
        raise ValueError('Water must be nonnegative; NaN is allowed for censored values')
    return water*1000/energy  # ML*1e6 L / (MWh*1000 kWh)

def load_clean():
    annual=pd.read_csv(ROOT/'data/raw/microsoft_annual.csv')
    sites=pd.read_csv(ROOT/'data/raw/microsoft_locations_fy25.csv')
    if annual.fiscal_year.duplicated().any() or sites.location.duplicated().any():
        raise ValueError('Duplicate observation keys')
    for frame in (annual,sites):
        frame['withdrawal_l_per_kwh']=withdrawal_intensity(frame.water_withdrawal_ml,frame.electricity_mwh)
    if not np.allclose(annual.water_withdrawal_ml-annual.water_discharge_ml,annual.water_consumption_ml,atol=1):
        raise ValueError('Corporate water balance does not reconcile')
    annual['scope']='Microsoft global corporate operations; fiscal year'
    sites['scope']='Microsoft owned operated datacenter location clusters; FY25'
    return annual,sites

def cooling_scenarios(it_mwh=1000):
    # Scenario inputs, not measured Microsoft performance; overhead includes more than cooling.
    if not np.isfinite(it_mwh) or it_mwh<=0: raise ValueError('Positive IT energy required')
    pue=np.array([1.1,1.2,1.4,1.6])
    return pd.DataFrame({'pue_assumption':pue,'it_mwh':it_mwh,'facility_mwh':it_mwh*pue,'non_it_mwh':it_mwh*(pue-1)})

def run():
    report=ROOT/'reports'; report.mkdir(exist_ok=True)
    processed=ROOT/'data/processed'; processed.mkdir(exist_ok=True)
    annual,sites=load_clean()
    annual.to_csv(processed/'annual.csv',index=False); sites.to_csv(processed/'locations.csv',index=False)
    plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
    colors=['#087e8b','#c65d32','#70528d']
    fig,ax=plt.subplots(figsize=(9,5))
    for col,label,c in zip(['electricity_mwh','water_withdrawal_ml','water_consumption_ml'],['Electricity','Water withdrawal','Water consumption'],colors):
        ax.plot(annual.fiscal_year,annual[col]/annual[col].iloc[0]*100,'o-',label=label,color=c)
    ax.set(title='Microsoft corporate resource growth',xlabel='Fiscal year (2026 fact-sheet vintage)',ylabel='Index: FY20 = 100')
    ax.legend(); fig.text(.01,.01,'Source: Microsoft 2026 Data Fact Sheet, Tables 5 and 8. Corporate scope; restated history.',fontsize=8)
    fig.tight_layout(rect=(0,.04,1,1)); fig.savefig(report/'resource_growth.png',dpi=160); plt.close(fig)
    ranked=sites.dropna(subset=['withdrawal_l_per_kwh']).sort_values('withdrawal_l_per_kwh')
    fig,ax=plt.subplots(figsize=(10,8))
    ax.barh(ranked.location,ranked.withdrawal_l_per_kwh,color='#087e8b')
    ax.set(title='FY25 owned datacenter locations: withdrawal intensity',xlabel='Liters withdrawn / kWh of total facility electricity')
    fig.text(.01,.01,'Microsoft Table 15; Auckland omitted (<1 ML). Ratios are not WUE or cooling-efficiency scores.',fontsize=8)
    fig.tight_layout(rect=(0,.035,1,1)); fig.savefig(report/'location_intensity.png',dpi=160); plt.close(fig)
    scenario=cooling_scenarios(); scenario.to_csv(processed/'cooling_scenarios.csv',index=False)
    fig,ax=plt.subplots(figsize=(8,4.5))
    ax.bar(scenario.pue_assumption.astype(str),scenario.it_mwh,label='IT',color='#087e8b')
    ax.bar(scenario.pue_assumption.astype(str),scenario.non_it_mwh,bottom=scenario.it_mwh,label='Non-IT overhead',color='#c65d32')
    ax.set(title='Illustrative PUE sensitivity: fixed 1,000 MWh IT workload',xlabel='Assumed PUE',ylabel='Facility energy (MWh)'); ax.legend()
    fig.tight_layout(); fig.savefig(report/'cooling_scenarios.png',dpi=160); plt.close(fig)
    eia=pd.read_csv(ROOT/'data/raw/eia_regional_sales.csv')
    fig,ax=plt.subplots(figsize=(8,4.5))
    for state,g in eia.groupby('state'):
        ax.plot(g.year,g.sales_mwh/1e6,label=state)
    ax.set(title='Regional context: total retail electricity sales',xlabel='Calendar year',ylabel='TWh (all end-use sectors)'); ax.legend()
    fig.text(.01,.01,'Source: EIA annual state sales workbook; all providers total. Not datacenter-only demand.',fontsize=8)
    fig.tight_layout(rect=(0,.04,1,1)); fig.savefig(report/'regional_sales.png',dpi=160); plt.close(fig)
    growth={c:float((annual[c].iloc[-1]/annual[c].iloc[0]-1)*100) for c in ['electricity_mwh','water_withdrawal_ml','water_consumption_ml']}
    result={'fy20_to_fy25_growth_percent':growth,'location_rows':len(sites),'censored_water_rows':int(sites.water_withdrawal_ml.isna().sum()),'regional_context_years':[int(eia.year.min()),int(eia.year.max())],'ml_status':'No model fitted: descriptive aggregate evidence only'}
    (report/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    return result

if __name__=='__main__': print(json.dumps(run(),indent=2))
