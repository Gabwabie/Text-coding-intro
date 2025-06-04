import pygame

pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Pygame Window")

screen.fill("blue")
pygame.display.update()

img = pygame.image.load("pygame/tree.png")
img = pygame.transform.scale(img,(100,100))

bgimg = pygame.image.load("pygame/sky.jpg")
bgimg = pygame.transform.scale(bgimg,(500,500))

font = pygame.font.SysFont("Times New Roman",72)
text = font.render("Happy Tree",True,(255,255,0))

while True:
    screen.blit(bgimg,(0,0))
    screen.blit(img,(50,50))
    screen.blit(text,(200,10))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
    pygame.display.update()