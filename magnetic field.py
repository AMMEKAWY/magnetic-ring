import numpy as np
import matplotlib.pyplot as plt
import math

xo=[]
yo=[]
R= 0.5 #m
n=1
i=-n


while round(i,2) != n+R:
    xo.append(round(i,2))
    i+=R

yo=xo
x,y=np.meshgrid(xo,yo)

#-----------------------------------------------------------

mu= 1.3*10**(-6)
k= 0.5 #Amp

pi= 3.14

def Bx(x,y):
    return ((mu*k/2)*(y*x)/(((x-R)**2+y**2)**(3/2)))

def By(x,y):
    return ((mu*k/2)*((R*(R-np.sqrt(x**2)))/(((x-R)**2+y**2)**(3/2))))

#-------------------------------------------------------------

Bx1=np.array([])
i=0
while i != len(xo):
    j=0
    while j != len(yo):
        if x[i,j]==R and y[i,j]==0:
            Bx1=np.append(Bx1,0)
            j+=1
        else:
            Bx1=np.append(Bx1,Bx(x[i,j],y[i,j]))
            j+=1
    i+=1
Bx2=Bx1.reshape(len(xo),len(yo))

#---------------------------------------------------------------

By1=np.array([])

i=0
while i != len(xo):
    j=0
    while j != len(yo):
        if x[i,j]==R and y[i,j]==0:
            By1=np.append(By1,0)
            j+=1
        else:
            By1=np.append(By1,By(x[i,j],y[i,j]))
            j+=1
    i+=1
By2=By1.reshape(len(xo),len(yo))


#-------------------------------------------------------------------

plt.streamplot(x,y,Bx2,By2)
plt.show()

