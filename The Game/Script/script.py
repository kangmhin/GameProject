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

game_state = "start"  # 현재 게임 상태

start_button = pygame.image.load("The Game/image/Other/startButton.png")
start_button_rect = start_button.get_rect()
start_button_rect.center = (100, screen_height // 2)



exitdoor = pygame.image.load("The Game/image/hollway/hollway_exit.png")
exitdoor_rect = exitdoor.get_rect()
exitdoor_rect.center = (screen_width // 2, screen_height // 2)
labdoor = pygame.image.load("The Game/image/hollway/hollway_lab_door.png")
labdoor_rect = labdoor.get_rect()
labdoor_rect.center = (screen_width // 5.0, screen_height // 2)
retiringdoor = pygame.image.load("The Game/image\hollway/hollway_retiringroom_door.png")
retiringdoor_rect = retiringdoor.get_rect()
retiringdoor_rect.center = (screen_width // 2.6, screen_height // 2)
storagedoor = pygame.image.load("The Game/image/hollway/hollway_storage_door.png")
storagedoor_rect = storagedoor.get_rect()
storagedoor_rect.center = (screen_width // 1.6, screen_height // 2)
seciritydoor = pygame.image.load("The Game/image/hollway/hollway_securityroom_door.png")
seciritydoor_rect = seciritydoor.get_rect()
seciritydoor_rect.center = (screen_width // 1.3 , screen_height // 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 마우스 클릭 이벤트 처리
            if game_state == "start":
                # 시작 버튼을 클릭하면 게임 상태를 "hollway"로 변경
                if start_button_rect.collidepoint(event.pos):
                    game_state = "hollway"
            elif game_state == "hollway" :
                if exitdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    print('exitdoor') 
                elif labdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    game_state = "lab"
                elif retiringdoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    print('retiringdoor')
                elif storagedoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    print('storagedoor')
                elif seciritydoor_rect.collidepoint(event.pos):  # 이미지 위에서 클릭되었는지 확인
                    print('seciritydoor')
    
    screen.fill(white)  # 화면을 흰색으로 지우기

    if game_state == "start":
        screen.blit(start_button, start_button_rect)

    if game_state == "hollway":
        screen.blit(exitdoor, exitdoor_rect)
        screen.blit(labdoor, labdoor_rect)
        screen.blit(retiringdoor, retiringdoor_rect)
        screen.blit(storagedoor, storagedoor_rect)
        screen.blit(seciritydoor, seciritydoor_rect)
    elif game_state == "lab":
        pass
    pygame.display.flip()  # 화면 업데이트

pygame.quit()