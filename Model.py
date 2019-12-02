# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 15:29:58 2019

@author: gy19sr
"""

import matplotlib
#allows to make plots
matplotlib.use('TkAgg')
#
import tkinter

#allows set up of GUI window
#import operator
import matplotlib.pyplot
#allows plots to be created
#import matplotlib.pyplot as plt
#import matplotlib.cm as cm
import random
import agentframework
#connects to the agentframework file
#import wolfframework
#connects to the wolf framework file if wish to view sep, just switch the wolf append
import csv
#allows for csv files to be added
import matplotlib.animation 
#allows for animation in plots
import requests
#allows to take info from internet
import bs4
#allows to use functions to read html data





r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
#gets html from the website used in 'web scraping' prac
content = r.text
#taking the text from the web link above
soup = bs4.BeautifulSoup(content, 'html.parser')
#setting up the website data to be readible 
td_ys = soup.find_all(attrs={"class" : "y"})
#setting the y coordinates 
td_xs = soup.find_all(attrs={"class" : "x"})
#setting x coordinate

#print(td_ys)
#print(td_xs)






f = open('in.txt', newline='') 
#open the csv file in working directory
    

reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#each row is returned as a list of strings


#create environment then put in lots of rows
environment = []
#this makes an environment list


for row in reader:				# A list of rows
    # Lines here happen before each row is processed
    rowlist = []
    # means environment made up of rowlists
    for value in row:				# A list of value
        # do something with values.
        rowlist.append(value)
        #at end of list put a value
        
    
    environment.append(rowlist)
    #stops from filling up on just one rowlist

f.close() 
#done looking at CSV




#intial set up of wolves, agents, iterations, neighborhood

neighbourhood = 5
#noticing distance between agents 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#setting up fig size
ax = fig.add_axes([0, 0, 1, 1])
#setup figure axis
num_of_iterations = 100
#number of iterations






def setup():
#this is done to allow for connection with scale bar
    global num_of_agents
    #global allows to be seen outside of def function, agents=sheep 
    num_of_agents = scale_sheep.get()
    #number of agents, connecting with scale bar
    global num_of_wolves
    #number of wolves
    num_of_wolves = scale_wolves.get()
    #set number of wolves
    global wolves
    #make wolves global
    wolves = []
    #makes wolves list
    global agents
    #makes agents global
    agents = []
    # Make the agents list
    
    for i in range(num_of_agents):
    #setting x y for sheep
        y = int(td_ys[i].text)
        #grabing text from html
        x = int(td_xs[i].text)
        #grabing text from html
        agents.append(agentframework.Agent(environment, agents, wolves, x, y))
        #connects agents to the environment, and grabs from framework
        #print(agents[i])
    
    
    for i in range(num_of_wolves):
    #seeting up num of wolves
        x = random.randint(150,199)
        #seting wolves random starting x coordinate
        y = random.randint(0,50)
        #setting agents random y starting points
        wolves.append(agentframework.Wolf(environment, wolves, agents, x, y))
        #connects agents to the environment, and grabs from framework
        #print ("wovles:", wolves[i])
        








#now define update function and incorporate below for animation

carry_on = True	
#allows for new interation to run

def update(frame_number):
#each fram of the animation    
    fig.clear()
    #clear figure
    global carry_on
    #carry on with new frame
    matplotlib.pyplot.ylim(0,250)
    #plot size
    matplotlib.pyplot.xlim(0,250)
    #plot size
    matplotlib.pyplot.imshow(environment)
    #display environment

        
    for i in range(len(wolves)):
    #setting wolves movement
        wolves[i].move()
        #move wolves

    #print(len(agents))
    
    for i in range(len(agents)):
    #what the agents do each iteration
        agents[i].move()
        #move agents
        agents[i].eat()
        #agents eat
        agents[i].share_with_neighbours(neighbourhood)
        #agents share with other agents

        if agents[i].store >= 600:
        #setting stopping condition of max stomach storage 
        
            carry_on = False
            #stops iterations
            print("stopping condition met")
            #lets user know storages were filled
       
        
    for i in range(len(agents)):  
    #for agents
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='white')
        #plot agents each frame and make them white
    for i in range(len(wolves)):  
    #for wolves
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y,color='red')
        #plot wolves each fram and make them red
    
    
 
    
    
    
    
def gen_function():
#seting up to run a new iteration
    a = 0
    global carry_on
    #Not actually needed as we're not assigning, but clearer
    while (a < num_of_iterations) & (carry_on) :
    #if under the requested iterations and stopping condition not met ...
        yield a			
        # Returns control and waits next call.
        a = a + 1   
        #conduct a new iteration
    print("stopping iteration num", a)
     #print how many iterations were run  
    #for i in range(num_of_agents):
        #print("STORE: ",agents[i].store)     
   #for i in range(num_of_wolves):
        #print ("wolves:", wolves[i])
        






def run():
#define run fucntion to run final model
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    #what is to be animated
    canvas.draw()
    #display canvas
   
    
root = tkinter.Tk()
#setting root
root.wm_title("Model")
#root title
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
#what should be displayed on the canvas, make sure correct backend ikinter is set in spyder
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
#pack the canvas



frame = tkinter.Frame(root)
#set frame
frame.pack()
#pack the frame


run_button = tkinter.Button(frame,
#new run button 
                   text="Run Model",
                   command=run)
#button runs model
run_button.pack(side=tkinter.LEFT)
#place button left side


scale_sheep = tkinter.Scale(root, from_=1, to_= 100, orient='horizontal')
#set sheeps scale bar
scale_sheep.pack()
#pack the scale bar


button = tkinter.Button(root, text="change sheep amount", command=setup)
#take the scalebar number as the number of agents 
button.pack()

scale_wolves = tkinter.Scale(root, from_=1, to_= 10, orient='horizontal')
#set scale bar for wolves
scale_wolves.pack()

button = tkinter.Button(root, text="change wolf amount", command=setup)
#take the scalebar number as the number of wolves
button.pack()




quit_button = tkinter.Button(frame, 
#quit button 
                   text="QUIT", 
                   fg="red",
                   command=root.destroy)
#clicking destroys the root
quit_button.pack(side=tkinter.LEFT)
#place button next to run 

menubar = tkinter.Menu(root)
#set up menubar
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
#puts an optional second run method
model_menu.add_command(label="Run model", command=run, state="normal") 



root.mainloop()
tkinter.mainloop()
#end of tkinter 
#end of model