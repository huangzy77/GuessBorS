#coding=utf-8
import GetMyData as gd
import numpy as np



#获取数据data_df：#5*N的array记录0\交易日期，1\开盘大盘点位数据，2\１3:00大盘点位数据,3\13:00成交交金额，４\昨日收盘点位数据，５\昨日成交金额，6\今日收盘点位）
data_df_raw=np.array(gd.data_df)
np.nan_to_num(data_df_raw)#去除nan

ysc=[]#去除０
for dt in np.arange(np.shape(data_df_raw)[0]):
	#print dt
	if data_df_raw[dt,5]==0:
		ysc.append(dt)
		print(data_df_raw[dt,:])
print(ysc)
data_df=np.delete(data_df_raw,ysc,0)

#整理数据data_zl　０、交易日期　１、开盘涨跌幅度　２＼１３时涨跌幅度　３＼１３时成交金额涨跌幅度　４、昨日收盘点位　５昨日成交金额　６今日收盘涨跌情况-1为跌１为涨
data_zl=np.zeros(data_df.shape)
data_zl[:,0]=data_df[:,0]#０、交易日期
data_zl[:,4]=data_df[:,4]#４、昨日收盘点位
data_zl[:,5]=data_df[:,5]#５昨日成交金额
data_zl[:,1]=(data_df[:,1]-data_df[:,4])/data_df[:,4]#１、开盘涨跌幅度
data_zl[:,2]=(data_df[:,2]-data_df[:,4])/data_df[:,4]#２、１３时涨跌幅度
data_zl[:,3]=(data_df[:,3]-data_df[:,5])/(data_df[:,5])#３＼１３时成交金额涨跌幅度
for i in range(data_zl.shape[0]):#６今日收盘涨跌情况０为跌１为涨
    if data_df[i,6]>data_df[i,4]:data_zl[i,6]=1
    else:data_zl[i,6]=-1


#归一化函数
def autoNorm(dataSet):
    minVals=dataSet.min(0)
    maxVals=dataSet.max(0)
    ranges=maxVals-minVals
    #normDataSet=np.zeros(shape(dataSet))
    m=dataSet.shape[0]
    normDataSet=dataSet-np.tile(minVals,(m,1))
    normDataSet=normDataSet/np.tile(ranges,(m,1))
    return normDataSet

def get_cleandata():
    return data_zl

for l in data_zl[:,6]:
	if l==0:
		print(l)
print(data_zl.shape)
