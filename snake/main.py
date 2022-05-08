import pygame
import os
import sys
import random
import logging

from constants import *
from snake import Snake

#Logging part
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

pygame.init()
pygame.display.set_caption('My First Snake Game')
pygame.font.init()

screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH), pygame.HWSURFACE)

score_font      = pygame.font.Font(None, 38)
score_num_font  = pygame.font.Font(None, 28)
game_over_font  = pygame.font.Font(None, 48)
play_again_font = score_num_font
score_msg_font  = score_font.render('Score: ', True, GREEN)
score_msg_size  = score_font.size('Score')
backround_color = BLACK

gameClock = pygame.time.Clock()


def check_collision(pos_a: int, size_a: int, pos_b: int, size_b: int) -> bool:
    if pos_a.x < pos_b.x * size_b and pos_a.x * size_a > pos_b.x \
        and pos_a.y < pos_b.y * size_b and pos_a.y * size_a > pos_b.y :
        return True
    return False

def check_limits(snake):
    if snake.x > SCREEN_WIDTH:
        snake.x = SNAKE_SIZE
    if snake.x < 0:
        snake.x = SCREEN_WIDTH - SNAKE_SIZE
    if snake.y > SCREEN_HEIGHT:
        snake.y = SNAKE_SIZE
    if snake.y < 0:
        snake.y = SCREEN_HEIGHT - SNAKE_SIZE
    


def getKeys() -> DirectionType | SystemButtonType:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                return DirectionType.UP
            if event.key == pygame.K_DOWN:
                return DirectionType.DOWN
            if event.key == pygame.K_LEFT:
                return DirectionType.LEFT
            if event.key == pygame.K_RIGHT:
                return DirectionType.RIGHT
            if event.key == pygame.K_ESCAPE:
                return SystemButtonType.EXIT
            if event.key == pygame.K_y:
                return SystemButtonType.YES
            if event.key == pygame.K_n:
                return SystemButtonType.NO
        if event.type == pygame.QUIT:
            sys.exit(0)

def end_game() -> None:
    msg = game_over_font.render("Game Over", True, WHITE)
    msg_play_again = play_again_font.render("Play Again? (Y/N)", True, GREEN)

    screen.blit(msg,(SCREEN_HEIGHT_CENTER + MSG_PADDING, SCREEN_WIDTH_CENTER / 2 + MSG_PADDING * 2))
    screen.blit(msg_play_again,(SCREEN_HEIGHT_CENTER + MSG_PADDING * 2, SCREEN_WIDTH_CENTER / 2 + MSG_PADDING * 4))

    pygame.display.flip()
    pygame.display.update()

    mKey = getKeys()
    while(mKey != SystemButtonType.EXIT):
        if mKey == SystemButtonType.YES: 
            main()
        elif mKey == SystemButtonType.NO:
            break
        mKey = getKeys()
        gameClock.tick(FPS)
    sys.exit(0)

def draw_score(score: int) -> None:
    score_num = score_num_font.render(str(score), True, RED)
    screen.blit(score_msg_font, (SCREEN_WIDTH - score_msg_size[0]  - MSG_PADDING * 3, 10))
    screen.blit(score_num, (SCREEN_WIDTH - 45, 14))

def draw_game_time(game_time: int) -> None:
    game_time_msg = score_font.render(f"Time: {game_time / 1000}", True, WHITE)
    screen.blit(game_time_msg, (30,10)) 

def exit_screen() -> None:
    pass

def main():
    is_game_on = True
    my_snake = Snake(SCREEN_WIDTH_CENTER,SCREEN_WIDTH_CENTER)
    while is_game_on:
        key_pressed = getKeys()        
        if key_pressed == SystemButtonType.EXIT:
            pygame.QUIT()

        my_snake.move(key_pressed)
        my_snake.draw(screen)

        gameClock.tick(FPS)
        
        pygame.display.flip()
        pygame.display.update()
        screen.fill(BLACK)



if __name__ == '__main__':
    main()
