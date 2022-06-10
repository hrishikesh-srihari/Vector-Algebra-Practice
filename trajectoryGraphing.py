import time
from point import point
from matplotlib import pyplot as plt
import numpy as np
from numpy import pi
F_k=0.2
dt=0.018    
r=1
m=0.5
I = 2/5*m*r**2


def get_rot_energy(N):
    return(1/2*(N/I)**2 *I)
def get_move_energy(v):
    return(m/2*v**2) 

def draw_circle(p,line):    
    XX=[]
    YY=[]
    for phi in np.arange(3.14,-3.20,-0.1):
        XX.append(np.cos(phi)*r+p.x)
        YY.append(np.sin(phi)*r+p.y)
    plt.plot(XX,YY,line,linewidth = 2)
    
def kinematic(x,v,N):    
    h=N.rotatedUp()*(1/I)*r - v     
    F,err=h.norm()
    if err==1:
        F=point()
    F=F*-F_k

    N=N+F.rotatedDown()*r
    
    v=v+(F*dt)*(1/m)
    x=x+v*dt
    return [x,v,N]

for fr in np.arange(0.29,0.7,0.2):
    psi=np.arccos(1-fr)    
    phi = psi+pi/2
    N = point(-1, 0) *15
    V_init = point(np.cos(phi), np.sin(phi))*-1.1*np.cos(phi)
    x_start = point(np.cos(psi), np.sin(psi))*-2*r
    x = x_start
    v = V_init

    en=[]
    XX=[x_start.x]
    YY=[x_start.y-8]
    for t in range(600):    
        [x,v,N] = kinematic(x,v,N)
        en.append(get_move_energy(v.length()))
        XX.append(x.x)
        YY.append(x.y)
    plt.plot(XX,YY)
    plt.xlim((-9,3))
    plt.ylim((-5,9))
    
    draw_circle(x_start,'--')
    
draw_circle(point(),'')

plt.figure(2)
plt.plot(en)
plt.show()