#coding=utf-8
import ANNBP as bp
import data_clean as da
import numpy as np

#整理数据data_zl　０、交易日期　１、开盘涨跌幅度　２＼１３时涨跌幅度　３＼１３时成交金额涨跌幅度　４、昨日收盘点位　５昨日成交金额　６今日收盘涨跌情况０为跌１为涨
dataclean=da.get_cleandata()
cases=np.zeros((dataclean.shape[0],3))
cases[:,0]=dataclean[:,2]
cases[:,1]=dataclean[:,3]
cases[:,2]=dataclean[:,1]
labels=np.zeros((dataclean.shape[0],1))
labels[:,0]=dataclean[:,6]


bpNet=bp.bp(3,7,1)
bpNet.train(cases, labels, 10000, 0.005,0.0001)

