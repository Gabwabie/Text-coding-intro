import pygame

pygame.init()
screen = pygame.display.set_mode((500,500))
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.draw.rect(screen, (0, 125, 255), pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(screen, (25, 100, 0), pygame.Rect(300, 30, 60, 60))

    pygame.draw.circle(screen, (0, 255, 0), (300, 300), 50)
    pygame.draw.circle(screen, (0, 255, 0), (100, 100), 50, 10)

    pygame.draw.line(screen, (255, 212, 0), (0, 50), (500, 50), 5)

    pygame.display.flip()