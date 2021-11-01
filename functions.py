import pandas as pd
import numpy as np
import seaborn as sb
import pandas_datareader as pdr
import datetime
import matplotlib.pyplot as plt
import streamlit as st

#define start and end dates of data to be read into app
def dates(year, month, date):
    start = datetime.datetime(year, month, date)
    end = datetime.datetime.today()
    return start, end

#function to retrieve employment and unemployment data from FRED
def get_data(start, end):
    df_employed = pdr.DataReader('PAYEMS', 'fred', start, end)
    df_unemployment = pdr.DataReader('UNRATE', 'fred', start, end)
    return df_employed, df_unemployment

#modify the employment and unemployment data for analysis
def modify_data(df_employed, df_unemployment):
    df_employed['change'] = df_employed['PAYEMS'] - df_employed['PAYEMS'].shift(1)
    df_unemployment = df_unemployment.rename(columns = {'UNRATE':'Unemployment Rate'})
    df_employed['pct_change'] = (df_employed['PAYEMS'].pct_change(periods=12,
                             fill_method='bfill')*100).round(1)
    df_unemployment['change'] = df_unemployment['Unemployment Rate'] - df_unemployment['Unemployment Rate'].shift(1)

    print('{:+,} jobs created last month'.format(int(df_employed['change'][-1]*1000)))
    print('The unemployment Rate last month was {:}%'.format(df_unemployment['Unemployment Rate'][-1]))
    print('The unemployment rate changed by {:0.1f}% last month compared to the previous month.'.format(
          df_unemployment['change'][-1])) 
