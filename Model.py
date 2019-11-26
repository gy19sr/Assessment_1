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
import wolfframework
#connects to the wolf framework file
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



neighbourhood = 5
#noticing distance between agents 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
#
ax = fig.add_axes([0, 0, 1, 1])
num_of_iterations = 100
#number of iterations


def setup():
    global num_of_agents
    num_of_agents = scale_sheep.get()
    #number of agents
    global num_of_wolves
    num_of_wolves = scale_wolves.get()
    #set number of wolves
    global wolves
    wolves = []
    global agents
    agents = []
    # Make the agents list
    #agents.append(agentframework.Agent(environment, agents, 50, 50))
    
    for i in range(num_of_agents):
    #
        y = int(td_ys[i].text)
        #
        x = int(td_xs[i].text)
        #
        agents.append(agentframework.Agent(environment, agents, wolves, x, y))
        #connects agents to the environment
        #print(agents[i])
     
    
    
    #make the wolves list
    #wolves.append(wolfframework.Wolf(environment, wolves, agents, 0, 0))
    
    
    for i in range(num_of_wolves):
    #    agents.append(agentframework.Wolf)
    #    wolves.append(agentframework.Wolf())
    #    x = random.randint(0,99)
        
    #    y = random.randint(0,99)
        x = random.randint(150,199)
        y = random.randint(0,50)
        wolves.append(wolfframework.Wolf(environment, wolves, agents, x, y))
        print ("wovles:", wolves[i])

#now define update function and incorporate below for animation

carry_on = True	
#allows for new interation to run

def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    matplotlib.pyplot.ylim(0,250)
    matplotlib.pyplot.xlim(0,250)
    
    matplotlib.pyplot.imshow(environment)
            
#    random.shuffle(agents)
        
    for i in range(len(wolves)):
        wolves[i].move()

    print(len(agents))
    
    for i in range(len(agents)):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)

        if agents[i].store >= 400:
        #setting stopping condition of max stomach storage 
        
            carry_on = False
            #stops iterations
            print("stopping condition met")
            #lets user know storages were filled
       
        
    for i in range(len(agents)):  
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='white')
        
    for i in range(len(wolves)):  
        matplotlib.pyplot.scatter(wolves[i].x,wolves[i].y,color='red')
    
    
 
    
    
    
    
def gen_function():
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
    for i in range(num_of_agents):
    #looking at all individual agents
        print("STORE: ",agents[i].store)     
        #list the final stomach content of the cows 
    for i in range(num_of_wolves):
        print ("wolves:", wolves[i])
#        print ("agents:", agents[])





def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    canvas.draw()
   
    
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

frame = tkinter.Frame(root)
frame.pack()


run_button = tkinter.Button(frame,
                   text="Run Model",
                   command=run)
run_button.pack(side=tkinter.LEFT)



scale_sheep = tkinter.Scale(root, from_=1, to_= 100, orient='horizontal')
scale_sheep.pack()

button = tkinter.Button(root, text="change sheep amount", command=setup)
button.pack()


scale_wolves = tkinter.Scale(root, from_=1, to_= 10, orient='horizontal')
scale_wolves.pack()

button = tkinter.Button(root, text="change wolf amount", command=setup)
button.pack()







quit_button = tkinter.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=root.destroy)
quit_button.pack(side=tkinter.LEFT)


menubar = tkinter.Menu(root)
root.config(menu=menubar)
model_menu = tkinter.Menu(menubar)
menubar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run, state="normal") 


#w = tkinter.Canvas(root, width=200, height=200)
#w.pack()

root.mainloop()
tkinter.mainloop()
