from vectors_util import *
import random
import math

class Brain:
    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.directions = []
        self.initial_vectors()

    def initial_vectors(self):
        for i in range(self.max_steps):
            acceleration = Vector((random.random() - 0.5) * 5, (random.random() - 0.5) * 5)
            self.directions.append(acceleration)

