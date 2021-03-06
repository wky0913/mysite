import tushare as ts
import pandas as pd
import numpy as np
import os
import pickle
import matplotlib.pyplot as plt

eps = {'2010':0,'2011':0,'2012':0,'2013':0,'2014':0,'2015':0,'2016':0,'2017':0,}


def get_eps(code):
    for i in range(2010,2017):
        if os.path.exists('/home/wk/wkfile/data'+str(i)+'.pkl'):
            with open('/home/wk/wkfile/data'+str(i)+'.pkl','rb') as f:
                data = pickle.load(f)
        else:
            data = ts.get_report_data(i,4)
            with open('/home/wk/wkfile/data'+str(i)+'.pkl','wb') as f:
                pickle.dump(data,f)
        if str(i) in eps.keys():
            eps[str(i)] = data[ data['code'] == code ].iloc[0,2] 
    return eps

def get_price(code):
    return ts.get_k_data(code,start='2011-01-01',end='2017-12-29')

def calculate_pe(eps,Price):
    pe = pd.Series(0,Price.date)
    for i in Price.date:
        year_now = i.split('-')[0]
        year_before = str(int(year_now)-1)
        pe.at[i] = (Price[Price.date == i].close)/(eps[year_before])
    return pe

def get_pe():
    eps = get_eps('600519')
    Price = get_price('600519')
    pe = calculate_pe(eps,Price)
    return pe

#eps = get_eps('600519')
#Price = get_price('600519')
#pe = calculate_pe(eps,Price)
#pe.plot()
#print("\n************\n")
#print(pe)
#print("\n************\n")
#print("\n************\n")
#print(eps)
#print("\n************\n")
#print(Price)

#print(data)
