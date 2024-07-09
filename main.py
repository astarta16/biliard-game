import pygame
import pymunk
import pymunk.pygame_util
import math

pygame.init() #ბრძანებების გააქტიურება


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 678
BOTTOM_PANEL = 50

#ფანჯრის გამოტანა
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT + BOTTOM_PANEL))
pygame.display.set_caption("Pool")

#ეკრანის გამართვა
space = pymunk.Space()
static_body = space.static_body
draw_options = pymunk.pygame_util.DrawOptions(screen)

