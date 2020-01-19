#At this code you can see how to simulate an event and find the value of pi. Beware that expanding the number of events will get better results.

#Let's say we have an empty square which has an arc of quarter circle.
#Radius of circle is 1 unit thus area of quarter circle goes to pi/4 square units.
#Also side of square is 1 unit thus area of square goes to 1 square units.

#The probablity of a random point being inside of the circle is P = Area of Quarter Circle / Area of Square = Pi / 4

#For N samples, M points; M for N samples: M = N*PI/4

from random import random
import numpy as np

points = int(input("How many points do you want to simulate?(Remember more points get better results)"))

inside = 0

for i in range(points):
    x = random()
    y = random()
    if (x**2+y**2)**0.5<1:
        inside=inside+1

simulated_pi = 4.0*(float(inside)/points)
print("The value of simulated pi for {} points is {}".format(points,simulated_pi))
print("The difference between real pi and our simulated pi is: {}".format(np.pi-simulated_pi))
