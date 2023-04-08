"""
@author: yd00
"""
import pygame
import numpy as np

knots = []   # n+d+1 knots


def basis(knot, degree, t):
    if degree == 0:
        return 1 if knots[knot] <= t < knots[knot + 1] else 0
    return (basis(knot, degree-1, t)*((t - knots[knot]) / (knots[knot+degree] - knots[knot]))) + \
        (basis(knot+1, degree-1, t)*((knots[knot+degree+1] - t) / (knots[knot+degree+1] - knots[knot+1])))


pygame.display.set_caption('HW7 - Cubic B-Spline')
screen = pygame.display.set_mode((800, 600))
screen.fill((255, 255, 255))

vertices = []
clock = pygame.time.Clock()
active = True

while active:
    time_passed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(vertices) < 4:
                x, y = pygame.mouse.get_pos()
                print(f'clicked at ({x}, {y})')
                pygame.draw.circle(screen, (0, 0, 255), (x, y), 3)

                if len(vertices) > 0:
                    pygame.draw.line(screen, (0, 0, 0), (vertices[-1][0], vertices[-1][1]), (x, y))
                vertices.append((x, y))

            if len(vertices) == 4:
                pygame.display.update()
                knots = np.linspace(vertices[0][0], vertices[3][0], num=8)

                for t in np.arange(vertices[0][0], vertices[3][0], 0.05):
                    point_x, point_y, denom = 0, 0, 0
                    for i in range(0, len(vertices)):
                        basis_value = basis(i, 3, t)
                        point_x += vertices[i][0] * basis_value
                        point_y += vertices[i][1] * basis_value
                        denom += basis_value
                    point_x /= denom
                    point_y /= denom
                    pygame.draw.circle(screen, (255, 0, 0), (point_x, point_y), 1)
                    pygame.display.update()
    pygame.display.update()
pygame.quit()