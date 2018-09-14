import pygame
from dot import Dot
from game_consts import *

def start():
    pygame.init()
    check_me = Dot(300,300)

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(BACKGROUND_SIZE)
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, DOT_COLOR, [check_me.position.x, check_me.position.y, DOT_HEIGHT, DOT_WIDTH])
    pygame.display.update()

    stop = False
    while not stop:
        check_me.move()
        check_me.update()

        if check_me.is_dead:
            stop = True

       # for event in pygame.event.get():
       #     if event.type == pygame.QUIT:
       #         stop = True
       #     print(event)

        screen.fill(BACKGROUND_COLOR)
        check_me.show(screen)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    start()