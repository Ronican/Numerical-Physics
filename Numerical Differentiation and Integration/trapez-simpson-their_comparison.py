#At this example I will give trapez and simpson subroutines and then compare the effectiveness of them with s = [a,b],e^xdx = e-1 = 1.718281

import numpy as np

def f(x):
    return np.exp(x)

a=0.0
b=1.0

s_exact = f(1.0)-1.0
n=5 #choosing a right number of n could be challenging because as the number n grows it get better results yet if it grows too much you'll get an error. Try to find with trial and error.



def trapez(a,b,n):
    if (n<1) or (a>b):
        print("Wrong values. N can not be lower than 1 and a can not be higher than b!")
    else:
        h = (b-a)/n
        s = 0.5*(f(a)+f(b))
        for i in range(1,n):
            x = a+i*h
            s = s+f(x)
        return (h*s)

def simpson(a,b,n):
    if n<1 or a>b:
        print("Wrong values. N can not be lower than 1 and a can not be higher than b!")
    elif n%2==1:
        print("N is not an even number!")
    else:
        
        h = (b-a)/n

        s = f(a)+f(b)
        for i in range(1,n):

            coefficient = 2*(i%2+1)
            x = a+i*h
            s=s+coefficient*f(x)
    return h*s/3


print("N","Trapez Error","Simpson Error")

for i in range(5):
    print(n,"%.6f" % float(trapez(a,b,n)-s_exact),"%.6f" % float(simpson(a,b,n)-s_exact))
    n=n+5
