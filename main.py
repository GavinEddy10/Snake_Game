import random
import pygame

# go back to pong to get how to do letters

# start the pygame engine
from Game import *

pygame.init()

# start the pygame font engine
pygame.font.init()
WHITE = (255, 255, 255)
myfontTitle = pygame.font.SysFont('gabriola', 80)  # load a font for use

# Initalize Text for Title


# start the sound engine
pygame.mixer.init()

# game variables
simOver = False
game = Game()

# game independent variables (needed for every pygame)
FPS = 60  # 60 Frames Per Second for the game update cycle
fpsClock = pygame.time.Clock()  # used to lock the game to 60 FPS
screen = pygame.display.set_mode((850, 750))  # initialize the game window


def clear_screen():
    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 850, 750))


def draw_borders():
    for i in range(17):
        if i != 0:
            pygame.draw.line(screen, WHITE, (50*i, 0), (50*i, 750), 1)
    for i in range(15):
        if i != 0:
            pygame.draw.line(screen, WHITE, (0, 50*i), (850, 50*i), 1)


# main while loop
while not simOver:
    # loop through and empty the event queue, key presses
    # buttons, clicks, etc.
    for event in pygame.event.get():
        # if the event is a click on the "X" close button
        if event.type == pygame.QUIT:
            simOver = True

    # draw code
    clear_screen()
    draw_borders()


    # player update code

    # put all the graphics on the screen
    # should be the LAST LINE of game code
    pygame.display.flip()
    fpsClock.tick(FPS)  # slow the loop down to 60 loops per second
