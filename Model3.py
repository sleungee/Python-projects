
import random
import matplotlib
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
#generating multyple agents in a loop
agents = []
num_of_agents = 3
for i in range (num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])
print(agents)

matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.xlim(0, 99)
for i in range (num_of_agents):
    matplotlib.pyplot.scatter(agents[i][1],agents[i][0],color='red')

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

    
