from enum import Enum
from random import randrange

class Field(Enum):
    EMPTY = 1
    BODY = 2
    APPLE = 3

class Snake:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.field = []
        for i in range(height):
            row = []
            for j in range(width):
                row.append(Field.EMPTY)
            self.field.append(row)

        apple_x = apple_y = snake_x = snake_y = 0
        while apple_x == snake_x and apple_y == snake_y:
            apple_x = randrange(self.width)
            apple_y = randrange(self.height)
            snake_x = randrange(self.width)
            snake_y = randrange(self.height)

        self.set_field(apple_x, apple_y, Field.APPLE)
        self.set_field(snake_x, snake_y, Field.BODY)

    def get_field(self, x: int, y:int):
        return self.field[y][x]

    def set_field(self, x: int, y: int, value: Field):
        self.field[y][x] = value
