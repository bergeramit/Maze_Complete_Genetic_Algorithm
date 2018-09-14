from vectors_util import *
from brain import Brain
import pygame
import math
from game_consts import *

class Dot:

    def __init__(self, x, y):
        self.position = Vector(x, y)
        self.velocity = Vector()
        self.brain = Brain(1000)
        self.step = 0
        self.is_dead = False


    def move(self, time_elapsed=1):
        if not self.is_dead:
            update_position(self.position, self.velocity, self.brain.directions[self.step], time_elapsed)
            print(self.velocity.x, self.velocity.y)
            if math.fabs(self.velocity.x) <= 5 and math.fabs(self.velocity.y) <= 5:
                update_velocity(self.velocity, self.brain.directions[self.step], time_elapsed)


    def update(self):
        self.step += 1
        if self.step == self.brain.max_steps or self.is_crossed(Vector(0,0), BACKGROUND_SIZE):
            self.is_dead = True


    def show(self, screen):
        pygame.draw.rect(screen, DOT_COLOR, [self.position.x, self.position.y, DOT_HEIGHT, DOT_WIDTH])

    def is_crossed(self, position, size):
        return True if self.position.x <= position.x or self.position.x >= position.x + size[0] or \
                        self.position.y <= position.y or self.position.y >= position.y + size[1] else False
