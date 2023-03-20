import pygame
import numpy as np

pygame.display.set_caption('HW3 - Barycentric Coordinates 1')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

pygame.font.init()
font = pygame.font.Font(pygame.font.get_default_font(), 10)

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
            elif len(vertices) == 3:
                x, y = pygame.mouse.get_pos()
                pygame.draw.circle(screen, (0, 255, 255), (x, y), 3)
                # u = [(y2-y3)(x-x3) + (x3-x2)(y-y3)] / [(y2-y3)(x1-x3) + (x3-x2)(y1-y3)]
                # v = [(y3-y1)(x-x3) + (x1-x3)(y-y3)] / [(y2-y3)(x1-x3) + (x3-x2)(y1-y3)]
                u = ((vertices[1][1] - vertices[2][1]) * (x - vertices[2][0]) + (vertices[2][0] - vertices[1][0]) * (y - vertices[2][1])) / ((vertices[1][1] - vertices[2][1]) * (vertices[0][0] - vertices[2][0]) + (vertices[2][0] - vertices[1][0]) * (vertices[0][1] - vertices[2][1]))
                v = ((vertices[2][1] - vertices[0][1]) * (x - vertices[2][0]) + (vertices[0][0] - vertices[2][0]) * (y - vertices[2][1])) / ((vertices[1][1] - vertices[2][1]) * (vertices[0][0] - vertices[2][0]) + (vertices[2][0] - vertices[1][0]) * (vertices[0][1] - vertices[2][1]))
                text = font.render(f'({u:.2f}, {v:.2f}, {1-u-v:.2f})', True, (20, 20, 20))
                screen.blit(text, (x, y))
    pygame.display.update()

pygame.quit()
