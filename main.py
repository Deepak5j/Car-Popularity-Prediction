import pandas
from sklearn.linear_model import LinearRegression
import csv

train = 'train.csv'
data_train = pandas.read_csv(train, delimiter=",")

test = 'test.csv'
names = ['buying_price','maintainence_cost','number_of_doors','number_of_seats','luggage_boot_size','safety_rating','popularity']
data_test = pandas.read_csv(test, names=names, delimiter=",")

array = data_train.values
x = array[:,0:6] 
y = array[:,6:7]

model = LinearRegression()
model.fit(x, y)

array2 = data_test.values
x_pr = array2[:,0:6]

        
y_pr = model.predict(x_pr)
    
#print(x)
#print(x_pr)
#print(y)
#print(y_pr)

def rd(num):
    if num < 0:
        return int(num - 0.5)
    else:
        return int(num + 0.5)    
ls = []
for i in y_pr:
    tmp = []
    for j in i:
        ls.append(int(rd(j)))

print(ls)

with open('prediction.csv', 'w', newline='\n') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter='\n', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(ls)































