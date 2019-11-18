# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 13:24:50 2019

@author: gy19sr
"""
import random

class Agent():
    def __init__ (self, environment, agents, x, y): 
    #intialise have to do this anytime make an agent, setting its self to be the string
        pass
        
        
    def __str__(self):
    #letting it know it's a string
        return "Y=" + str(self.y) + ", X=" + str(self.x)
    
    def move(self): 
        
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1)
            
        if self.y < 0:
            self.y = 0

        if self.y > 100:
            self.y = 100
            
        if random.random() < 0.5:
            self.x = (self.x + 1) 
        else:
            self.x = (self.x - 1) 
            
        if self.x < 0:
            self.x = 0
                    
        if self.x > 100:
            self.x = 100
            
            
class Sheep(Agent):
    def __init__(self, environment, agents, x, y):
#        super().__init__()
        self.x = x 
        #print ("initising self.x to =", self.x)
        self.y = y 
        #print ("initising self.y to =", self.y)
        #(random.randint(0,99))
        self.environment = environment
        self.store = 0 
        self.sheeps = sheeps
        self.neighbourhood = 5
        
    def move(self):
        self.x += 1
        self.y += 1
        
    def share_with_neighbours (self,neighbourhood):
        self.neighbourhood = neighbourhood
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                summary = self.store + agent.store
                average = summary / 2
                self.store = average
                agent.store = average
                
                
class Wolf(Agent):
    def __init__(self, environment, agents, x, y):
        self.x = x
        if (x == None):
            self.x = random.randint(0,99)
        else:
            self.x = x
            
        self.y = y
        if (y == None):
            self.y = random.randint(0,99)
        else:
            self.y = y

    
    