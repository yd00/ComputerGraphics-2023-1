import numpy as np
import pygame

pygame.display.set_caption('Homework 2 - Coordinate-free System')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()
prev_loc = None

done = False
while not done:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(f'clicked at: ({x}, {y})')
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 3)
            if prev_loc is not None:
                for i in range(1000):
                    i *= 0.001
                    point_x, point_y = int(((1 - i) * prev_loc[0]) + (i * x)), int(((1 - i) * prev_loc[1]) + (i * y))
                    screen.set_at((point_x, point_y), (255, 0, 0))
            prev_loc = (x, y)

    pygame.display.update()
pygame.quit()
