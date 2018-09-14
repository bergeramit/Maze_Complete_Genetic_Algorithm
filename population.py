from dot import Dot, get_fitness
import random
from game_consts import *


class Population:
    def __init__(self):
        self.dots = []
        self.old_dots = []
        for i in range(SIZE_OF_POPULATION):
            self.dots.append(Dot(DOT_START_X_POSITION, DOT_START_Y_POSITION))


    def show(self, screen):
        for i in range(1, len(self.dots)):
            self.dots[i].show(screen)
        self.dots[0].show(screen, BEST_DOT_COLOR)


    def move_and_update(self):
        for i in range(len(self.dots)):
            self.dots[i].move()
            self.dots[i].update()


    def is_extinct(self):
        for i in range(len(self.dots)):
            if not self.dots[i].is_dead:
                return False
        return True


    def clone_elite(self):
        self.dots = self.old_dots[:ELITE_NUMBER]


    def clone_end_dot(self, source_dot):
        for i in range(MAX_STEPS):
            self.dots[-1].brain.directions[i] = source_dot.brain.directions[i]


    def calculate_fitness(self):
        for i in range(len(self.dots)):
            self.dots[i].calculate_fitness()
        self.dots.sort(key=get_fitness, reverse=True)


    def mate(self):
        sum_of_fitness = 0
        for i in range(MATE_POPULATION):
            sum_of_fitness += self.old_dots[i].fitness

        for _ in range(SIZE_OF_POPULATION - ELITE_NUMBER):
            place = random.randint(0, int(sum_of_fitness))
            index = 0
            for i in range(MATE_POPULATION):
                if place <= self.old_dots[i].fitness:
                    index = i
                    break
                place -= self.old_dots[i].fitness

            #print("sum: {} place: {} index: {}".format(str(sum_of_fitness), str(place), str(index)))

            self.dots.append(Dot(DOT_START_X_POSITION, DOT_START_Y_POSITION))
            self.clone_end_dot(self.old_dots[index])
            #self.dots[-1] = self.old_dots[index]
            #clone_dot(self.dots[-1], self.old_dots[index])
            #self.dots.append(self.old_dots[index])


    def mutate(self):
        for i in range(ELITE_NUMBER, len(self.dots)):
            self.dots[i].mutate()


    def revive(self):
        for i in range(len(self.dots)):
            self.dots[i].revive()


    def generate_new_population(self):
        # Calculate the fitness
        self.calculate_fitness()
        # only mate with the top 50%
        self.old_dots = self.dots[:MATE_POPULATION]
        # The new population
        self.dots = []
        # Clone the best dots
        self.clone_elite()
        # Generate the rest
        self.mate()
        # Mutate stage
        self.mutate()
        # revive all
        self.revive()

