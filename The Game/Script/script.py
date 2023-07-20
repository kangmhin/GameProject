import sys
import pygame

pygame.init()

# 게임 시작화면
def game_start() :
    start_screen = pygame.display.set_mode((500, 500))

    pygame.font.init()
    start_font = pygame.font.SysFont('Sans', 40, True, True)
    start_message = 'Start'
    start_message_object = start_font.render(start_message, True, (0, 0, 0))
    start_message_rect = start_message_object.get_rect()
    start_message_rect.center = (250, 250)

    while True :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
            start_screen.fill((255, 255, 255))
            start_screen.blit(start_message_object, start_message_rect)
            pygame.display.update()

game_start()

pygame.init()

fps = pygame.time.Clock()

background = pygame.display.set_mode((500, 500))
pygame.display.set_caption("SONOL")

background.fill((255, 255, 255))

play = True
while play:
    deltaTime = fps.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

pygame.quit()