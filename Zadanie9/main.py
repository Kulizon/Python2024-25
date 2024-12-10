import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Atari Pong")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 20
PADDLE_SPEED = 5
BALL_SPEED_X = 9
BALL_SPEED_Y = 9
WINNING_SCORE = 11

left_paddle = pygame.Rect(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)

ball_dx, ball_dy = BALL_SPEED_X, BALL_SPEED_Y
left_score, right_score = 0, 0
font = pygame.font.Font(None, 36)

def draw_game():
    WIN.fill(BLACK)
    pygame.draw.rect(WIN, WHITE, left_paddle)
    pygame.draw.rect(WIN, WHITE, right_paddle)
    pygame.draw.ellipse(WIN, WHITE, ball)
    pygame.draw.aaline(WIN, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)
    WIN.blit(left_text, (WIDTH // 4 - left_text.get_width() // 2, 20))
    WIN.blit(right_text, (3 * WIDTH // 4 - right_text.get_width() // 2, 20))
    pygame.display.flip()

def move_ball():
    global ball_dx, ball_dy, left_score, right_score
    ball.x += ball_dx
    ball.y += ball_dy
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy *= -1
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx *= -1
    if ball.left <= 0:
        right_score += 1
        reset_ball()
    elif ball.right >= WIDTH:
        left_score += 1
        reset_ball()

def reset_ball():
    global ball_dx, ball_dy
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx *= random.choice((-1, 1))
    ball_dy *= random.choice((-1, 1))

def move_paddles(keys, single_player):
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= PADDLE_SPEED
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += PADDLE_SPEED
    if not single_player:
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED
    else:
        if ball.y < right_paddle.y and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED
        elif ball.y > right_paddle.y and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

def main():
    clock = pygame.time.Clock()
    run = True
    single_player = True
    global left_score, right_score
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        move_paddles(keys, single_player)
        move_ball()
        if left_score == WINNING_SCORE or right_score == WINNING_SCORE:
            display_winner("Left" if left_score == WINNING_SCORE else "Right")
            break
        draw_game()
    pygame.quit()

def display_winner(winner):
    WIN.fill(BLACK)
    text = font.render(f"{winner} Player Wins!", True, WHITE)
    WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(2000)

if __name__ == "__main__":
    main()
