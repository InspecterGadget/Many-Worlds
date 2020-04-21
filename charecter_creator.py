class Plant1:
    def __init__(self):
        self.id_num = 1
        self.kingdom = 'Plant'
        self.age = 0
        self.size = 1000
        self.energy = 10000
        self.soil =0
        self.nitrogen = 0
        self.water = 0
        self.co2 = 0
        self.oxygen =0
        self.sun_energy = 0
        self.storage = self.size

    def replicate(self, habitat):
        new_plant = Plant1()
        energy = self.energy - 100

        size = self.size / 2
        self.size = size
        new_plant.size = size
        self.energy = energy
        new_plant.energy = energy
        habitat.population.append(new_plant)

    def receive_resource_pack(self, habitat):
        pack = habitat.create_random_resource_pack()
        self.soil += pack['soil']
        self.nitrogen += pack['nitrogen']
        self.water += pack['water']
        self.co2 += pack['co2']
        self.sun_energy += pack['sun_energy']
        self.energy -= 10

    def grow(self, habitat):
        self.sun_energy -=300
        self.soil -= 200
        self.nitrogen -= 47
        self.water -=100
        self.co2 -= 100
        habitat.oxygen +=54
        self.energy+= (200 - self.age/1000)
        self.size += (self.energy/500)


'''
population = 0
sun_energy = 999999999999
core_energy = 111111111111
soil = 7849995
water = 9999955
co2 = 7666495
oxygen = 4757788
nitrogen = 588900
'''
