#coding=utf-8
import numpy as np
f=open('data.txt','r')
lines=f.readlines()
temp=lines[0].replace(']','')
temp=temp.replace('[','')
temp=temp.replace(' ','')
temp=temp.replace('nan','0')
temp=temp.replace('\n','')
data_df_temp=temp.split(',')
data_df=np.zeros((len(data_df_temp)/9,9))#开辟数据容器内存空间

i=0
for data in data_df_temp:
	data_df[i//9,i%9]=float(data)
	i+=1
