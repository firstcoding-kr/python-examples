import pygame
import random

# 화면 크기
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# 색깔 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 뱀의 크기
BLOCK_SIZE = 20

# 게임 속도
CLOCK_TICK = 10

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')

def game_over():
    pygame.quit()
    quit()

def game_loop():
    # 초기 위치 설정
    x = SCREEN_WIDTH // 2
    y = SCREEN_HEIGHT // 2

    # 이동 방향 설정
    dx = BLOCK_SIZE
    dy = 0

    # 먹이 위치 설정
    food_x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 10) * BLOCK_SIZE
    food_y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 10) * BLOCK_SIZE

    # 뱀의 초기 위치 설정
    snake = [(x, y)]

    # 게임 루프
    while True:
        # 이벤트 처리
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over()

        # 방향 변경
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            dx = -BLOCK_SIZE
            dy = 0
        elif keys[pygame.K_RIGHT]:
            dx = BLOCK_SIZE
            dy = 0
        elif keys[pygame.K_UP]:
            dx = 0
            dy = -BLOCK_SIZE
        elif keys[pygame.K_DOWN]:
            dx = 0
            dy = BLOCK_SIZE

        # 이동
        x += dx
        y += dy

        # 벽 충돌 검사
        if x < 0 or x >= SCREEN_WIDTH or y < 0 or y >= SCREEN_HEIGHT:
            game_over()

        # 먹이 먹음 검사
        if x == food_x and y == food_y:
            snake.append((x, y))
            food_x = random.randint(0, SCREEN_WIDTH // BLOCK_SIZE - 1) * BLOCK_SIZE
            food_y = random.randint(0, SCREEN_HEIGHT // BLOCK_SIZE - 1) * BLOCK_SIZE

        # 뱀 이동
        snake.insert(0, (x, y))
        snake.pop()

        # 그리기
        screen.fill(BLACK)
        for block in snake:
            pygame.draw.rect(screen, WHITE, (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

        pygame.draw.rect(screen, RED, (food_x, food_y, BLOCK_SIZE, BLOCK_SIZE))

        pygame.display.update()

        # 게임 속도 조절
        pygame.time.Clock().tick(CLOCK_TICK)

game_loop()
