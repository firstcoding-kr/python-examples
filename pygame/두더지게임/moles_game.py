import pygame
import random
import time

pygame.init() #파이 게임 초기화
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
LIMIT_SEC = 30
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #화면 크기 설정
clock = pygame.time.Clock() 

BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
large_font = pygame.font.SysFont('malgungothic', 72)
small_font = pygame.font.SysFont('malgungothic', 36)

score = 0 # 점수
start_time = int(time.time()) #1970년 1월 1일 0시 0분 0초 부터 현재까지 초 
remain_second = LIMIT_SEC # 남은시간
game_over = False # 게임오버 여부

mole_image = pygame.image.load('mole.png') # 두더지 이미지 로드
moles = []
for i in range(2):
    # 랜덤 위치에 두더지를 생성한다.
    mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
    moles.append(mole)
    print(moles)

# 사운드 처리
pygame.mixer.init()
pygame.mixer.music.load('music.mid') #배경 음악 (https://bitmidi.com/)
pygame.mixer.music.play(-1) # -1: 무한 반복, 0: 한번
whack_sound = pygame.mixer.Sound('whack.mp3') #사운드
game_over_sound = pygame.mixer.Sound('game_over.mp3')

while True: #게임 루프
    screen.fill(BLACK) #단색으로 채워 화면 지우기

    event = pygame.event.poll() #이벤트 처리
    if event.type == pygame.QUIT:
        break
    elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
        # 클릭 이벤트 처리
        print(event.pos[0], event.pos[1])
        for mole in moles:
            if mole.collidepoint(event.pos):
                print(mole)
                moles.remove(mole)
                mole = mole_image.get_rect(left=random.randint(0, SCREEN_WIDTH - mole_image.get_width()), top=random.randint(0, SCREEN_HEIGHT - mole_image.get_height()))
                moles.append(mole)
                score += 1
                whack_sound.play()

    if not game_over: 
        # 남은시간 계산
        current_time = int(time.time())
        remain_second = LIMIT_SEC - (current_time - start_time)

        if remain_second <= 0:
            game_over = True
            pygame.mixer.music.stop()
            game_over_sound.play()

    #화면 그리기
    for mole in moles:
        screen.blit(mole_image, mole)

    # 점수 표시
    score_image = small_font.render('점수 {}'.format(score), True, YELLOW)
    screen.blit(score_image, (10, 10))

    # 남은 시간 표시
    remain_second_image = small_font.render('남은 시간 {}'.format(remain_second), True, YELLOW)
    screen.blit(remain_second_image, remain_second_image.get_rect(right=SCREEN_WIDTH - 10, top=10))

    # 게임 오버 시 메시지 표시
    if game_over:
        game_over_image = large_font.render('게임 종료', True, RED)
        screen.blit(game_over_image, game_over_image.get_rect(centerx=SCREEN_WIDTH // 2, centery=SCREEN_HEIGHT // 2))

    pygame.display.update() #모든 화면 그리기 업데이트
    clock.tick(30) #30 FPS (초당 프레임 수) 를 위한 딜레이 추가, 딜레이 시간이 아닌 목표로 하는 FPS 값

pygame.quit() 
