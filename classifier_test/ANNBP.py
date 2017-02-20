# -*- coding:utf-8 -*- 
import random
import math
def rand(a,b):
	    return (b - a) * random.random() + a
def make_matrix(m,n,fill=0.0):  # 创造一个指定大小的矩阵
    mat = []
    for i in range(m):
	mat.append([fill] * n)
    return mat

#sigmoid函数及导数
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def sigmod_derivate(x):
    return x * (1 - x)

class bp(object):
		#初始化神经网络，ｎｉ为输入层，ｎｈ为隐藏层，ｎｏ为输出层
	def __init__(self,ni,nh,no):
	    self.input_n = ni + 1
	    self.hidden_n = nh
	    self.output_n = no
	    # init cells
	    self.input_cells = [1.0] * self.input_n
	    self.hidden_cells = [1.0] * self.hidden_n
	    self.output_cells = [1.0] * self.output_n
	    # init weights
	    self.input_weights = make_matrix(self.input_n,self.hidden_n)
	    self.output_weights = make_matrix(self.hidden_n,self.output_n)
	    # random activate
	    for i in range(self.input_n):
		for h in range(self.hidden_n):
		    self.input_weights[i][h] = rand(-0.2,0.2)
	    for h in range(self.hidden_n):
		for o in range(self.output_n):
		    self.output_weights[h][o] = rand(-2.0,2.0)
	    # init correction matrix
	    self.input_correction = make_matrix(self.input_n,self.hidden_n)
	    self.output_correction = make_matrix(self.hidden_n,self.output_n)

	#定义predict方法进行一次前馈,并返回输出
	def predict(self,inputs):
	    # activate input layer
	    for i in range(self.input_n - 1):
		self.input_cells[i] = inputs[i]
	    # activate hidden layer
	    for j in range(self.hidden_n):
		total = 0.0
		for i in range(self.input_n):
		    total += self.input_cells[i] * self.input_weights[i][j]
		self.hidden_cells[j] = sigmoid(total)
	    # activate output layer
	    for k in range(self.output_n):
		total = 0.0
		for j in range(self.hidden_n):
		    total += self.hidden_cells[j] * self.output_weights[j][k]
		self.output_cells[k] = sigmoid(total)
	    return self.output_cells[:]

	#定义back_propagate方法定义一次反向传播和更新权值的过程,并返回最终预测误差:
	def back_propagate(self,case,label,learn,correct):
	    # feed forward
	    self.predict(case)
	    # get output layer error
	    output_deltas = [0.0] * self.output_n
	    for o in range(self.output_n):
		error = label[o] - self.output_cells[o]
		output_deltas[o] = sigmod_derivate(self.output_cells[o]) * error
	    # get hidden layer error
	    hidden_deltas = [0.0] * self.hidden_n
	    for h in range(self.hidden_n):
		error = 0.0
		for o in range(self.output_n):
		    error += output_deltas[o] * self.output_weights[h][o]
		hidden_deltas[h] = sigmod_derivate(self.hidden_cells[h]) * error
	    # update output weights
	    for h in range(self.hidden_n):
		for o in range(self.output_n):
		    change = output_deltas[o] * self.hidden_cells[h]
		    self.output_weights[h][o] += learn * change + correct * self.output_correction[h][o]
		    self.output_correction[h][o] = change
	    # update input weights
	    for i in range(self.input_n):
		for h in range(self.hidden_n):
		    change = hidden_deltas[h] * self.input_cells[i]
		    self.input_weights[i][h] += learn * change + correct * 	self.input_correction[i][h]
		    self.input_correction[i][h] = change
	    # get global error
	    error = 0.0
	    for o in range(len(label)):
			error += 0.5 * (label[o] - self.output_cells[o]) ** 2
	    return error

	#定义train方法控制迭代,该方法可以修改最大迭代次数,学习率λλ,矫正率μμ三个参数.
	def train(self,cases,labels,limit=10000,learn=0.05,correct=0.1):
	    for i in range(limit):
			error = 0.0
			for i in range(len(cases)):
			    label = labels[i]
			    case = cases[i]
			    error += self.back_propagate(case,label,learn,correct)
		 	print(error) 

	#编写test方法，演示如何使用神经网络学习异或逻辑:
	def test(self):
	    cases = [
		    [0,0],
		    [0,1],
		    [1,0],
		    [1,1],
		]
	    labels = [[0],[1],[1],[0]]
	    self.__init__(2,5,1)
	    self.train(cases,labels,1000000,0.005,0.1)
	    for case in cases:
		print(self.predict(case))

