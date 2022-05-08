import pygame
from constants import *

class Apple():

    def __init__(self, x: int, y: int, state):
        self._x = x
        self._y = y
        self._state = state

    def draw(self, screen: pygame.display):
        pygame.draw.rect(screen, ORRANGE, (self._x, self._y, APPLE_SIZE, APPLE_SIZE),0)