import pygame

pygame.display.set_caption('Homework 1')
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
            pygame.draw.circle(screen, (0, 0, 255), (x, y), 5)
            if prev_loc is not None:
                pygame.draw.line(screen, (0, 0, 0), prev_loc, (x, y))
            prev_loc = (x, y)
            print(f'clicked at: ({x}, {y})')
    pygame.display.update()

pygame.quit()
