from vectors_util import *
import random
from brain import Brain
import pygame
from game_consts import *
import math


def get_fitness(single_dot):
    return single_dot.fitness


class Dot:
    def __init__(self, x, y, max_steps):
        self.position = Vector(x, y)
        self.velocity = Vector()
        self.brain = Brain(max_steps)
        self.step = 0
        self.fitness = 0
        self.is_dead = False


    def move(self, time_elapsed=1):
        if not self.is_dead:
            update_velocity(self.velocity, self.brain.directions[self.step], time_elapsed)
            if self.velocity.x > 3:
                self.velocity.x = 3
            if self.velocity.x < -3:
                self.velocity.x =  -3
            if self.velocity.y > 3:
                self.velocity.y= 3
            if self.velocity.y < -3:
                self.velocity.y =  -3
            update_position(self.position, self.velocity, time_elapsed)
            #print("Velocity: {} {}".format(str(self.velocity.x), str(self.velocity.y)))


    def is_arrived(self):
        return True if self.position.calculate_distance(TARGET_POINT) < 5 else False


    def hit_terrain(self):
        for name, terr in TERRAIN.items():
            if name == 'target_point' and self.is_arrived():
                return True
            elif self.is_crossed(terr.position, (terr.width, terr.height)):
                return True
        return False


    def update(self):
        self.step += 1
        if self.step == self.brain.max_steps or self.hit_terrain() or self.is_arrived():
            self.is_dead = True


    def add_steps(self, max_steps):
        for _ in range(max_steps - self.brain.max_steps):
            self.brain.directions.append(get_random_direction_vector())


    def show(self, screen, color=DOT_COLOR):
        pygame.draw.rect(screen, color, [self.position.x, self.position.y, DOT_HEIGHT, DOT_WIDTH])


    def is_inside(self):
        pass
        #return True if math.fabs(2)

    def is_crossed(self, position, size):
        MIN_DIST_TO_HIT = 5
        if math.fabs(self.position.x - position.x) < MIN_DIST_TO_HIT and (position.y <= self.position.y <= position.y + size[0]):
            return True
        if math.fabs(self.position.y - position.y) < MIN_DIST_TO_HIT and (position.x <= self.position.x <= position.x + size[1]):
            return True
        if math.fabs(self.position.y - size[0] - position.y) < MIN_DIST_TO_HIT and (position.x <= self.position.x <= position.x + size[1]):
            return True
        if math.fabs(self.position.x - size[1] - position.x) < MIN_DIST_TO_HIT and (position.y <= self.position.y <= position.y + size[0]):
            return True
        return False


    def above_terrain(self):
        return True if self.position.y <= 180 else False


    def distance_from_upper_place(self):
        left_distance = self.position.calculate_distance(LEFT_SPACE)
        right_distance = self.position.calculate_distance(RIGHT_SPACE)
        return left_distance if left_distance <= right_distance else right_distance


    def calculate_fitness(self):
        if self.is_arrived():
            self.fitness = (1 + (20 / self.step)) * 10
        elif not self.above_terrain():
            self.fitness = ((1 / self.distance_from_upper_place()) + (20 / self.step))
        else:
            #print("Distances: {}".format(self.position.calculate_distance(TARGET_POINT)))
            self.fitness = ((1 / self.position.calculate_distance(TARGET_POINT)) + (20 / self.step)) * 10



    def mutate(self):
        for i in range(self.brain.max_steps):
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

