# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:49:59 2019

@author: gy19sr
"""

import random

class Wolf:
    def __init__ (self, environment, wolves, sheeps, x, y): 
    #intialise have to do this anytime make an agent, setting its self to be the string
        self.x = x
        #print ("initising self.x to =", self.x)
        self.y = y
        #print ("initising self.y to =", self.y)
        #(random.randint(0,99))
        self.environment = environment
        self.wolves = wolves
        self.store = 0 
        self.sheeps = sheeps
        self.neighbourhood = 150
        
    def __str__(self):
    #letting it know it's a string
        return str(self.y) + " " + str(self.x)
    
    def move(self): 
        # Are there any sheep near?
        closeSheep = []
        for sheep in self.sheeps:
            distance = self.distance_between(sheep)
            if distance <= self.neighbourhood:
                metrics = []
                metrics.append(distance)
                metrics.append(sheep.x)
                metrics.append(sheep.y)
                closeSheep.append(metrics)
        if (len(closeSheep) > 0):
            # Move to the closest one
            closestSheep = min(closeSheep)
            #print(closestSheep)
            if (self.x > closestSheep[1]):
                self.x = self.x - 3
            elif (self.x == closestSheep[1]):
                self.x == closestSheep[1]
                #donothing
            else:
                self.x = self.x + 3
            
            if (self.y > closestSheep[2]):
                self.y = self.y - 3
            elif (self.y == closestSheep[2]):
                #donothing
                self.y == closestSheep[2]
            else :
                self.y = self.y + 3

            if closestSheep[0] < 20:
                for sheep in self.sheeps:
                    if sheep.x == closestSheep[1] and sheep.y == closestSheep[2]:
                        self.sheeps.remove(sheep)
                        break
        else:
            # Otheriwise move randomly
            if random.random() < 0.5:
                self.y = (self.y + 2) #% 280
            else:
                self.y = (self.y - 2) #% 280 
                
            if self.y < 0:
                self.y = 0
                
            if self.y > 200:
                self.y = 200
                
            if random.random() < 0.5:
                self.x = (self.x + 2) #% 280
            else:
                self.x = (self.x - 2) #%280
                
            if self.x < 0:
                self.x = 0
                
            if self.x > 200:
                self.x = 200                   
        
            
    def eat(self): # makes eat environment
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

    def distance_between (self, agent):
        return (((self.x - agent.x)**2) +
                ((self.y - agent.y)**2))**0.5

            
    def share_with_neighbours (self,neighbourhood):
        self.neighbourhood = neighbourhood
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                summary = self.store + agent.store
                average = summary / 2
                self.store = average
                agent.store = average
                