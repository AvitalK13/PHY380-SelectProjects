# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 09:53:44 2022

@author: Avital
"""

import random
import numpy as np
import matplotlib.pyplot as plt

class coffee():
    '''A cup of coffee for which we can track cream particles'''
    def __init__(self,nparticles):
        self.nparticles = nparticles
        self.x = np.zeros(nparticles)
        self.y = np.zeros(nparticles)
        
    def updatePosition(self):
        '''Update the position of all cream particles using a random number'''
        for i in np.arange(self.nparticles):
            
            r = np.sqrt(self.x[i]**2 + self.y[i]**2)
            
            if r > 100:
                self.x[i] = self.x[i]
                self.y[i] = self.y[i]
                
            else:
                self.x[i] = self.x[i] + random.uniform(-1,1)
                self.y[i] = self.y[i] + random.uniform(-1,1)
            
                if self.x[i] > 100:
                    self.x[i] = 100
                    
                if self.x[i] < -100:
                    self.x[i] = -100
                    
                if self.y[i] > 100:
                    self.y[i] = 100
                    
                if self.y[i] < -100:
                    self.y[i] = -100
            
    def plotDistribution(self,loc):
        '''Plot the distribution given a subplot location'''
        plt.subplot(loc)
        plt.scatter(self.x,self.y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.xlim(-150,150)
        plt.ylim(-150,150)
        

nps = 500 #number of particles
newCup = coffee(nps)

print(newCup.__doc__)

#a = [4,3,5]
#(a.__doc__)

t = 0
tmax = 10000
loc = 221
while t < tmax:
    newCup.updatePosition()
    if t % 100 == 0:
        print(t)
        
    if t == 0 or t == 100 or t == 1000 or t == tmax-1:
        newCup.plotDistribution(loc)
        loc += 1
    t += 1

plt.savefig('coffee.png')

