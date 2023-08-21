
import pygame
pygame.init()




screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 게임 로직 및 그래픽 업데이트
    
    pygame.display.flip()

pygame.quit()
