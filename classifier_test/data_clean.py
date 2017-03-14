#coding=utf-8
import GetMyData as gd
import numpy as np



#获取数据data_df：#5*N的array记录0\交易日期，1\开盘大盘点位数据，2\１3:00大盘点位数据,3\13:00成交交金额，４\昨日收盘点位数据，５\昨日成交金额，6\今日收盘点位）
data_df_raw=np.array(gd.data_df)

ysc=[]#去除０
for dt in np.arange(np.shape(data_df_raw)[0]):
	#print dt
	if data_df_raw[dt,5]==0:
		ysc.append(dt)

data_df=np.delete(data_df_raw,ysc,0)

#整理数据data_zl　０、交易日期　１、开盘是否涨（涨为１跌为－１）　２＼１３时相对昨日是否涨（涨为１跌为－１）　３＼１３时成交金额相对于昨日的二分之一是否涨（（涨为１跌为－１））　４、昨日收盘点位　５昨日成交金额　６今日收盘涨跌情况(-1为跌１为涨 )　7上午最高点相对于昨日收盘是否涨（涨为１跌为－１）　８上午最低点相对于昨日收盘是否涨（涨为１跌为－１）
data_zl=np.zeros(data_df.shape)
data_zl[:,0]=data_df[:,0]#０、交易日期
data_zl[:,4]=data_df[:,4]#４、昨日收盘点位
data_zl[:,5]=data_df[:,5]#５昨日成交金额


for i in range(data_zl.shape[0]):
	if data_df[i,6]>data_df[i,4]:#６今日收盘涨跌情况(-1为跌１为涨 )
		data_zl[i,6]=1
	else:
		data_zl[i,6]=-1

	if data_df[i,1]>data_df[i,4]:#１、开盘是否涨（涨为１跌为－１）
		data_zl[i,1]=1
	else:
		data_zl[i,1]=-1

	if data_df[i,2]>data_df[i,4]:#１、１３时相对昨日是否涨（涨为１跌为－１）
		data_zl[i,2]=1
	else:
		data_zl[i,2]=-1

	if data_df[i,3]>data_df[i,5]:#１、１３时成交金额相对于昨日的0.8是否涨（（涨为１跌为－１））
		data_zl[i,3]=1
	else:
		data_zl[i,3]=-1

	if data_df[i,7]>data_df[i,4]:#１、上午最高点相对于昨日收盘是否涨（涨为１跌为－１）
		data_zl[i,7]=1
	else:
		data_zl[i,7]=-1

	if data_df[i,8]>data_df[i,4]:#１、上午最低点相对于昨日收盘是否涨（涨为１跌为－１）
		data_zl[i,8]=1
	else:
		data_zl[i,8]=-1



def get_cleandata():
	return data_zl

for l in data_zl[:,6]:
	if l==0:
		print(l)
#print(data_zl.shape)
