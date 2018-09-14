from vectors_util import *
import random
from brain import Brain
import pygame
import math
from game_consts import *


def get_fitness(single_dot):
    return single_dot.fitness


class Dot:

    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector()
        self.brain = Brain(MAX_STEPS)
        self.step = 0
        self.fitness = 0
        self.is_dead = False


    def move(self, time_elapsed=1):
        if not self.is_dead:
            update_velocity(self.velocity, self.brain.directions[self.step], time_elapsed)
            update_position(self.position, self.velocity, time_elapsed)
            #print("Velocity: {} {}".format(str(self.velocity.x), str(self.velocity.y)))


    def is_arrived(self):
        return True if self.position.calculate_distance(TARGET_POINT) < 5 else False


    def update(self):
        self.step += 1
        if self.step == self.brain.max_steps or self.is_crossed(Vector(0,0), BACKGROUND_SIZE):
            self.is_dead = True
        if self.is_arrived():
            self.is_dead = True


    def show(self, screen, color=DOT_COLOR):
        pygame.draw.rect(screen, color, [self.position.x, self.position.y, DOT_HEIGHT, DOT_WIDTH])


    def is_crossed(self, position, size):
        return True if self.position.x <= position.x or self.position.x + DOT_WIDTH >= position.x + size[0] or \
                        self.position.y <= position.y or self.position.y + DOT_HEIGHT >= position.y + size[1] else False


    def calculate_fitness(self):
        if self.is_arrived():
            self.fitness = (1 + (100 / self.step)) * 10
        else:
            #print("Distances: {}".format(self.position.calculate_distance(TARGET_POINT)))
            self.fitness = ((1 / self.position.calculate_distance(TARGET_POINT)) + (100 / self.step)) * 10



    def mutate(self):
        for i in range(MAX_STEPS):
            if random.random() < MUTATE_RATE:
                self.brain.directions[i] = get_random_direction_vector()
                #print("Mutate Velocity: {} {}".format(self.brain.directions[i].x, self.brain.directions[i].y))
                #self.brain.directions[i].x = self.brain.directions[i].x if self.brain.directions[i].x < -1 else self.brain.directions[i].x * -1
                #self.brain.directions[i].y = self.brain.directions[i].y if self.brain.directions[i].y < -1 else self.brain.directions[i].y * -1


    def revive(self):
        self.position = Vector(DOT_START_X_POSITION, DOT_START_Y_POSITION)
        self.velocity = Vector()
        self.step = 0
        self.is_dead = False

