"""
@author: yd00
"""
import pygame
import numpy as np

pygame.display.set_caption('HW4 - Linear Spline')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()
prev_loc = None

active = True
while active:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'clicked at: ({x}, {y})')
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 3)
            if prev_loc is not None:
                for t in np.arange(0, 1.001, 0.001):
                    point_x = int((1 - t) * prev_loc[0] + t * x)
                    point_y = int((1 - t) * prev_loc[1] + t * y)
                    pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)
            prev_loc = (x, y)

    pygame.display.update()
pygame.quit()