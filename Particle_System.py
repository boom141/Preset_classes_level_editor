import random

class Particle_Lists:
    def __init__(self):
        self.Testing = 'Testing'

    def Disperse(self,x,y,range):
        return [[x, y], [random.randrange(-3,3),random.randrange(-10,10)], random.randint(0, range)]
    
    def Test(self):
        return self.Testing

