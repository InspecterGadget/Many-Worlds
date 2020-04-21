import random
import matplotlib.pyplot as plt
import numpy as np

def single_random_scoop(pool):
    dict = pool.supply
    summer = sum(dict.values())
    rand_val = random.randint(1,summer)
    total = 0
    for k, v in dict.items():
        total += v
        if rand_val <= total:
            return k

def resources_over_time_graph(tl,rg,interval, iterations,resource_type):
    total_sun_over_time = []
    time = []
    for x in range(iterations):
        for i in range(interval):
            tl.add_minute()
        rg.apply_sunlight(tl)
        a_maper = np.array(rg.make_squares_supply_map(resource_type))
        sumer = np.sum(a_maper)
        total_sun_over_time.append(sumer)
        time.append(x)
    plt.scatter(time, total_sun_over_time)
    plt.show()

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

def fill_region_basic(region):
    squares_list = []
    for row in range(0, 100):
        for column in range(0, 100):
            new = Single_square()
            new.location = [row, column]
            squares_list.append(new)
    region.squares = squares_list

class Timeline:
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


class Region:
    def __init__(self):
        self.squares = []

    def apply_sunlight(self, timeline):
        tod_bonus = abs(4 - timeline.hour)
        season_bonus = abs(200 - timeline.day)
        for square in self.squares:
            square.supply['a'] = int(square.supply['a'] / 2)
            if square.location[0] > 90: square.supply['a'] += (100 * tod_bonus) + season_bonus
            elif square.location[0] >70: square.supply['a'] += (200 * tod_bonus) + season_bonus
            elif square.location[0] > 40: square.supply['a'] += (300 * tod_bonus) + season_bonus
            elif square.location[0] > 20: square.supply['a'] += (500 * tod_bonus) + season_bonus

    def make_squares_supply_map(self, supply_type):
        map_array = [[0 for col in range(100)] for row in range(100)]
        for i in range(len(self.squares)):
            x_axis = self.squares[i].location[0]
            y_axis = self.squares[i].location[1]
            map_array[x_axis][y_axis] += self.squares[i].supply[supply_type]
        return map_array




class Single_square:
    def __init__(self):
        self.population = []
        self.location = [0,0]
        self.supply = {'a': 100, 'b': 1000, 'c': 5000}



class Character1:
    def __init__(self):
        self.id = 1
        self.age = 0
        self.dna = {'reckon_cost':{'a':2, 'b': 2, 'c':2}, 'scoop size': 10, 'actions per reckon': 1, 'total storage': 1000, 'rep rate': [100,99]}
        self.memes = {'replicate':1, 'scoop':1, 'convert':1, 'move':1,'move_type':{'up':1, 'down':1, 'left':1, 'right':1}}
        self.reckoning_rate = 1
        self.reckoning_cost = self.dna['reckon_cost']
        self.scoop_size = self.dna['scoop size']
        self.actions_per_reckon = self.dna['actions per reckon']
        self.scoop_type = 'Random'
        self.supply = {'a': 100, 'b': 100, 'c': 100}
        self.total_storage = self.dna['total storage']
        self.location = [0,0]
        self.direction = 0
        self.speed = {'Swim':3, 'Fast swim': 5, 'Walk': 2, 'Run': 4}

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

    def select_action(s, habitat):
        selection_range = s.memes['replicate'] + s.memes['scoop'] + s.memes['convert'] + s.memes['move']
        selection_number = random.randint(1,selection_range)
        if selection_number <= s.memes['replicate']:
            s.replicate(habitat)
        elif selection_number <= s.memes['replicate'] + s.memes['scoop']:
            s.scoop(habitat)
        elif selection_number <= s.memes['replicate'] + s.memes['scoop'] + s.memes['convert']:
            s.convert()
        elif selection_number <= s.memes['replicate'] + s.memes['scoop'] + s.memes['convert'] + s.memes['move']:


    def replicate(self, habitat):
        halved_supply = {k: int(v / 2) for k, v in self.supply.items()}
        new_char1 = Character1()
        self.supply = halved_supply
        new_char1.supply = halved_supply

   # def move(self):



    def scoop(self, habitat):
        multi_scoop(habitat, self, self.scoop_size)

    def convert(self):
        n=0
        while self.supply['a'] > 40 and n < 20:
            self.supply['a'] -= 1
            self.supply['b'] += 1
            n+=1
