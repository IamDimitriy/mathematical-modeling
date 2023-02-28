import pygame
import random

pygame.init()
"""Настройки проги"""
# global variables
BOX_WIGHT = 1024
BOX_HEIGHT = 700
FPS = 30
# color r g b
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (219, 209, 123)
RED = (204, 129, 110)
VIOLET = (148, 99, 212)
GREEN = (0, 255, 0)
GRAY = (169, 169, 169)
all_color = [VIOLET, YELLOW, RED]
# шрифт
game_font = pygame.font.SysFont("Roboto", 30)
txt_color = BLACK
font = pygame.font.SysFont('Calibri', 16)  # text for inform table
# info window
alpha = 0.5  # коэф сдвига информационного окна относительно бактерий
table_size_x, table_size_y = 100, 100
# экран и вывод
screen = pygame.display.set_mode((BOX_WIGHT, BOX_HEIGHT))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
dir = r"C:\Users\Honor\Desktop\piton\проект"
icon = pygame.image.load(
    dir + r"\спрайты\чашка-петри.jpg")
bg_image = pygame.image.load(
    dir + r"\спрайты\фон.jpg").convert()
"""Объекты"""
# группы объектов
all_sprites = pygame.sprite.Group()
violet_facs = pygame.sprite.Group()
yellow_facs = pygame.sprite.Group()
red_facs = pygame.sprite.Group()
eats = pygame.sprite.Group()
bacs = pygame.sprite.Group()
crispr_bacs = pygame.sprite.Group()
non_crispr = pygame.sprite.Group()
norm_bacs = pygame.sprite.Group()
inf_bacs = pygame.sprite.Group()
x = random.randrange(0, BOX_WIGHT)
y = random.randrange(0, BOX_HEIGHT)
# кол-во и соотношения объектов
satiety = 40  # сытность пищи
color_eat = GREEN
quantity_bac = 40
quantity_fac = quantity_bac*2
quantity_eat = quantity_bac*(200//satiety)
"""Настройки животных"""
# Настройки бактерий
img_normal = dir + r"\спрайты\sprites\bacs\normal_bac.png"
crispr_def = []
quantity = 0  # кол-во фагов

# получение подробной статистики
data = []
