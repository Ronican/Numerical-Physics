Derivation of function *f(x)* in range [a,b] at *x* is:

![](https://www.latex4technics.com/l4ttemp/iixw9s.png?1579142485168)

If the analytic equation of *f(x)* is known, then derivation of *f(x)* can be found most of the time, yet it could be challenging. As a experimental physics undergrad, most of the time our equations are given at precise values at lab, so we need those numerical differentiations.

Let's say *f(x)* is ordered with equal *h* intervals of <img src="http://bit.ly/2RrdWEa" align="center" border="0" alt=" x_{0} ,  x_{1} , x_{2},  x_{3} ... x_{N} " width="146" height="15" /> :


<img src="http://bit.ly/2FTGcKg" align="center" border="0" alt=" {x_{i} =  x_{0} +   ih}" width="97" height="18" /> and <img src="http://bit.ly/2Nug38S" align="center" border="0" alt="  { f_{i} = f( x_{i} ) " width="74" height="19" />

Let's do **Taylor Expansion** near xi:

<img src="http://bit.ly/2Tso55P" align="center" border="0" alt=" f' ( x_{i} ) = \frac{f( x_{i}+h) - f( x_{i})}{h} +  \mathcal{O}(h)" width="258" height="43" /> + O(h) (Forward Difference)

Hence by using f(xi-h) we can find backward difference also.

<img src="http://bit.ly/2Tso55P" align="center" border="0" alt=" f' ( x_{i} ) = \frac{f( x_{i}) - f( x_{i}-h)}{h} +  \mathcal{O}(h)$" width="258" height="43" />+ 0(h) (Backward Difference)

The error ratio is at h. Can we get a better error ratio? Hell yeah!

If we subtract forward and backward we get:

<img src="http://bit.ly/2Tso55P" align="center" border="0" alt=" f' ( x_{i} ) = \frac{f( x_{i}+h) - f( x_{i}-h)  }{2h} +  {\mathcal{O}(h^2)}" width="297" height="43" /> + O(h^2) (Central Difference)

As you can see h^2 error ratio is getting smaller by power of 2 ratio when h getting smaller.

This method can be improved by more xi points.

Let's give an example: ***You can find this example code at comparison.py***

<img src="http://bit.ly/30ql9Zd" align="center" border="0" alt="f(x) = cot(x) ,  f' (x) =  {-1}  \backslash  {sin^2(x)}" width="272" height="22" />

We will find the differentiation of f(x) at x=1,2,3 and h=0.00001

As you can see forward and backward differences have less correct values than central difference.

---
So, how do we use these at physics. Let's jump in another example: ( You can find the code at 1d-movement.py)

There is a string with applied force of F=-kx. Calculate the travel.

To keep the program simple, take m=k=1 and <img src="http://bit.ly/3ae50KU" align="center" border="0" alt="T = 2 \Pi  \sqrt{m/k}  \approx 6.28s" width="258" height="43" />

---

With that, we finish our first lesson. I only give python3 codes but if I can find time or if anyone request it, I will give matlab, fortran, c++, mathematica and maybe sagemath examples too.
