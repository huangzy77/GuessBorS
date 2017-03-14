#coding=utf-8
import numpy as np
np.random.seed(1337)  # for reproducibility
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt # 可视化模块

# create some data
X = np.linspace(-1, 1, 200)
np.random.shuffle(X)    # randomize the data
Y = 0.5 * X + 2 + np.random.normal(0, 0.05, (200, ))


model = Sequential()
model.add(Dense(output_dim=1, input_dim=1))
# choose loss function and optimizing method
model.compile(loss='mse', optimizer='sgd')

print('Training -----------')
for step in range(301):
    cost = model.train_on_batch(X, Y)
    if step % 100 == 0:
        print('train cost: ', cost)
# test
print('\nTesting ------------')
cost = model.evaluate(X, Y, batch_size=40)
print('test cost:', cost)
W, b = model.layers[0].get_weights()
print('Weights=', W, '\nbiases=', b)
# plot data
Y_pred = model.predict(X)
plt.scatter(X, Y)
plt.plot(X, Y_pred)
plt.show()
