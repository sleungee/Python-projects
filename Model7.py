
import random
import matplotlib
def distance (agent1, agent2):
    y_diff = (agent1[0] - agent2[0])
    y_diffsq = y_diff * y_diff
    x_diff = (agent1[1] - agent2[1])
    x_diffsq = x_diff * x_diff
    sum = y_diffsq + x_diffsq
    answer = sum**0.5
    print(answer)
    return answer
#this is for creating the raster "environment" in the grid where the 'agents' will be be animated in. 
import csv
data = []
f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []
    for value in row:				# A list of value
        rowlist.append(value) 				# Floats
    data.append(rowlist)
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.

matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()
"""
# Initialise x0 and y0
#x0=50
#y0=50
y0 = random.randint(0,99)
x0 = random.randint(0,99)

# Randomly move y0
random_number = random.random()
print (random_number)
if random_number < 0.5:
    y0 = y0 + 1
else:
    y0 = y0 - 1
print (y0)

# Randomly move x0
random_number=random.random()
print (random_number)
if random_number < 0.5:
    x0 = x0 + 1
else:
    x0 = x0 - 1
print (x0)

# Initialise x1 and y1
#x1=50
#y1=50
y1 = random.randint(0,99)
x1 = random.randint(0,99)

# Randomly move y0
random_number = random.random()
print (random_number)
if random_number < 0.5:
    y1 = y1 + 1
else:
    y1 = y1 - 1
print (y1)

# Randomly move x1
random_number=random.random()
print (random_number)
if random_number < 0.5:
    x1 = x1 + 1
else:
    x1 = x1 - 1
print (x1)

#assigning container for our agents

#assigning agents (coordinates)
#agents.append([y0,x0])
#agents.append([y1,x1])
#agents.append([random.randint(0,99),random.randint(0,99)])
#showing the agents in text. agents [0][1]-means agent number 1 part1
#print(agents)
#print(agents[0])
#print(agents[0][0])
#print(agents[0][1])
##print(agents[0][2])
#
#print(agents[1])
#print(agents[1][0])
#print(agents[1][1])
#print(agents[2])
#print(agents[2][0])
#print(agents[2][1])

#matplotlib.pyplot.ylim(0, 99)
#matplotlib.pyplot.xlim(0, 99)
#matplotlib.pyplot.scatter(agents[0][1],agents[0][0],color='red')
#matplotlib.pyplot.scatter(agents[1][1],agents[1][0])
#matplotlib.pyplot.scatter(agents[2][1],agents[2][0])
#matplotlib.pyplot.show()
"""
import (Agent_Framework)


#generating multyple agents in a loop
agents = []
num_of_agents = 10
for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

max_distance = distance(agents[0], agents[1])
print("fdsafds")


for i in range (0, num_of_agents):
    print("i", i)
    for j in range (0, num_of_agents):
        print("j", j)
        print("i", i, "j", j)
        if (i < j):
            dist = distance(agents[i], agents[j])
            if (dist > max_distance):
                max_distance = dist
                print("max_distance", max_distance)


print("max_distance", max_distance)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color='red')

"""
# move the agents once
for i in range (num_of_agents):
    #change the y value of the agent...
    random_number=random.random()
    if random_number < 0.5:
        agents[i][0] = agents[i][0] + 1
    else:
        agents[i][0] = agents[i][0] - 1
    # change the x value of the agent...
    random_number=random.random()
    if random_number < 0.5:
        agents[i][1] = agents[i][1] + 1
    else:
        agents[i][1] = agents[i][1] - 1    
"""

# move the agents multiple times
num_of_moves = 130

for t in range (num_of_moves):   
    for i in range (num_of_agents):
        #change the y value of the agent...
        random_number=random.random()
        if random_number < 0.5:
            agents[i][0] = agents[i][0] + 1
        else:
            agents[i][0] = agents[i][0] - 1
        # change the x value of the agent...
        random_number=random.random()
        if random_number < 0.5:
            agents[i][1] = agents[i][1] + 1
        else:
            agents[i][1] = agents[i][1] - 1

      
print(agents)



for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color='black')
#matplotlib.pyplot.show(agents)

for i in range (num_of_agents):
    (agents [i] [1] +1,agents[i][0] +1)    

 