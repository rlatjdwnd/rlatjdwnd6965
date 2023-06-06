import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

#데이터불러오기
investBM=pd.read_csv('EcoproBM.csv',parse_dates =["Date"]).set_index('Date').sort_index()
investHN=pd.read_csv('EcoproHN.csv',parse_dates =["Date"]).set_index('Date').sort_index()

#데이터 확인
investBM.info()
investHN.info()

#데이터 컬럼명 지정하고 바꿔주기
col_map_BM = {'Date' : 'Date_BM',
       'Price' : 'Price_BM',
       'Open' : 'Open_BM',
       'High' : 'High_BM',
       'Low' : 'Low_BM',
       'Vol.' : 'Vol._BM',
       'Change %' : 'Change %_BM'}
col_map_HN = {'Date' : 'Date_HN',
       'Price' : 'Price_HN',
       'Open' : 'Open_HN',
       'High' : 'High_HN',
       'Low' : 'Low_HN',
       'Vol.' : 'Vol._HN',
       'Change %' : 'Change %_HN'}
investBM= investBM.rename(columns=col_map_BM)
investHN= investHN.rename(columns=col_map_HN)

investBM.info()
investHN.info()

#데이터프레임 합치기
invest = pd.concat([investBM,investHN],axis=1)

invest.info()

#결측값 0으로 채우기 
invest.isna().sum()
invest = invest.fillna(0)

weekly_invest=
(
    invest.groupby(pd.Grouper(freq='W')).size()
)

weekly_invest

fig, ax = plt.subplots(figsize=(16,4))
weekly_invest.plot(title='Ecopro investing',ax=ax)

invest.columns

(
invest
.resample('Q')
[['Price_BM','Price_HN','Vol._BM','Vol._HN', 'Change %_BM', 'Change %_HN']]
.sum()
)

#BM과 HN의 가격 차이 
fig, ax = plt.subplots(figsize=(16,4))
(
    invest
    .resample('Q')
    [['Price_BM','Price_HN']]
    .sum()
    .plot(color=['black','blue'],ax=ax, title='invest')
)

#BM과 HN의 거래량 차이 
fig, ax = plt.subplots(figsize=(16,4))
(
    invest
    .resample('Qs')
    [['Vol._BM','Vol._HN']]
    .sum()
    .plot(color=['black','blue'],ax=ax, title='invest')
)

#BM과 HN의 변동량 차이 
fig, ax = plt.subplots(figsize=(16,4))
(
    invest
    .resample('Qs')
    [['Change %_BM','Change %_HN']]
    .sum()
    .plot(color=['black','blue'],ax=ax, title='invest')
)

invest_begin=(
    invest.resample('Q')
    [['Price_BM','Price_HN']]
    .sum()
    .iloc[0]
)

fig, ax = plt.subplots(figsize=(16,4))
(
    invest
    .resample('Q')
    [['Price_BM','Price_HN']]
    .sum()
    .div(invest_begin)
    .sub(1)
    .round(2)
    .plot.bar(color=['black','blue'],ax=ax)
)

invest_begin=(
    invest.resample('Q')
    [['Vol._BM','Vol._HN']]
    .sum()
    .iloc[0]
)

fig, ax = plt.subplots(figsize=(16,4))
(
    invest
    .resample('Q')
    [['Vol._BM','Vol._HN']]
    .sum()
    .div(invest_begin)
    .sub(1)
    .round(2)
    .plot.bar(color=['black','blue'],ax=ax)
)

invest_begin=(
    invest.resample('Q')
    [['Change %_BM','Change %_HN']]
    .sum()
    .iloc[0]
)

fig, ax = plt.subplots(figsize=(16,4))
(
    invest
    .resample('Q')
    [['Change %_BM','Change %_HN']]
    .sum()
    .div(invest_begin)
    .sub(1)
    .round(2)
    .plot.bar(color=['black','blue'],ax=ax)
)