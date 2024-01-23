import numpy as np
n = 9
x = np.array([[1,1,1,1,1,1,1,1,1]]) #эталон
W = np.dot(x.T,x)
y = np.array([[1,-1,1,-1,1,-1,1,1,-1]]) #тест

for i in range(n):
    y[0][i]=np.sign(y[0][i])

Second_y = y
k=np.array([[0,0,0,0,0]])
col = 1
while (True):
    for i in range(n):
        for j in range(n):
            Second_y[0][i]=W[j][i]*y[0][j]+Second_y[0][i]
        Second_y[0][i]=np.sign(Second_y[0][i])
    if (np.array_equal(k, Second_y)):
        break
    else:
        k=Second_y
        col=col+1
print(Second_y,col)
if (np.array_equal(x,Second_y)): 
    print("Совпало")
else: print("Не совпало")