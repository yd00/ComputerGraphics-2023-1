"""
@author: yd00
"""
import pygame
import numpy as np

pygame.display.set_caption('HW6 - Cubic Hermite Interpolation')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

vertices = []
time_passed = pygame.time.Clock()
active = True

while active:
    time_passed.tick(30)

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
                a = np.array([
                    [vertices[0][0]**3, vertices[0][0]**2, vertices[0][0], 1, 0, 0, 0, 0],
                    [vertices[1][0]**3, vertices[1][0]**2, vertices[1][0], 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, vertices[1][0]**3, vertices[1][0]**2, vertices[1][0], 1],
                    [0, 0, 0, 0, vertices[2][0]**3, vertices[2][0]**2, vertices[2][0], 1],
                    [3*vertices[1][0]**2, 2*vertices[1][0], 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 3*vertices[1][0]**2, 2*vertices[1][0], 1, 0],
                    [6*vertices[1][0], 2, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 6*vertices[1][0], 2, 0, 0]
                ])
                b = np.array([vertices[0][1], vertices[1][1], vertices[1][1], vertices[2][1], 0, 0, 0, 0])
                result = np.dot(np.linalg.inv(a), b)

                for point_x in np.arange(vertices[0][0], vertices[1][0], 0.5):
                    point_y = result[0]*(point_x**3) + result[1]*(point_x**2) + result[2]*point_x + result[3]
                    pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)

                for point_x in np.arange(vertices[1][0], vertices[2][0], 0.5):
                    point_y = result[4]*(point_x**3) + result[5]*(point_x**2) + result[6]*point_x + result[7]
                    pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)
    pygame.display.update()
pygame.quit()