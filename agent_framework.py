import random
class Agent (object):
    def __init__ (self):
        self.x = random.randint(0,99)
        self.y = random.randint(0,99)

    def move(self):
        random_number=random.random()
        if random_number < 0.5:
            self.y = self.y + 1
        else:
            self.y = self.y - 1
    
    random_number=random.random()
    if random_number < 0.5:
            self.x = self.x + 1
    else:
        self.x = self.x - 1

    def eat(self): # can you make it eat what is left?
        if self.environment[self.y][self.x] > 10:
        self.environment[self.y][self.x] -= 10
        self.store += 10

    