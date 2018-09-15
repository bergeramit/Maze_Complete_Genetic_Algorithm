import pygame
from population import Population
from game_consts import *


def draw_terrain(screen):
    for name, terrain in TERRAIN.items():
        pygame.draw.rect(screen, terrain.color, [terrain.position.x, terrain.position.y, terrain.height, terrain.width])


def start():
    population = Population()

    generation_count = 1
    stop = False
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(BACKGROUND_SIZE)

    while not stop:

        screen.fill(BACKGROUND_COLOR)
        draw_terrain(screen)
        population.show(screen)
        pygame.display.update()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = True

        population.move_and_update()
        if population.is_extinct():
            print("Generation: {}".format(generation_count))
            generation_count += 1
            population.generate_new_population()


    pygame.quit()

if __name__ == "__main__":
    start()