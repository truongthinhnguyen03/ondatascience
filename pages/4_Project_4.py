import streamlit as st
import pandas as pd
import wbgapi as wb
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import math

st.set_page_config(
    page_title="ThinhNT Portfolio / Project 4",
    page_icon="chart_with_upwards_trend",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
# World Development Indicators

This app explore the World Development Indicators dataset from United Nations
""")

# search_query = st.text_input('Search for indicators, countries, and more')
# search_result = wb.search(search_query)
# st.write(search_result)

def get_data_from_list(indicators):
    indicator_list = pd.DataFrame.from_records(wb.series.info(indicators).items)\
                                               .sort_values('id').reset_index(drop=True)
    data = wb.data.DataFrame(indicator_list['id'], 'VNM',
                             skipBlanks=True, numericTimeKeys=False, columns='series')
    data.index = pd.to_datetime(data.index, format='YR%Y').strftime('%Y')
    return indicator_list, data

def make_subplot_from_list(indicators):
    indicator_list, data = get_data_from_list(indicators)

    ncol = 2
    nrow = math.ceil(len(indicators) / ncol)
    row, col = 1, 1

    fig = make_subplots(rows=nrow, cols=ncol, subplot_titles=indicator_list['value'])
    for i in range(len(indicators)):
        fig.add_trace(go.Line(x=data.index, y=data[indicators[i]],
                              mode='lines+markers', name=data.columns[i]),
                      row=row, col=col)
        col += 1
        if col > ncol:
            col = 1
            row += 1

    fig.update_layout(height=300*nrow, showlegend=False)
    return data, fig

# Growth and economic structure ------------------------------------------------------------------

growth_economic_structure = [
'NY.GDP.MKTP.CD' # GDP (current US$)     	      	
, 'NY.GDP.MKTP.KD.ZG' # GDP growth (annual %)	     	      	
, 'NV.AGR.TOTL.KD.ZG' # Agriculture, value added (annual % growth)
, 'NV.IND.TOTL.KD.ZG' # Industry, value added (annual % growth)	     	      	
, 'NV.IND.MANF.KD.ZG' # Manufacturing, value added (annual % growth)
, 'NV.SRV.TOTL.KD.ZG' # Services, value added (annual % growth)
, 'NE.CON.TOTL.KD.ZG' # Final consumption expenditure (annual % growth)
, 'NE.GDI.TOTL.KD.ZG' # Gross capital formation (annual % growth)
, 'NE.EXP.GNFS.KD.ZG' # Exports of goods and services (annual % growth)
, 'NE.IMP.GNFS.KD.ZG' # Imports of goods and services (annual % growth)
, 'NV.AGR.TOTL.ZS' # Agriculture, value added (% of GDP)
, 'NV.IND.TOTL.ZS' # Industry, value added (% of GDP)
, 'NV.SRV.TOTL.ZS' # Services, value added (% of GDP)
, 'NE.CON.TOTL.ZS' # Final consumption expenditure (% of GDP)
, 'NE.GDI.TOTL.ZS' # Gross capital formation (% of GDP)
, 'NE.EXP.GNFS.ZS' # Exports of goods and services (% of GDP)
, 'NE.IMP.GNFS.ZS' # Imports of goods and services (% of GDP)
]

data, fig = make_subplot_from_list(growth_economic_structure)

st.markdown("""
## Vietnam Growth & Economic structure
""")

with st.expander('Table data'):
    st.dataframe(data)

st.plotly_chart(fig, use_container_width=True)



# # Income & Savings ------------------------------------------------------------------

income_savings = [
'NY.GNP.PCAP.CD' # GNI per capita, Atlas method (current US$)
, 'NY.GNP.PCAP.PP.CD' # GNI per capita, PPP (current international $)
, 'SP.POP.TOTL' # Population, total
, 'NY.GNS.ICTR.ZS' # Gross savings (% of GDP) 	      	
, 'NY.ADJ.SVNG.GN.ZS' # Adjusted net savings, including particulate emission damage (% of GNI)
]

data, fig = make_subplot_from_list(income_savings)

st.markdown("""
## Vietnam Income & Savings
""")

with st.expander('Table data'):
    st.dataframe(data)

st.plotly_chart(fig, use_container_width=True)

# Balance of payments ------------------------------------------------------------------

balance_payments = [
'TX.VAL.MRCH.XD.WD' # Export value index (2000 = 100)
, 'TM.VAL.MRCH.XD.WD' # Import value index (2000 = 100)
, 'BX.TRF.PWKR.DT.GD.ZS' # Personal remittances, received (% of GDP)
, 'BN.CAB.XOKA.GD.ZS' # Current account balance (% of GDP)
, 'BX.KLT.DINV.WD.GD.ZS' # Foreign direct investment, net inflows (% of GDP)
]

data, fig = make_subplot_from_list(balance_payments)

st.markdown("""
## Vietnam Balance of Payments
""")

with st.expander('Table data'):
    st.dataframe(data)

st.plotly_chart(fig, use_container_width=True)

# Prices and terms of trade ------------------------------------------------------------------

prices_terms_of_trade = [
'FP.CPI.TOTL' # Consumer price index (2010 = 100)
, 'TX.UVI.MRCH.XD.WD' # Export unit value index (2000 = 100)
, 'TM.UVI.MRCH.XD.WD'	# Import unit value index (2000 = 100)
, 'TT.PRI.MRCH.XD.WD' # Net barter terms of trade index (2000 = 100)
]

data, fig = make_subplot_from_list(prices_terms_of_trade)

st.markdown("""
## Vietnam Prices & Terms of trade
""")

with st.expander('Table data'):
    st.dataframe(data)

st.plotly_chart(fig, use_container_width=True)

# Labor and productivity ------------------------------------------------------------------

labor_productivity =[
'SL.GDP.PCAP.EM.KD' # GDP per person employed (constant 2011 PPP $)
, 'SL.UEM.TOTL.ZS' # Unemployment, total (% of total labor force) (modeled ILO estimate)
, 'NV.AGR.EMPL.KD' # Agriculture, value added per worker (constant 2010 US$)
, 'NV.IND.EMPL.KD' # Industry, value added per worker (constant 2010 US$)
, 'NV.SRV.EMPL.KD' # Services, value added per worker (constant 2010 US$)
]

data, fig = make_subplot_from_list(labor_productivity)

st.markdown("""
## Vietnam Labor and Productivity
""")

with st.expander('Table data'):
    st.dataframe(data)

st.plotly_chart(fig, use_container_width=True)