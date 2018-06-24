#import tensorflow as tf
from sklearn.preprocessing import scale
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
import matplotlib
from matplotlib import style
import pandas

train = 'train.csv'
data_train = pandas.read_csv(train, delimiter=",")

test = 'test.csv'
names = ['buying_price','maintainence_cost','number_of_doors','number_of_seats','luggage_boot_size','safety_rating','popularity']
data_test = pandas.read_csv(test, names=names, delimiter=",")

array = data_train.values
xtr = array[0:,0:6] #features training
xls = []
for i in xtr:
    sm = 0
    for j in i:
        sm += j
    xls.append([sm/7])        
ytr = array[0:,6:7] #price training

array = data_test.values
xts = array[:,0:6] #features validation
xkl = []
for i in xts:
    sm = 0
    for j in i:
        sm += j
    xkl.append([sm/7])        

model = LinearRegression()
model.fit(xls, ytr)
yts = model.predict(xkl)

def rd(num):
    if num < 0:
        return int(num - 0.5)
    else:
        return int(num + 0.5)    
ls = []
for i in yts:
    tmp = []
    for j in i:
        ls.append(int(rd(j)))

print(ls)

print('1',ls.count(1))
print('2',ls.count(2))
print('3',ls.count(3))
print('4',ls.count(4))



