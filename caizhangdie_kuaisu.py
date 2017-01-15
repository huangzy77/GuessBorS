# coding=utf-8
k=10098   #当前的额度
P_z= 0.34759623 #上涨概率
df00=3144.99 #当前点数
bf_pj= 0.069498#统计均值

b_zhang=6.09#涨率1换几
b_die=1.16#跌率1换几

P_d=1-P_z

#购买额度
buy_bl=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))
sell_bl=((P_d*(b_die-1)-P_z)/(b_die-1))
buy=((P_z*(b_zhang-1)-P_d)/(b_zhang-1))*k
sell=((P_d*(b_die-1)-P_z)/(b_die-1))*k
print("买涨额： %d"%buy+"  买涨比例： %.2f"%buy_bl)
print("卖跌额： %d"%sell+"  买跌比例： %.2f"%sell_bl)

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
zx=(1+bf_pj/100)*df00
print('彩票买入中心值： %.2f'%zx)
