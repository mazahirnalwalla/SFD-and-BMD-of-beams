import numpy as np
import matplotlib.pyplot as plt

l = 4 #length of the beam is 4 m
ab = 1
bc = 2
ca = 1
w = 4000 #UDL in N/m
f = 2000 #Point load in Newtons
r = w*bc #reaction force in Newtons

tr = f+r #totla reaction force
m = ((w*bc**2)/8) + (f*l/4)

x1 = np.linspace(0,ab,500)
x2 = np.linspace(0,bc,1000)
x3 = np.linspace(0,ca,500)

X = []
SF = []
BM = []

for ab in x1:
    sfi = tr
    bmi = tr - (f*ab/2)
    X.append(ab)
    SF.append(sfi)
    BM.append(bmi)

bm1 = tr - (f*ab/2)

for bc in x2:
    sfi = tr - (w*bc)
    bmi = bm1 - (tr*bc) + ((w*bc**2)/2)
    X.append(ab+bc)
    SF.append(sfi)
    BM.append(bmi)

sfi_fin = tr - (w*bc)
bm2 = bm1 - (tr*bc) + ((w*bc**2)/2)

for ca in x3:
    sfi = sfi_fin
    bmi = bm2 - tr + (f*ca/2)
    X.append(ab+bc+ca)
    SF.append(sfi)
    BM.append(bmi)

print(f"The maximum shear force is {tr} Newtons")
print(f"The maximum bending moment is {m} Nm")

plt.subplot(2,1,1)
plt.bar(X,SF,width=0.01)
plt.ylabel("Shear Force (in N) ->")
plt.text(1.5,5000,"SFD")
plt.subplot(2,1,2)
plt.bar(X,BM,width=0.01,color="red")
plt.xlabel("<- Length of the beam in meters ->")
plt.ylabel("Bending Moment (in Nm) ->")
plt.text(3,1000,"BMD")
plt.show()