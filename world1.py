import random

def single_random_scoop(pool):
    dict = pool.supply
    summer = sum(dict.values())
    rand_val = random.randint(1,summer)
    total = 0
    for k, v in dict.items():
        total += v
        if rand_val <= total:
            return k

def multi_scoop(pool, to_pool, size):
    for x in range(size):
        if sum(pool.supply.values()) == 0:
            break
        scooped = single_random_scoop(pool)
        pool.supply[scooped] -= 1
        to_pool.supply[scooped] += 1

def transfer(original_pool, new_pool, resource, quantity):
    original_pool.supply[resource] -= quantity
    new_pool.supply[resource] += quantity

class Timeline1:
    def __init__(self):
        self.year = 0
        self.day = 0
        self.hour = 0
        self.minute = 0

    def add_minute(self):
        if self.minute < 99:
            self.minute += 1
        else:
            self.minute = 0
            if self.hour < 7:
                self.hour += 1
            else:
                self.hour = 0
                if self.day < 399:
                    self.day += 1
                else:
                    self.day = 0
                    self.year += 1


class region:
    def __init__(self):
        self.id = 1
        self.supply = {'a':0, 'b':0, 'c':0}
        self.region = {'vertical':0, 'time':1}
        self.location = [(-500, 500), (500, 1500), (500, 1500)]
        self.state = 'Liquid'
        self.population = []

    def apply_sunlight(self, timeline):
        tod_bonus = abs(4-timeline.hour)
        season_bonus = abs(200 - timeline.day)

class Character1:
    def __init__(self):
        self.id = 1
        self.age = 0
        self.dna = {'reckon_cost':{'a':2, 'b': 2, 'c':2}, 'scoop size': 10, 'actions per reckon': 1, 'total storage': 1000 }
        self.reckoning_rate = 1
        self.reckoning_cost = self.dna['reckon_cost']
        self.scoop_size = self.dna['scoop size']
        self.actions_per_reckon = self.dna['actions per reckon']
        self.scoop_type = 'Random'
        self.supply = {'a': 100, 'b': 100, 'c': 100}
        self.total_storage = self.dna['total storage']
        self.location = [0,0,0]
        self.direction = 0
        self.speed = {'Swim':3, 'Fast swim': 5, 'Walk': 2, 'Run': 4, 'Fly' :0, 'Dig': 0}

    def reckon(self, habitat, void):
        self.age += 1
        subtracted = {key: self.supply[key] - self.reckoning_cost[key] for key in dict.keys()
                      if key in self.reckoning_cost[key].keys()}
        alive = all(value >= 0 for value in subtracted.values())
        if alive:
            transfer(self,void,'a',2)
            transfer(self,void,'b',1)
            transfer(self,habitat,'b',1)
            transfer(self,habitat,'c',2)
            self.select_action(habitat)

    def select_action(self, habitat):
        if self.age % 100 == 1:
            self.replicate(habitat)
        elif any(value < 100 for value in self.supply) and sum(self.supply.values()) < (
            self.total_storage - self.scoop_size):
            self.scoop(habitat)
        elif (self.supply['a'] / 2) >= self.supply['b']:
            self.convert()

    def replicate(self, habitat):
        halved_supply = {k: int(v / 2) for k, v in self.supply.items()}
        new_char1 = Character1()
        self.supply = halved_supply
        new_char1.supply = halved_supply


    def scoop(self, habitat):
        multi_scoop(habitat, self, self.scoop_size)

    def convert(self):
        n=0
        while self.supply['a'] > 40 and n < 20:
            self.supply['a'] -= 1
            self.supply['b'] += 1
            n+=1

    def move(self):
        change = random.randint(1,40)
        if change in [4]:
            self.direction = 0
        if change in [6]:
            self.direction = 1
        if change in [8]:
            self.direction = 2
        if change in [9]:
            self.direction = 3
        if change in [12]:
            self.direction = 4
        if change in [13]:
            self.direction = 5








pool1 = Habitat1()
