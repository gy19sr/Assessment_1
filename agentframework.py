# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:33:11 2019

@author: gy19sr
"""


#this is the framework for the sheep

import random
#allows random function


class Agent:
    def __init__ (self, environment, agents, wolves, x, y): 
    #intialise have to do this anytime make an agent, setting its self to be the string
        self.x = x
        #x = x (taking from webscraping in model) 
        if (x == None):
            self.x = random.randint(0,99)
            #if no value then x is random
        else:
            self.x = x
        #print ("initising self.x to =", self.x)

        self.y = y
       #y = y (taking from webscraping in model)                                   

        if (y == None):
            self.y = random.randint(0,99)
            #if no value then y is random
        else:
            self.y = y
        #print ("initising self.y to =", self.y)
        self.environment = environment
        self.agents = agents
        self.wolves = wolves
        self.store = 0 
        #intial storage
        self.neighbourhoods = 80
        #how far sheep can see
        
    def __str__(self):
    #letting it know it's a string
        return "Y=" + str(self.y) + ", X=" + str(self.x)
    
    def move(self): 
    #setting up sheeps movements    
        closewolf = []
        #create list for close wolves
        for wolf in self.wolves:
            distance = self.distance_between(wolf)
            if distance <= self.neighbourhoods:
                metrics = []
                metrics.append(distance)
                metrics.append(wolf.x)
                metrics.append(wolf.y)
                closewolf.append(metrics)
                #set closewolf x, y, and distance between
        if (len(closewolf) > 0):
            # Move to the closest one
            closestwolf = min(closewolf)
            #print(closestSheep)
            if (self.x > closestwolf[1]):
                self.x = self.x + 2
                #if father x than the cloest wolf keep going way
            elif (self.x == closestwolf[1]):
                self.x == closestwolf[1]
                #donothing
            else:
                self.x = self.x - 1
                #if father left x than the cloest wolf keep going left
            if (self.y > closestwolf[1]):
                self.y = self.y + 3
                #if higher than close wolf keep heading up
            elif (self.y == closestwolf[1]):
                #donothing
                self.y == closestwolf[1]
            else :
                self.y = self.y - 1
                #if lower than wolf keep heading down

        
        #below means move randomly if no wolves seen 
        
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1)
        #move up or down one randomly
        if self.y < 0:
            self.y = 0
        #setting lower fence boundary
        if self.y > 250:
            self.y = 250
        #setting upper fence boundary
        if random.random() < 0.5:
            self.x = (self.x + 1) #% 280
        else:
            self.x = (self.x - 1) #%280
        #move left or right one randomly    
        if self.x < 0:
            self.x = 0
        #setting lower x boundary
        if self.x > 250:
            self.x = 250
        # setting upper x boundary
            
            
    def eat(self): # makes eat environment
        #eat food from the environment taking a value of 10 at a time
        if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10
            #add food to storage 
            
        #there stomach, the max they can eat
        if self.store >= 605:
            self.store = 605

    def distance_between (self, agent):
        #make distance between defintion
        return (((self.x - agent.x)**2) +
                ((self.y - agent.y)**2))**0.5

            
    def share_with_neighbours (self,neighbourhood):
        #defining sharing food with neighboring agents
        self.neighbourhood = neighbourhood
        for agent in self.agents:
            distance = self.distance_between(agent)
            if distance <= neighbourhood:
                #if within neighborhood then share food averaged out between them
                summary = self.store + agent.store
                average = summary / 2
                self.store = average
                agent.store = average


class Wolf:
#making a new class for the wolves
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
        #how far the wolves can see
        
    def __str__(self):
    #letting it know it's a string
        return str(self.y) + " " + str(self.x)
    
    def move(self): 
        # Are there any sheep near?
        closeSheep = []
        #setting up a list for closest sheep
        for sheep in self.sheeps:
            distance = self.distance_between(sheep)
            if distance <= self.neighbourhood:
                metrics = []
                metrics.append(distance)
                metrics.append(sheep.x)
                metrics.append(sheep.y)
                closeSheep.append(metrics)
                #closets sheep now has distance, x, and y
        if (len(closeSheep) > 0):
            # Move to the closest one
            closestSheep = min(closeSheep)
            #print(closestSheep)
            if (self.x > closestSheep[1]):
                self.x = self.x - 5
            elif (self.x == closestSheep[1]):
                self.x == closestSheep[1]
                #donothing
            else:
                self.x = self.x + 5
            
            if (self.y > closestSheep[2]):
                self.y = self.y - 5
            elif (self.y == closestSheep[2]):
                #donothing
                self.y == closestSheep[2]
            else :
                self.y = self.y + 5

            if closestSheep[0] < 15:
            #if wolf close to sheep
                for sheep in self.sheeps:
                    if sheep.x == closestSheep[1] and sheep.y == closestSheep[2]:
                    #relate the two sheep lists 
                        self.sheeps.remove(sheep)
                        #remove the sheep
                        break
                    
                    
        #below means move randomly if no sheep seen 
        
        if random.random() < 0.5:
            self.y = (self.y + 1) 
        else:
            self.y = (self.y - 1)
        #move up or down one randomly
        if self.y < 0:
            self.y = 0
        #setting lower fence boundary
        if self.y > 250:
            self.y = 250
        #setting upper fence boundary
        if random.random() < 0.5:
            self.x = (self.x + 1) #% 280
        else:
            self.x = (self.x - 1) #%280
        #move left or right one randomly    
        if self.x < 0:
            self.x = 0
        #setting lower x boundary
        if self.x > 250:
            self.x = 250
        # setting upper x boundary

    def distance_between (self, agent):
        return (((self.x - agent.x)**2) +
                ((self.y - agent.y)**2))**0.5

