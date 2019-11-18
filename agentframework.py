# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:33:11 2019

@author: gy19sr
"""

import random

class Agent:
    def __init__ (self, environment, agents, wolves, x, y): 
    #intialise have to do this anytime make an agent, setting its self to be the string
        self.x = x
        if (x == None):
            self.x = random.randint(0,99)
        else:
            self.x = x
        
        #print ("initising self.x to =", self.x)
        #(random.randint(0,99))
        self.y = y
        

        if (y == None):
            self.y = random.randint(0,99)
        else:
            self.y = y
        #print ("initising self.y to =", self.y)
        #(random.randint(0,99))
        self.environment = environment
        self.agents = agents
        self.wolves = wolves
        self.store = 0 
        self.neighbourhoods = 150
        
    def __str__(self):
    #letting it know it's a string
        return "Y=" + str(self.y) + ", X=" + str(self.x)
    
    def move(self): 
        
        closewolf = []
        for wolf in self.wolves:
            distance = self.distance_between(wolf)
            if distance <= self.neighbourhoods:
                metrics = []
                metrics.append(distance)
                metrics.append(wolf.x)
                metrics.append(wolf.y)
                closewolf.append(metrics)
        if (len(closewolf) > 0):
            # Move to the closest one
            closestwolf = min(closewolf)
            #print(closestSheep)
            if (self.x > closestwolf[1]):
                self.x = self.x + 3
            elif (self.x == closestwolf[1]):
                self.x == closestwolf[1]
                #donothing
            else:
                self.x = self.x - 3
            
            if (self.y > closestwolf[1]):
                self.y = self.y + 3
            elif (self.y == closestwolf[1]):
                #donothing
                self.y == closestwolf[1]
            else :
                self.y = self.y - 3

        
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1)
            
        if self.y < 0:
            self.y = 0

        if self.y > 200:
            self.y = 200
            
        if random.random() < 0.5:
            self.x = (self.x + 1) #% 280
        else:
            self.x = (self.x - 1) #%280
            
        if self.x < 0:
            self.x = 0
                    
        if self.x > 200:
            self.x = 200
            
            
    def eat(self): # makes eat environment
        #sharing with near neighbor, splitting between the two
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            
        #there stomach, the max they can eat
        if self.store >= 400:
            self.store = 400

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
#breeding
#    def Breed (self,neighbourhood)
    
                