import pygame
pygame.init()
done = False
screen = pygame.display.set_mode((500,500))
screen.fill("green")
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.draw.circle(screen,"blue",(90,90),50)
    pygame.draw.circle(screen,"black",(30,30),50,2)
    pygame.display.flip()
    