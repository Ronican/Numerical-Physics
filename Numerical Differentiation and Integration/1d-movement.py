import numpy as np
import matplotlib.pyplot as plt

def f(x,v,t):
    return -x

n=500
h=6.28/n
t=np.zeros(n,float)
x=np.zeros(n,float)
v=np.zeros(n,float)

v[0]=1.0

for i in range(1,n):
    t[i]=h*i
    x[i]=x[i-1]+v[i-1]*h
    v[i]=v[i-1]+f(x[i-1],v[i-1],t[i-1])*h

plt.plot(t,x,"k-")
plt.plot(t,v,"k--")
plt.xlabel("t")
plt.ylabel("y=sinx and y=cosx")
plt.show()
