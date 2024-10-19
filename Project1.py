import pygame
pygame.init()
w, h = 500,500
display_surface = pygame.display.set_mode((w,h))

bg_image = pygame.transform.scale(pygame.image.load("bg.png").convert(),(w,h))
def game_loop():
    clock = pygame.time.Clock()
    running =  True
    while running:
        display_surface.blit(bg_image, (0,0))
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
   game_loop()