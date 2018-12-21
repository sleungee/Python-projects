import random
class Agent ():
    #this is the self/being. You're creating the character of the agent
    def __init__(self, environment, agents):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)
        self.store = 0
        self.environment = environment
        self.agents = agents
        
#defining how to move it
    def move(self):
        random_number=random.random()
        if random_number < 0.5:
            self.y = (self.y + 1) % 100
        else:
            self.y = (self.y - 1) % 100
    
        random_number=random.random()
        if random_number < 0.5:
            self.x = (self.x + 1) % 100
        else:
            self.x = (self.x - 1) % 100
            
#what's it allowed to do.
            
'''eating the environment. In this we give the agent the ability to interact with the given environment, in this
case it will act as the food for the agents. It defines the action of Def eat [define eat] function.''' 

def eat(self): 
   if self.environment[self.y][self.x] > 10:
            self.environment[self.y][self.x] -= 10
            self.store += 10

''' this gives the ability for the agents to calculate the distance between each other, this will be 
useful later on in the framework.'''
 
def distance_between(self, agent):
        return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5

'''Here gives the example of communication between the agents, we chose to show this with them sharing
the food they collected.'''
 
def share_with_neighbours(self, neighbourhood) :
    for Agent in self.agents:
            distance = self.distance_between(Agent)
            if distance <= neighbourhood:
                sum = self.store + Agent.store
                ave = sum /2
                self.store = ave 
                Agent.store = ave 
                print("sharing " + str(distance) + " " + str(ave)) 

    
    
