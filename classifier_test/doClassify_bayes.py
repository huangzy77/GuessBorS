#coding=utf-8
from sklearn.naive_bayes import GaussianNB
import data_clean as da
import numpy as np

#数据设置函数
#整理数据data_zl　０、交易日期　１、开盘涨跌幅度　２＼１３时涨跌幅度　３＼１３时成交金额涨跌幅度　４、昨日收盘点位　５昨日成交金额　６今日收盘涨跌情况０为跌１为涨
def setData(bfb,dataset):#bfb指数据集中用来测试的数据百分比，dataset指numpy数据集
	testVecNum=int(dataset.shape[0]*bfb/100)#用于测试的行数
	trainVecNum=dataset.shape[0]-testVecNum#用于训练的行数

	trainVec=np.zeros((trainVecNum,2))#初始化数据容器
	trainLabelsVec=[]
	testVec=np.zeros((testVecNum,2))
	testLabelsVec=[]

	trainVec[:,0]=dataset[0:trainVecNum,2]#填充数据容器
	trainVec[:,1]=dataset[0:trainVecNum,3]
	#trainVec[:,2]=dataset[0:trainVecNum,1]
	trainLabelsVec=dataset[0:trainVecNum,6]

	testVec[:,0]=dataset[trainVecNum:dataset.shape[0],2]#填充数据容器
	testVec[:,1]=dataset[trainVecNum:dataset.shape[0],3]
	#testVec[:,2]=dataset[trainVecNum:dataset.shape[0],1]
	testLabelsVec=dataset[trainVecNum:dataset.shape[0],6]

	return trainVec,trainLabelsVec,testVec,testLabelsVec,testVecNum

#分类测试函数
def classifyTest(testVec_num):
	errorCount=0
	for i in range(testVec_num):
		classifierResult=clf.predict(testVec[i,:].reshape((1,-1)))
		print("分类器结果是：%d,实际情况是：%d"%(classifierResult,testLabelsVec[i]))
		if(classifierResult!=testLabelsVec[i]):errorCount+=1
	cuowulv=errorCount/float(testVec_num)
	print("错误率为：%f"%(errorCount/float(testVec_num)))
	return cuowulv

#获取数据
dataclean=da.get_cleandata()
trainVec,trainLabelsVec,testVec,testLabelsVec,testVecNum=setData(10,dataclean)
print trainVec
#bayes分类

clf=GaussianNB().fit(trainVec,trainLabelsVec)

#测试这个分类器并统计争取率
P_wrong=classifyTest(testVecNum)

#用于预测当前
dqzd=-0.0015#当前１３时涨跌幅度百分比换算成小数
dqcj=435800#当前成交量
zrcj=212000000#昨日成交量
b_zhang=1.88#涨赔率
b_die=1.01#跌赔率
k=7000#当前余额

nowData=[dqzd,dqcj/zrcj]#第一个为１３时涨跌幅，第二个为１３时成交金额比例
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


