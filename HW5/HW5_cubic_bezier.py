"""
@author: yd00
"""

import pygame
import numpy as np

pygame.display.set_caption('HW5 - Cubic Bezier Curve')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()
vertices = []

active = True
while active:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 4:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 3)
                vertices.append((x, y))
                print(f'clicked at: ({x}, {y})')

                if len(vertices) == 4:
                    # connect vertices with straight lines
                    for i in range(3):
                        pygame.draw.line(screen, (0, 0, 0), vertices[i], vertices[i+1])

                    # draw Bezier curve
                    for t in np.arange(0, 1.001, 0.001):
                        point_x = vertices[0][0] * (1-t)**3 + 3 * vertices[1][0] * t * (1-t)**2 + 3 * vertices[2][0] * t**2 * (1-t) + vertices[3][0] * t**3
                        point_y = vertices[0][1] * (1-t)**3 + 3 * vertices[1][1] * t * (1-t)**2 + 3 * vertices[2][1] * t**2 * (1-t) + vertices[3][1] * t**3
                        pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)

    pygame.display.update()
pygame.quit()