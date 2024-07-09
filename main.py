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


#კადრის ჩატვირთვა წამში
clock = pygame.time.Clock()
FPS = 120

#თამაშის ძირითადი ცვლადები
lives = 3
dia = 36
pocket_dia = 66
force = 0
max_force = 10000
force_direction = 1
game_running = True
cue_ball_potted = False
taking_shot = True
powering_up = False
potted_balls = []

#ფერების კოდები
BG = (50, 50, 50)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

#ფონტები და ტექსტის ზომა
font = pygame.font.SysFont("Lato", 30)
large_font = pygame.font.SysFont("Lato", 60)
