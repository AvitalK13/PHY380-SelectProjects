# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 16:14:19 2022

@author: Avital
"""

import matplotlib.pyplot as plt
import math
import numpy as np

G = 6.6743*10**-11 #Nm^2/kg^2
ME = 5.97*10**24 #kg
MS = 1.99*10**30 #kg
MJ = 1.898*10**27 #kg

Xe0 = 1 #AU
Xj0 = 5.2 #AU
Xs0 = 0 #AU

xcm = (Xe0*ME + Xj0*MJ + Xs0*MS)/(ME + MJ + MS)

xe0 = Xe0 - xcm #AU
ye0 = 0 #AU
vxe0 = 0 #AU/year
vye0 = 2*math.pi #AU/year

xj0 = Xj0 - xcm #AU
yj0 = 0 #AU
vxj0 = 0 #AU
vyj0 = 2*math.pi*xj0/12

xs0 = Xs0 - xcm #AU
ys0 = 0 #AU
vxs0 = 0 #AU
vys0 = -(ME*vye0 + MJ*vyj0)/MS


#Convert AU to meter to adjust Fg
metertoau = (6.68*10**-12) #1 meter = this many AU

yeartosecond = (365.25*24*60*60) #1 year = this many seconds



def dxdt(vx):
    return vx

def dvedt(res, rej, xe, xj, xs):
    acceleration_si = -(G*MS*(xe-xs)*metertoau**2)/res**3 - (G*MJ*(xe-xj)*metertoau**2)/(rej**3)
    acceleration = acceleration_si*metertoau*yeartosecond**2
    return acceleration

def dydt(vy):
    return vy

def dvjdt(rjs, rej, xe, xj, xs):
    acceleration_si = -(G*MS*(xj-xs)*metertoau**2)/rjs**3 - (G*ME*(xj-xe)*metertoau**2)/(rej**3)
    acceleration = acceleration_si*metertoau*yeartosecond**2
    return acceleration

def dvsdt(res, rjs, xe, xj, xs):
    acceleration_si = -(G*ME*(xs-xe)*metertoau**2)/res**3 - (G*MJ*(xs-xj)*metertoau**2)/rjs**3
    acceleration = acceleration_si*metertoau*yeartosecond**2
    return acceleration

dt = 0.001 #years
time = np.arange(0,40+dt,dt) #years


xepos = []
yepos = []
xe, ye = xe0,ye0

xjpos = []
yjpos = []
xj, yj = xj0,yj0

xspos = []
yspos = []
xs, ys = xs0,ys0

for n in time:
    
    res = np.sqrt((xe-xs)**2 + (ye-ys)**2)
    rjs = np.sqrt((xj-xs)**2 + (yj-ys)**2)
    rej = np.sqrt((xe-xj)**2 + (ye-yj)**2)
    rs = np.sqrt(xs**2 + ys**2)
        
    
    vxe = vxe0 + dvedt(res,rej,xe,xj,xs)*dt
    vye = vye0 + dvedt(res,rej,ye,yj,ys)*dt
    
    
    xe = xe0 + dxdt(vxe)*dt
    
    ye = ye0 + dydt(vye)*dt
    
    xepos.append(xe0)
    
    yepos.append(ye0)
    
    xe0 = xe
    ye0 = ye
    vxe0 = vxe
    vye0 = vye
        
    
    vxj = vxj0 + dvjdt(rjs,rej,xe,xj,xs)*dt
    vyj = vyj0 + dvjdt(rjs,rej,ye,yj,ys)*dt
    
    
    xj = xj0 + dxdt(vxj)*dt
    
    yj = yj0 + dydt(vyj)*dt
    
    xjpos.append(xj0)
    
    yjpos.append(yj0)
    
    xj0 = xj
    yj0 = yj
    vxj0 = vxj
    vyj0 = vyj
    
    
    vxs = vxs0 + dvsdt(res, rjs, xe, xj, xs)*dt
    vys = vys0 + dvsdt(res, rjs, ye, yj, ys)*dt
    
    
    xs = xs0 + dxdt(vxs)*dt
    
    ys = ys0 + dydt(vys)*dt
    
    xspos.append(xs0)
    
    yspos.append(ys0)
    
    xs0 = xs
    ys0 = ys
    vxs0 = vxs
    vys0 = vys
    
plt.plot(xepos,yepos,label='Earth',marker='o',color='g')
plt.plot(xjpos,yjpos,label='Jupiter',marker='v',color='navy')
plt.plot(xspos,yspos,label='Sun',marker='*')
plt.title('Full Three-Body Problem')
plt.xlabel('x Position (AU)')
plt.ylabel('y Position (AU)')
plt.xlim(-6.5,6.5) #yes I know I hardcoded that oops
plt.ylim(-6.5,6.5)
plt.legend()
plt.show()