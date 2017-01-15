from jqdata import *
from datetime import *
from numpy import *
from scipy import stats

#需要填入的变量
j=-0.18 #当前的涨跌幅度百分比
b_zhang=2.2 #涨率1换几
b_die=1.68   #跌率1换几
k=7648      #当前的额度
kp_open=3132.16 #今日开盘价格
i=28 #统计多少天的

opentime=[]
starttime=[]
endtime=[]
df_open=[] #当日开盘数据
df=[] #存储下午分钟数据
bf=[] #存储下午波幅百分比数据(（15：00数据-13：00数据）/9：30开盘数据)


#获取i天内下午的波幅
dddd=get_trade_days(end_date=0, count=i)#获取交易日期数列dddd
for l in range(0,i-1):
    opentime.append(dddd[l].strftime('%Y-%m-%d 09:30:00'))
    starttime.append(dddd[l].strftime('%Y-%m-%d 13:00:00'))
    endtime.append(dddd[l].strftime('%Y-%m-%d 15:00:00'))
    df_open.append(get_price('000001.XSHG', start_date=opentime[l], end_date=endtime[l], frequency='1d') )# 获得全天数据
    df.append(get_price('000001.XSHG', start_date=starttime[l], end_date=endtime[l], frequency='1m') )# 获得下午13:00数据
    bf.append((df[l]['close'][-1]-df[l]['open'][0])*100/df_open[l]['open'][0])#这是一天中下午的波幅（15：00-13：00）
#计算落入概率
bf_pj=mean(bf) #下午的平均波幅比
fc=std(bf) #求方差
print("波幅均值： %.6f"%bf_pj+"波幅方差： %.6f"%fc)

P_z=sum(stats.norm.pdf(arange(-j,10,0.000001),bf_pj,fc))/1000000 #涨跌概率(密度函数有问题)
#print(P_z_lisan)
P_d=1-P_z
print("涨概率： %.8f"%P_z+" 跌概率： %.8f"%P_d)

#购买额度
buy=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))*k
sell=((P_d*(b_die-1)-P_z)/(b_die-1))*k
print("买涨额： %d"%buy)
print("卖跌额： %d"%sell)

#彩票系列
md=0 #存储买入彩票金额
if buy>0 and sell <0:
    md=buy
if buy<0 and sell >0:
    md=sell
if buy>0 and sell >0:
    md=sell+buy
zs=(md-md%50)/50 #存储买入张数
print('彩票买入张数： %d'%zs) #最高买20张
zx=kp_open*(1+bf_pj/100)
print('彩票买入中心值： %.2f'%zx)
