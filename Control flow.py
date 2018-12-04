# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 16:11:11 2018

@author: gy18stl
"""
import matplotlib
import random
import csv
f = open('data.csv', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    for value in row:				# A list of value
        print(value) 				# Floats
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.



agents = []
num_of_agents = 10
for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color='red')

print(agents)
# for every agent...
for i in range (num_of_agents):
    #move the agent..
    #change y value...
    random_number = random.random()
    if random_number < 0.5:
        agents[i][0] = agents[i][0] + 1 
    else:
        agents[i][0] = agents[i][0] - 1
    #change xvalue...
    if random_number < 0.5:
        agents[i][1] = agents[i][1] + 1 
    else:
        agents[i][1] = agents[i][1] - 1
    
    
    
    #(agents [i] [1] +1,agents[i][0] +1)    
print(agents)   
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color='black')
matplotlib.pyplot.show()