import pygame
pygame.init()
w, h = 500,500
display_surface = pygame.display.set_mode((w,h))
pygame.display.set_caption("Adding BG image")

bg_image = pygame.transform.scale(pygame.image.load("bg.png").convert(),(w,h))
img = pygame.transform.scale(pygame.image.load("cow.png").convert_alpha(),(200,200))

cow_rect = img.get_rect(center = (w//2, (h//2) -30))

text = pygame.font.Font(None, 36). render("Hello world", True, pygame.Color("black"))
text_rect = text.get_rect(center = (w//2, h//2 +110))

def game_loop():
    clock = pygame.time.Clock()
    running =  True
    while running:
        display_surface.blit(bg_image, (0,0))
        display_surface.blit(img, cow_rect)
        display_surface.blit(text, text_rect)
        for event in pygame.event.get():
          if event.type == pygame.QUIT:
             running = False
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__ == "__main__":
   game_loop()