# coding=utf-8
import tushare as ts
import numpy as np
import pandas as pd

ts.set_token('6a67ac9bfe7f0f5ca103409a7af4f8002bfb97639b988d4a5e3ab80319f0dc46')
df = ts.get_tick_data('000756','2015-03-27')
#df=ts.get_hist_data('000001',ktype='5',index=True,start='2000-01-01',end='2012-01-01')
#df.to_hdf('shdata.h5','df')
print df
#def CallIndex(df): #计算各种指标

#print df[df.index=='2017-03-02']['close'].values
