import math #importing our math library

def f(x): #a function f as cot(x)
    return 1/math.tan(x)


def fd(x): #derivative of f(x) = cot(x)
    return -1/math.sin(x)**2

h=0.001 #our given h

for i in range(3): #x values of x=1,2,3
    x = float(i+1)
    fd_forward = (f(x+h)-f(x))/h
    fd_backward = (f(x)-f(x-h))/h
    fd_central = (f(x+h)-f(x-h))/(2*h)
    fd_original = fd(x)

    print("%.10f" % fd_forward,"%10.f" %fd_backward,"%10.f" %fd_central,"%10.f" %fd_original)
