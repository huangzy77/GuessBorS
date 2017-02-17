# coding=utf-8
import math
import matplotlib.pylab as plt
import numpy as np
#import pandas as pd
from scipy import stats
from scipy import integrate


import sys
if not "/home/young/GuessBorS" in sys.path:
    sys.path.append("/home/young/GuessBorS") 
if not 'GetMyData' in sys.modules:
    GetMyData = __import__('GetMyData')
else:
    eval('import GetMyData')
    GetMyData= eval('reload(GetMyData)')

bf=GetMyData.bf#存储下午波幅百分比数据(（15：00数据-13：00数据）/9：30开盘数据)
#scipy.stats.gaussian_kde估计概率密度函数

mdhs=stats.gaussian_kde(bf)
x=np.arange(-10,10,0.1)
y=[]
for i in x:
	y.append(mdhs(i))
y2=np.arange(0,1,0.1)
x2=np.zeros(len(y2))+0.32
plt.plot(x2,y2,'r')
plt.plot(x,y)
plt.hist(bf,100,normed=1)


#积分求概率

gl=integrate.quad(mdhs,-10,10)[0]
print(gl)

#标准正太分布函数
def gd(x,m,s):
    left=1/(math.sqrt(2*math.pi)*s)
    right=math.exp(-math.pow(x-m,2)/(2*math.pow(s,2)))
    return left*right
#绘制图形
datamean=np.mean(bf)#数据均值和均方差
datavar=np.var(bf)

x3=np.arange(-10,10,0.1)
y3=[]
for i in x3:
	y3.append(gd(i,datamean,datavar))
plt.plot(x3,y3,'r')
plt.show()

