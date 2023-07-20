import pygame
import sys

#화면 크기
screen_height = 750
screen_width = 1280

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Game')

startImg = pygame.image.load("image/others/")

#게임 실행
run = True
while run :

    #event 값
    for event in pygame.event.get() :
        #게임 종료
        if event.type == pygame.QUIT :
            run = False
    
    pygame.display.update()

pygame.quit()