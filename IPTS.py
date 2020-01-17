import numpy as  np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import math
import random 

def nhood_n_dim(point,delta_x):
    neighbors = []
    # 1-dimension
    if len(point) == 1:
        neighbors.append([point[0] - delta_x])  # left
        neighbors.append([point[0]])  # current
        neighbors.append([point[0] + delta_x])  # right

        return neighbors

    # n-dimensional
    for sub_dimension in nhood_n_dim(point[1:],delta_x):
        neighbors.append([point[0] - 1] + sub_dimension)  # left
        neighbors.append([point[0]] + sub_dimension)  # center
        neighbors.append([point[0] + 1] + sub_dimension)  # right

    return neighbors   

def contains(pt, TL,eps):
    for i in TL:
        out = []
        for j in range(len(pt)):
            out.append(abs(pt[j]-i[j])<eps)
        if all(out):
            return True
    return False
def satisfies(point, con):
    for function in con:
        if(not function(point)):
            return False
    return True
def get_best(nhood,f,c):
    minimum = nhood[0]
    j = 0
    for i in nhood:
        if f(i)<f(minimum) and satisfies(i,c):
            minimum = i
        else:
            j+=1
    if j == len(nhood):
        for i in nhood:
            if satisfies(i,c):
                return i
    return minimum
    
def TS(f, x_0, dx, N, eps, L, c):
    bp = x_0
    bp_cand = x_0
    TL = []
    TL.append(x_0)
    iteration = 0
    neighbors=[];
    while (iteration<N):
        neighbors = nhood_n_dim(bp_cand,dx)
        neighbors.remove(bp_cand)
        j=0
        for cand in neighbors :
            a=satisfies(cand,c)
            b=not contains(cand, TL,eps)
            d=f(cand)<f(bp_cand)
            if(a and b and d):
                bp_cand = cand 
            else:
                j+=1
        if j==len(neighbors):
            kand = get_best(neighbors,f,c)
            bp_cand = kand
        if(f(bp_cand)<f(bp)):
            bp = bp_cand
        TL.append(bp_cand)
        if(len(TL)>L):
            TL.remove(TL[0])
        iteration+=1
    return bp

def f1(s):
    return (s[0]-3)*(s[0]-3)+(s[1]+1)*(s[1]+1)

def f2(s):
    return (1-s[0])*(1-s[0])+100*(s[1]-s[0]*s[0])*(s[1]-s[0]*s[0])

def f3(s):
    return 20+(s[0]*s[0]-10*np.cos(2*np.pi*s[0]))+(s[1]*s[1]-10*np.cos(2*np.pi*s[1]))

def f4(s):
    return -abs( np.sin(s[0])*np.cos(s[1])*np.exp( abs(1-(np.sqrt(s[0]*s[0]+s[1]*s[1]))/(np.pi)) ) )


r_1 = lambda x: -x[0]+x[1]-10<=0
r_2 = lambda x: 0.5*x[0]+x[1]-10<=0
r_3 = lambda x: x[1]>=-1
r_4 = lambda x: x[0]>=-1

constr = [r_1,r_2,r_3,r_4]

izlaz1 = TS(f1,[5,5],1,1000,0.0001,10, constr)
print("TS: ", f1(izlaz1), ", Tacka: ", izlaz1)



izlaz2 = TS(f2,[5,5],1,1000,0.0001,10, constr)
print("TS: ", f2(izlaz2), ", Tacka: ", izlaz2)



izlaz3 = TS(f3,[5,5],1,1000,0.0001,10, constr)
print("TS: ", f3(izlaz3), ", Tacka: ", izlaz3)




izlaz4 = TS(f4,[5,5],1,1000,0.0001,10,constr)
print("TS: ", f4(izlaz4), ", Tacka: ", izlaz4)


x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f1([X1, X2])
fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour(X1, X2, Y, 50, cmap='binary')
ax.scatter(izlaz1[0], izlaz1[1], f1(izlaz1), s=75,color='blue', marker='x') 
ax.set_xlabel('$x$') 
ax.set_ylabel('$y$') 
ax.set_zlabel('$f(x,y)$') 

plt.show()

x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f2([X1, X2])
fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour(X1, X2, Y, 50, cmap='binary') 
ax.scatter(izlaz2[0], izlaz2[1], f2(izlaz2), s=75,color='blue', marker='x') 
ax.set_xlabel('$x$') 
ax.set_ylabel('$y$') 
ax.set_zlabel('$f(x,y)$') 
plt.show()


x1 = np.linspace(-5, 5, 100)
x2 = np.linspace(-5, 5, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f3([X1, X2])
fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour(X1, X2, Y, 50, cmap='binary') 
ax.scatter(izlaz3[0], izlaz3[1], f3(izlaz3), s=75,color='blue', marker='x') 
ax.set_xlabel('$x$') 
ax.set_ylabel('$y$') 
ax.set_zlabel('$f(x,y)$') 
plt.show()

x1 = np.linspace(-10, 10, 100)
x2 = np.linspace(-10, 10, 100)
X1, X2 = np.meshgrid(x1, x2)
Y = f4([X1, X2])
fig = plt.figure() 
ax = plt.axes(projection='3d') 
ax.contour(X1, X2, Y, 50, cmap='binary') 
ax.scatter(izlaz4[0], izlaz4[1], f4(izlaz4),s=75, color='blue', marker='x') 
ax.set_xlabel('$x$') 
ax.set_ylabel('$y$') 
ax.set_zlabel('$f(x,y)$') 
plt.show()