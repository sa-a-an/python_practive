import enum


import enum
from tkinter import RIGHT

SPEED = 0.30
SNAKE_SIZE    = 20
APPLE_SIZE    = SNAKE_SIZE
SEPARATION    = 1
SCREEN_HEIGHT = 600
SCREEN_WIDTH  = 800
FPS           = 1
MSG_PADDING   = 20

BLACK   = (0, 0, 0)
WHITE   = (255, 255, 255)
GREEN   = (0, 255, 0)
RED     = (255, 0, 0)
ORRANGE = (255, 165, 0)
YELLOW  = (255, 165, 0)

SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT / 2
SCREEN_WIDTH_CENTER  = SCREEN_WIDTH / 2

class DirectionType(enum.Enum):
    UP      = enum.auto()
    DOWN    = enum.auto()
    LEFT    = enum.auto()
    RIGHT   = enum.auto()

class SystemButtonType(enum.Enum):
    EXIT    = enum.auto()
    YES     = enum.auto()
    NO      = enum.auto()