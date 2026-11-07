from enum import Enum
from random import randrange
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

class Field(Enum):
    EMPTY = 1
    BODY = 2
    APPLE = 3

class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

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

        self.direction = Direction(randrange(1, 5))
        self.position_x = snake_x
        self.position_y = snake_y

    def get_field(self, x: int, y: int) -> Field:
        return self.field[y][x]

    def set_field(self, x: int, y: int, value: Field):
        self.field[y][x] = value

    def is_position_valid(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

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

    def move(self, grow: bool) -> bool:
        new_x = self.position_x
        new_y = self.position_y
        match self.direction:
            case Direction.UP:
                new_y -= 1
            case Direction.RIGHT:
                new_x += 1
            case Direction.DOWN:
                new_y += 1
            case Direction.LEFT:
                new_x -= 1

        if not self.is_position_valid(new_x, new_y):
            return False

        self.set_field(new_x, new_y, Field.BODY)

        # kovi oran Queue folytatjuk

        return True


snake = Snake(5, 5)
snake.display()