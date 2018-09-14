from vectors_util import *


class Brain:
    def __init__(self, max_steps):
        self.max_steps = max_steps
        self.directions = []
        self.initial_vectors()

    def initial_vectors(self):
        for i in range(self.max_steps):
            acceleration = get_random_direction_vector()
            self.directions.append(acceleration)

