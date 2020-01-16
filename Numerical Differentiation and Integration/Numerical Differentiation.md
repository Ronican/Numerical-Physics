Derivation of function *f(x)* in range [a,b] at *x* is:

![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142485168)

If the analytic equation of *f(x)* is known, then derivation of *f(x)* can be found most of the time, yet it could be challenging. As a experimental physics undergrad, most of the time our equations are given at precise values at lab, so we need those numerical differentiations.

Let's say *f(x)* is ordered with equal *h* intervals of ![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142603011) :


![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142730461)   and   ![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142784929)

Let's do **Taylor Expansion** near xi:

![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142888702) (Forward Difference)

Hence by using f(xi-h) we can find backward difference also.

![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142949097) (Backward Difference)

The error ratio is at h. Can we get a better error ratio? Hell yeah!

If we subtract forward and backward we get:

![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142994321) (Central Difference)

As you can see h^2 error ratio is getting smaller by power of 2 ratio when h getting smaller.

This method can be improved by more xi points.

Let's give an example: ***You can find this example code at comparison.py***

![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579143027895)

We will find the differentiation of f(x) at x=1,2,3 and h=0.00001

As you can see forward and backward differences have less correct values than central difference.

---
So, how do we use these at physics. Let's jump in another example: ( You can find the code at 1d-movement.py)

There is a string with applied force of F=-kx. Calculate the travel.

To keep the program simple, take m=k=1 and ![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579143078263)

---

With that, we finish our first lesson. I only give python3 codes but if I can find time or if anyone request it, I will give matlab, fortran, c++, mathematica and maybe sagemath examples too.
