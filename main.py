from enum import Enum
from random import randrange
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

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

    def display(self):
        clear()
        for y in range(self.height):
            for x in range(self.width):
                match self.get_field(x, y):
                    case Field.EMPTY:
                        print("⬜", end="")
                    case Field.BODY:
                        print("🟩", end="")
                    case Field.APPLE:
                        print("🟥", end="")
            print()

snake = Snake(5, 5)
snake.display()