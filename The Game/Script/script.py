import pygame
import time
import sys

black = (0,0,0)
white = (255,255,255)

#화면 크기
screen_height = 750
screen_width = 1280

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('The Game')

startImg = pygame.image.load("The Game/Image/others/starticon.png")
quitImg = pygame.image.load("The Game/Image/others/quiticon.png")
clickStartImg = pygame.image.load("The Game/Image/others/clickedStarticon.png")
clickQuitImg = pygame.image.load("The Game/Image/others/clickedQuiticon.png")

fps = pygame.time.Clock()

class Button :
    def __init__(self, img_in, x, y, width, height, img_act, x_act, y_act, action = None) :
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + width > mouse[0] > x and y + height > mouse[1] > y :
            screen.blit(img_act, (x_act, y_act))
        if click[0] and action != None :
            time.sleep(1)
            action()
        else :
            screen.blit(img_in, (x, y))

def quitgame():
    pygame.quit()
    sys.exit()

#게임 실행
def mainmenu() :
    
    run = True
    
    while run :
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                pygame.quit()
                sys.exit()
        screen.fill(white)

        startButton = Button(startImg,207,302,60,20,clickStartImg,200,300,None)
        quitButton = Button(quitImg,205,422,60,20,clickQuitImg,200, 420,quitgame)
        pygame.display.update()
        fps.tick(15)

mainmenu()