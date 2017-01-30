# coding=utf-8
from numpy import *
from scipy import stats
from scipy import integrate
import matplotlib.pylab as plt
#import 数据
import sys
if not "/home/young/GuessBorS" in sys.path:
    sys.path.append("/home/young/GuessBorS") 
if not 'GetMyData' in sys.modules:
    GetMyData = __import__('GetMyData')
else:
    eval('import GetMyData')
    GetMyData= eval('reload(GetMyData)')

bf=GetMyData.bf#存储下午波幅百分比数据(（15：00数据-13：00数据）/9：30开盘数据)


#需要填入的变量
j=0.1 #当前的涨跌幅度百分比
b_zhang=1.78 #涨率1换几
b_die=2.04 #跌率1换几
p00=3139.8 #当前的上证值
k=19016  #当前的额度


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
