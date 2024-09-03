import pygame
pygame.init()
done = False
screen = pygame.display.set_mode((500,500))
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.rect(screen,"yellow", pygame.Rect(30,30,45,45))
    pygame.display.flip()