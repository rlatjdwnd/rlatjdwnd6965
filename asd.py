import numpy as np
import pandas as pd


data1 = pd.read_csv('후성.csv',encoding='cp949',
                    dtype={
                     '날짜':'category',
                     '종가':np.int64,
                     '시가':np.int64,
                     '고가':np.int64,
                     '저가':np.int64,
                     '거래량': 'category',
                     '변동 %': 'category'
                    })

data2 = pd.read_csv('LG에너지솔루션.csv',encoding='cp949',
                    dtype={
                     '날짜':'category',
                     '종가':np.int64,
                     '시가':np.int64,
                     '고가':np.int64,
                     '저가':np.int64,
                     '거래량': 'category',
                     '변동 %': 'category'
                     })
data2.columns
data3 = pd.read_csv('엘앤에프.csv',encoding='cp949',
                    dtype={
                     '날짜':'category',
                     '종가':np.int64,
                     '시가':np.int64,
                     '고가':np.int64,
                     '저가':np.int64,
                     '거래량': 'category',
                     '변동 %': 'category'
                     })
data4 = pd.read_csv('코스모신소재.csv',encoding='cp949',
                    dtype={
                     '날짜':'category',
                     '종가':np.int64,
                     '시가':np.int64,
                     '고가':np.int64,
                     '저가':np.int64,
                     '거래량': 'category',
                     '변동 %': 'category'
                     })

col_map = {'날짜' : 'date',
       '종가' : 'close',
       '시가' : 'open',
       '고가' : 'high',
       '저가' : 'low',
       '거래량' : 'volume',
       '변동 %' : 'fluctuations'}

data=[data1,data2,data3,data4]
for i in range(0,4):
    data[i]=data[i].rename(columns=col_map)
    data[i].info() #데이터 타입 및 용량 확인
data1 = data1.rename(columns=col_map)

data1    
for i in range(0,4):
    data[i].isna().sum() #결측치확인
    data[i] = data[i].dropna() #거래량이 없는 것은 비교필요없기때문에 제거
