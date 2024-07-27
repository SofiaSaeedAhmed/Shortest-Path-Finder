from turtle import width
import pygame
# from pygame.locals import *
# from pygame import mixer

# pygame.mixer.init()
# pygame.init()
# pygame.mixer.music.load('ambient-cinematic-hip-hop-22168.mp3')
# pygame.mixer.music.play(loops=-1)


width = 700
WIN = pygame.display.set_mode((width, width))                               # setting display by dimension
pygame.display.set_caption("Path Finding Algorithm Visualization")       # setting caption

# bg_colour = (180,205,205)

# WIN.fill(bg_colour)
bg_img = pygame.image.load('pathfinding3.png')
bg_img = pygame.transform.scale(bg_img,(width, width))
WIN.blit(bg_img,(0,0))
pygame.font.init()
font = pygame.font.SysFont('CooperBlack',30)
line1 = font.render("Welcome to the pathfinding visualizer!", True, (220,20,60), (180,205,205))
WIN.blit(line1, (75, 300))
line1 = font.render("", True, (255, 255, 255), (0,0,0))
WIN.blit(line1, (75, 300))
font1 = pygame.font.SysFont('ComicSansMs',20)
line2 = font1.render("To see A* visualiztion, press 1. To see Dijkstra visualization press 2!", True, (220,20,60), (180,205,205))
WIN.blit(line2, (75, 380))
line3 = font1.render("(Click on the screen to proceed to the grid)", True, (220,20,60), (180,205,205))
WIN.blit(line3, (75, 430))
pygame.display.update()

dark_grey = (56,56,56)
blue = (0, 255, 0)
orange = (255, 165 ,0)
grey = (128, 128, 128)
turquoise = (64, 224, 208)
yellow = (255, 255, 0)
white = (255, 255, 255)
offwhite = (238,213,183)
black = (0, 0, 0)
purple = (128, 0, 128)
light_violet = (171,130,255)
navy_blue = (0,104,139)
red = (139,26,26)
light_green = (202,255,112)


