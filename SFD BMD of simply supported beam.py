import numpy as np
import matplotlib.pyplot as plt

l = float(input("Enter length of the beam in m: "))
w = float(input("Enter value of UDL in N/m: "))

R = w*l/2
M = (w*l**2)/8
x = np.linspace(0,l,5000)

X = []
SF = []
BM = []

for l in x:
    sfi = R-(w*l)
    bmi = (R*l)-((w*l**2)/2)
    X.append(l)
    SF.append(sfi)
    BM.append(bmi)

plt.subplot(2,1,1)
plt.bar(X,SF,color="blue",width=0.01)
plt.text(2*l/3,R/2,"SFD")
plt.ylim(-R-20,R+20)
plt.ylabel("Shear Force ->")

plt.subplot(2,1,2)
plt.bar(X,BM,color="red",width=0.2)
plt.text(l/2,M/2,"BMD")
plt.ylim(0,M+10)
plt.xlabel("<- Length of the Beam ->")
plt.ylabel("Bending Moment ->")
plt.show()
