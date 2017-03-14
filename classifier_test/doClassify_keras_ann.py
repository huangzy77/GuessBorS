#coding=utf-8

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD


import data_clean as da
import numpy as np
np.random.seed(1337)  # for reproducibility

#数据设置函数
#整理数据data_zl　０、交易日期　１、开盘涨跌幅度　２＼１３时涨跌幅度　３＼１３时成交金额涨跌幅度　４、昨日收盘点位　５昨日成交金额　６今日收盘涨跌情况０为跌１为涨 7上午最高点幅度　８上午最低点幅度
def setData(bfb,dataset):#bfb指数据集中用来测试的数据百分比，dataset指numpy数据集
	testVecNum=int(dataset.shape[0]*bfb/100)#用于测试的行数
	trainVecNum=dataset.shape[0]-testVecNum#用于训练的行数

	trainVec=np.zeros((trainVecNum,5))#初始化数据容器
	trainLabelsVec=[]
	testVec=np.zeros((testVecNum,5))
	testLabelsVec=[]

	trainVec[:,0]=dataset[0:trainVecNum,2]#填充数据容器
	trainVec[:,1]=dataset[0:trainVecNum,3]
	trainVec[:,2]=dataset[0:trainVecNum,1]
	trainVec[:,3]=dataset[0:trainVecNum,7]
	trainVec[:,4]=dataset[0:trainVecNum,8]

	trainLabelsVec=dataset[0:trainVecNum,6]

	testVec[:,0]=dataset[trainVecNum:dataset.shape[0],2]#填充数据容器
	testVec[:,1]=dataset[trainVecNum:dataset.shape[0],3]
	testVec[:,2]=dataset[trainVecNum:dataset.shape[0],1]
	testVec[:,3]=dataset[trainVecNum:dataset.shape[0],7]
	testVec[:,4]=dataset[trainVecNum:dataset.shape[0],8]

	testLabelsVec=dataset[trainVecNum:dataset.shape[0],6]

	return trainVec,trainLabelsVec,testVec,testLabelsVec,testVecNum


#获取数据
dataclean=da.get_cleandata()
trainVec,trainLabelsVec,testVec,testLabelsVec,testVecNum=setData(8,dataclean)
#print trainVec


#构造神经网络

model = Sequential() 
model.add(Dense(64, input_dim=5, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(64, init='uniform'))
model.add(Activation('tanh'))
model.add(Dropout(0.5))
model.add(Dense(1, init='uniform'))
model.add(Activation('softmax')) 

   
# 设定学习率（lr）等参数   编译
sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='mse',optimizer=sgd,metrics=['accuracy'])


#训练这个网络
model.fit(trainVec, trainLabelsVec, batch_size=200, nb_epoch=1000,shuffle=True, verbose=1, validation_split=0.3)   
print 'test set'  

#测试这个网络 
print model.evaluate(testVec, testLabelsVec)  

'''
#用于预测当前
dqzd=-0.0037#当前１３时涨跌幅度百分比换算成小数
dqcj=92898000#当前成交量
zrcj=181000000#昨日成交量
kpzdf=0.00
zgfd=0.005
zdfd=-0.0003
b_zhang=2.53#涨赔率
b_die=1.53#跌赔率
k=3746#当前余额

nowData=[dqzd,dqcj/zrcj,kpzdf,zgfd,zdfd]#第一个为１３时涨跌幅，第二个为１３时成交金额比例
classifierResult_now=clf.predict(np.array(nowData).reshape((1,-1)))
print("当前预测结果为：%d"%classifierResult_now)

#凯利公式测试
P_right=1-P_wrong
if classifierResult_now==1:
	buy_bl=((P_right*(b_zhang-1)-P_wrong)/(b_zhang-1))*k
	print("今天买涨额度：%d"%buy_bl)
if classifierResult_now==-1:
	buy_dl=((P_right*(b_die-1)-P_wrong)/(b_die-1))*k
	print("今天买跌额度：%d"%buy_dl)
'''

