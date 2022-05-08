from turtle import color
from typing import Tuple
import logging
import pygame
from constants import *

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',filename='snake/snake.log', filemode='w')
logger = logging.getLogger(__name__)

class Segment():
    """
        Snake segmet object
    """
    def __init__(self, x: int, y: int, color: Tuple[int, int, int] = WHITE):
        self._x         = x
        self._y         = y
        self._direction = ButtonType.UP
        self._color     = color

    def __repr__(self) -> str:
        return f"""Segmrnt(x: {self._x}, y: {self._y}, direction: {self._direction})"""

    @property
    def direction(self) -> ButtonType:
        return self._direction

    @direction.setter
    def direction(self, new_dirrection: ButtonType) -> None:
        self._direction = new_dirrection

    @property
    def color(self) -> Tuple[int, int, int]:
        return self._color

    @color.setter
    def color(self, new_color: Tuple[int,int,int]) -> None:
        self._color = new_color

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, new_x: int) -> None:
        self._x = new_x

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, new_y: int) -> None:
        self._y = new_y

class Snake():
    """
        Snake player object
    """

    def __init__(self, x: int, y: int):
        self._x         = x
        self._y         = y
        self._direction = ButtonType.UP
        self._stack     = [ Segment(self._x, self._y, color=GREEN), Segment(self._x, self._y + SNAKE_SIZE),
                            Segment(self._x - SNAKE_SIZE, self._y + SNAKE_SIZE), Segment(self._x - SNAKE_SIZE * 2, self._y + SNAKE_SIZE),
                            Segment(self._x - SNAKE_SIZE * 4, self._y + SNAKE_SIZE)]
        
        # black_box = Segment(self._x, self._y + SEPARATION)
        # black_box.direction(ButtonType.UP)
        # black_box.color(BLACK)
        # self._stack.append(black_box)

    def __repr__(self) -> str:
        return f"""Snake(x: {self._x}, y: {self._y}, direction: {self._direction}, stack: {self._stack})
        """

    #TODO: rewrite this
    def move(self) -> None:
        previcious_x, previcious_y =  self._stack[0].x,  self._stack[0].y
        current_x, current_y = 0, 0
        for index, element in enumerate(self._stack):
            
            if index == 0:
                if (self._stack[0].direction == ButtonType.UP):
                    element.y = self._stack[0].y - (SNAKE_SIZE)
                if (self._stack[0].direction == ButtonType.DOWN):
                    element.y = self._stack[0].y + (SNAKE_SIZE)
                if (self._stack[0].direction == ButtonType.LEFT):
                    element.x = self._stack[0].x - (SNAKE_SIZE)
                if (self._stack[0].direction == ButtonType.RIGHT):
                    element.x = self._stack[0].x + (SNAKE_SIZE)
            else:
                current_x, current_y = element.x, element.y
                element.x = previcious_x
                element.y = previcious_y
                previcious_x, previcious_y = current_x, current_y

        logger.info(self)
        # last_element = len(self._stack) - 1
        # logger.info(self._stack[0])
        # while (last_element != 0):
        #     self._stack[last_element].direction = self._stack[last_element].direction 
        #     self._stack[last_element].x         = self._stack[last_element - 1].x
        #     self._stack[last_element].y         = self._stack[last_element - 1].y
        #     last_element                        = last_element - 1 
        # if len(self._stack) < 2:
        #     last_segment = self._stack[0]
        # else:
        #     logger.info("Popping ITEM <---")
        #     last_segment = self._stack.pop(last_element)

        # last_segment._direction = self._stack[0].direction
        # if (self._stack[0].direction == ButtonType.UP):
        #     last_segment.y = self._stack[0].y - (SPEED * FPS)
        # if (self._stack[0].direction == ButtonType.DOWN):
        #     last_segment.y = self._stack[0].y + (SPEED * FPS)
        # if (self._stack[0].direction == ButtonType.LEFT):
        #     last_segment.x = self._stack[0].x - (SPEED * FPS)
        # if (self._stack[0].direction == ButtonType.RIGHT):
        #     last_segment.x = self._stack[0].x + (SPEED * FPS)
        
        # self._stack.insert(0, last_element)

    def get_head(self) -> Segment:
        return self._stack[0]

    #TODO: rewrite this
    def grow(self) -> None:
        last_element = len(self._stack) - 1
        self._stack[last_element].direction = self._stack[last_element].direction
        if (self._stack[0].direction == ButtonType.UP):
            new_segment = Segment(self._stack[last_element].x, self._stack[last_element].y - SNAKE_SIZE)
        if (self._stack[0].direction == ButtonType.DOWN):
            new_segment = Segment(self._stack[last_element].x, self._stack[last_element].y + SNAKE_SIZE)
        if (self._stack[0].direction == ButtonType.LEFT):
            new_segment = Segment(self._stack[last_element].x - SNAKE_SIZE, self._stack[last_element].y)
        if (self._stack[0].direction == ButtonType.RIGHT):
            new_segment = Segment(self._stack[last_element].x + SNAKE_SIZE, self._stack[last_element].y)
        
        self._stack.append(new_segment)

    #TODO: rewrite this
    def set_direction(self, direction: ButtonType):
        left    = ButtonType.LEFT
        right   = ButtonType.RIGHT
        up      = ButtonType.UP
        down    = ButtonType.DOWN
        if self._direction == left and direction == right or \
            self._direction == right and direction == left:
            pass
        elif self._direction == up and direction == down or \
                self._direction == down and direction == up:
            pass
        else:
            self._direction = direction

    def get_rect(self)-> Tuple[int,int]:
        rect = (self._x, self._y)
        return rect

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

    def draw(self, screen: pygame.display):
        for element in self._stack:
            pygame.draw.rect(screen,element.color,(element.x,element.y,SNAKE_SIZE,SNAKE_SIZE),0)