import pygame
import random

# Making canvas
screen = pygame.display.set_mode((900, 700))
screen.fill((255, 255, 255))

# Setting Title
pygame.display.set_caption('Perfect Circle by Aidar')

draw_on = False
last_pos = (0, 0)

# Radius of the Brush
radius = 5

def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)

ini_pos = (-1,-1)
ok = 0
try :
    while True :
        color = (0, 0, 0)
        pygame.draw.circle(screen, color, (450, 350), 10)
        e = pygame.event.wait()
        if e.type == pygame.QUIT :
            raise StopIteration
        if e.type == pygame.MOUSEBUTTONDOWN :
            if ini_pos[0] == -1 and ini_pos[1] == -1:
                ini_pos = pygame.mouse.get_pos()
            spot = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0, 255, 0), e.pos, radius)
            draw_on = True
        # When mouse button released it will stop drawing
        if e.type == pygame.MOUSEBUTTONUP :
            draw_on = False
        # It will draw a continuous circle with the help of roundline function.
        if e.type == pygame.MOUSEMOTION:
            spot = pygame.mouse.get_pos()
            if draw_on:
                pygame.draw.circle(screen, (0, 255, 0), e.pos, radius)
                roundline(screen, (0, 255, 0), e.pos, last_pos, radius)
            last_pos = e.pos
            ans = random.randint(60, 89)
            if abs(spot[0]-ini_pos[0]) <= 10 and abs(spot[1]-ini_pos[1]) <= 10 and ok == 0:
                ok = 1
                print(str(ans)+' %')
        pygame.display.flip()
except StopIteration:
    pass
pygame.quit()
