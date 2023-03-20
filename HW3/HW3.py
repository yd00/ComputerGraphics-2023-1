import pygame
import numpy as np

pygame.display.set_caption('HW3 - Barycentric Coordinates')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()
prev_loc = None
vertices = []

active = True
while active:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 3:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 3)
                if prev_loc is not None:
                    pygame.draw.line(screen, (0, 0, 0), prev_loc, (x, y))
                prev_loc = (x, y)
                vertices.append((x, y))
                print(f'clicked at: ({x}, {y})')
                if len(vertices) == 3:
                    pygame.draw.line(screen, (0, 0, 0), (vertices[0][0], vertices[0][1]), (x, y))

                    for u in np.arange(0, 1.001, 0.001):
                        for v in np.arange(0, 1.001, 0.001):
                            if u + v > 1.0:
                                break
                            point_x = int(u * vertices[0][0] + v * vertices[1][0] + (1 - u - v) * vertices[2][0])
                            point_y = int(u * vertices[0][1] + v * vertices[1][1] + (1 - u - v) * vertices[2][1])
                            pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)
    pygame.display.update()

pygame.quit()
