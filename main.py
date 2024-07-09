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




#ფოტოების შემოტანა
cue_image = pygame.image.load("assets/images/cue.png").convert_alpha()
table_image = pygame.image.load("assets/images/table.png").convert_alpha()
ball_images = []
for i in range(1, 17):
  ball_image = pygame.image.load(f"assets/images/ball_{i}.png").convert_alpha()
  ball_images.append(ball_image)

#ტექსტის გამოტანა
def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

#ბურთების ფუნქცია
def create_ball(radius, pos):
  body = pymunk.Body()
  body.position = pos
  shape = pymunk.Circle(body, radius)
  shape.mass = 5
  shape.elasticity = 0.8
  pivot = pymunk.PivotJoint(static_body, body, (0, 0), (0, 0))
  pivot.max_bias = 0 
  pivot.max_force = 1000
  space.add(body, shape, pivot)
  return shape

#ბურთების როუ და ქოლუმნი
balls = []
rows = 5
#potting balls
for col in range(5):
  for row in range(rows):
    pos = (250 + (col * (dia + 1)), 267 + (row * (dia + 1)) + (col * dia / 2))
    new_ball = create_ball(dia / 2, pos)
    balls.append(new_ball)
  rows -= 1
#cue ball
pos = (888, SCREEN_HEIGHT / 2)
cue_ball = create_ball(dia / 2, pos)
balls.append(cue_ball)


#ხვრელების შექმნა
pockets = [
  (55, 63),
  (592, 48),
  (1134, 64),
  (55, 616),
  (592, 629),
  (1134, 616)
]

#სათამაშო ბურთები
cushions = [
  [(88, 56), (109, 77), (555, 77), (564, 56)],
  [(621, 56), (630, 77), (1081, 77), (1102, 56)],
  [(89, 621), (110, 600),(556, 600), (564, 621)],
  [(622, 621), (630, 600), (1081, 600), (1102, 621)],
  [(56, 96), (77, 117), (77, 560), (56, 581)],
  [(1143, 96), (1122, 117), (1122, 560), (1143, 581)]
]