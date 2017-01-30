from jqdata import *
from datetime import *
from numpy import *
from scipy import stats
from scipy import integrate
import matplotlib.pylab as plt

#www.joinquant.com
#需要填入的变量
j=-0.36 #当前的涨跌幅度百分比
b_zhang=1.84 #涨率1换几from jqdata import *
from datetime import *
from numpy import *
from scipy import stats
from scipy import integrate
import matplotlib.pylab as plt

#需要填入的变量
j=0.23 #当前的涨跌幅度百分比
b_zhang=1.18#涨率1换几
b_die=5.58#跌率1换几
p00=3149.91 #当前的上证值
k=20386   #当前的额度
i=1280 #统计多少天的

opentime=[]
starttime=[]
endtime=[]
df_open=[] #当日开盘数据
df=[] #存储下午分钟数据
bf=[] #存储下午波幅百分比数据(（15：00数据-13：00数据）/9：30开盘数据)


#获取i天内下午的波幅
dddd=get_trade_days(end_date=0, count=i)#获取交易日期数列dddd
for l in range(0,i-1):
    starttime.append(dddd[l].strftime('%Y-%m-%d 13:00:00'))
    endtime.append(dddd[l].strftime('%Y-%m-%d 15:00:00'))
    df.append(get_price('000001.XSHG', start_date=starttime[l], end_date=endtime[l], frequency='1m') )# 获得下午13:00数据
    bf.append((df[l]['close'][-1]-df[l]['open'][0])*100/df[l]['open'][0])#这是一天中下午的波幅（15：00-13：00）


#估计出概率密度函数
mdhs=stats.gaussian_kde(bf)
#密度函数积分求上涨概率
P_z=integrate.quad(mdhs,-j,10)[0]
#print(P_z_lisan)
P_d=1-P_z
print("涨概率： %.8f"%P_z+" 跌概率： %.8f"%P_d)


#购买额度
buy_bl=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))
sell_bl=((P_d*(b_die-1)-P_z)/(b_die-1))
buy=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))*k
sell=((P_d*(b_die-1)-P_z)/(b_die-1))*k
print("买涨额： %.d"%buy+"  买涨比例： %.2f"%buy_bl)
print("卖跌额： %.d"%sell+"  买跌比例： %.2f"%sell_bl)

#彩票系列
bf_pj=mean(bf)
zx=(1+bf_pj/100)*p00
print('彩票买入中心值： %.2f'%zx)

#绘制数据柱状图
plt.hist(bf,100,normed=1)#第二个参数越大，柱子分得越细；normed=1表示归一化
x=np.arange(-10,10,0.1)
y=[]
for ii in x:
	y.append(mdhs(ii))
plt.plot(x,y)
#plt.plot(j,y)
plt.show()

b_die=1.96 #跌率1换几
p00=3117.71 #当前的上证值
k=21236   #当前的额度
i=1280 #统计多少天的

opentime=[]
starttime=[]
endtime=[]
df_open=[] #当日开盘数据
df=[] #存储下午分钟数据
bf=[] #存储下午波幅百分比数据(（15：00数据-13：00数据）/9：30开盘数据)


#获取i天内下午的波幅
dddd=get_trade_days(end_date=0, count=i)#获取交易日期数列dddd
for l in range(0,i-1):
    starttime.append(dddd[l].strftime('%Y-%m-%d 13:00:00'))
    endtime.append(dddd[l].strftime('%Y-%m-%d 15:00:00'))
    df.append(get_price('000001.XSHG', start_date=starttime[l], end_date=endtime[l], frequency='1m') )# 获得下午13:00数据
    bf.append((df[l]['close'][-1]-df[l]['open'][0])*100/df[l]['open'][0])#这是一天中下午的波幅（15：00-13：00）

#绘制数据柱状图
plt.hist(bf,100,normed=1)#第二个参数越大，柱子分得越细
#估计出概率密度函数
mdhs=stats.gaussian_kde(bf)
#密度函数积分求上涨概率
P_z=integrate.quad(mdhs,-j,10)[0]
#print(P_z_lisan)
P_d=1-P_z
print("涨概率： %.8f"%P_z+" 跌概率： %.8f"%P_d)

#购买额度
buy_bl=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))
sell_bl=((P_d*(b_die-1)-P_z)/(b_die-1))
buy=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))*k
sell=((P_d*(b_die-1)-P_z)/(b_die-1))*k
print("买涨额： %.d"%buy+"  买涨比例： %.2f"%buy_bl)
print("卖跌额： %.d"%sell+"  买跌比例： %.2f"%sell_bl)

#彩票系列
bf_pj=mean(bf)
zx=(1+bf_pj/100)*p00
print('彩票买入中心值： %.2f'%zx)
