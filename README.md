# Assessment_1
This is the first project for GEOG5990 at Leeds University

Student ID: 201378222


### List of Contents:
1. Model.py -- This is the main model that will be run
2. agentframework.py -- This is where code for the agents in the model are kept (essential to model)
3. in.txt -- This is the text file that holds the values for the environment (essential to model)
4. README.md -- This is what is currently being viewed, important details about the code and model within here
5. License -- This is the license agreement for the code within the repositry 
6. __pycache__ -- This is automatically generated folder, often kept hidden in repositories
  

### Prerequisites
Python 3.7
Anaconda3 (64bit) was used to make and test this model. 
The Spyder interface within Anaconda should be used to run the model. 


### Installing
install Anaconda3 with python 3.7 open Spyder. 
change settings for Ipython console in Spyder (Tools -> preferences -> backend -> Tkinter -> restart spyder).
If not done may be difficult to view animation
download whole repository to run model (model, in, agentframework are essential)	

## Instructions to run model:

1. Open "Model.py" in Spyder (Phthon).
2. Run model.
3. Full screen the pop up model window.
4. Use the slider to change the number of sheep. 
5. Then click the "change sheep amount" button.
6. Use the slider to change the number of wolves.
7. Then click the "change wolf amount" button.
8. Only once those are set should you then click the "Run Model" Button.
9. Once the model finishes you can click "quit".
10. The console will print if the stopping condition is met and number of iterations.

### Running the model again:
If wish to run model again, make sure you end the run by clicking the red square in console. Then restarting the kernal ensures that the model will run smoothly again 

### How it should run:
There should be an environment and two groups of agents. white are sheep and red are wolves. An animation will run where wolves will hunt down sheep and sheep will run away. When the wolves get close enough, they will eat the sheeps. The sheeps will consistantly eat grass and if they eat enough (500) the model will end and "stopping condition met" will be printed in the console. Otherwise the model will run until all iterations have been met. 

### known issues and what to avoid:

Not restarting the Kenal before restarting may cause spyder to stall. 
If any issue in running the model occurs, please email gy19sr@leeds.ac.uk. A response will be given within two working days.

### Licensing:
found on repository

###  End



