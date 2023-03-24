"""
@author: yd00
"""
import pygame
import numpy as np

pygame.display.set_caption('HW4 - Lagrange Polynomial')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()
active = True
vertices = []

while active:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 3:
                x, y = pygame.mouse.get_pos()
                print(f'clicked at: ({x}, {y})')
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 3)
                vertices.append((x, y))
                if len(vertices) == 3:
                    for t in np.arange(0.001, len(vertices)-1+0.001, 0.001):
                        point_x = int(-(t - 1) * -0.5 * (t - 2) * vertices[0][0] + t * -(t - 2) * vertices[1][0] + 0.5 * t * (t - 1) * vertices[2][0])
                        point_y = int(-(t - 1) * -0.5 * (t - 2) * vertices[0][1] + t * -(t - 2) * vertices[1][1] + 0.5 * t * (t - 1) * vertices[2][1])
                        pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)

    pygame.display.update()
pygame.quit()