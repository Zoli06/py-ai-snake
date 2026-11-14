import time
import keyboard
from enum import Enum
from random import randrange
import os
from math import floor

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

class Position:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def copy(self) -> Position:
        return Position(self.x, self.y)

    def equals(self, other: Position) -> bool:
        return self.x == other.x and self.y == other.y

    def neighbor(self, direction: Direction) -> Position:
        new_position = self.copy()
        match direction:
            case Direction.UP:
                new_position.y -= 1
            case Direction.RIGHT:
                new_position.x += 1
            case Direction.DOWN:
                new_position.y += 1
            case Direction.LEFT:
                new_position.x -= 1
        return new_position

class Snake:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

        self.snake = [Position(floor(self.width/2), floor(self.height/2))]
        self.apple = Position()
        self.new_apple_position()

        self.direction = Direction.UP

    def is_new_head_position_valid(self) -> bool:
        return self.is_head_inside_field() and not self.is_head_in_body()

    def is_head_in_body(self) -> bool:
        for i in range(1, len(self.snake)):
            if self.snake[0].equals(self.snake[i]):
                return True
        return False

    def is_head_inside_field(self):
        return 0 <= self.snake[0].x < self.width and 0 <= self.snake[0].y < self.height

    def is_apple_on_snake(self):
        for body_part in self.snake:
            if body_part.equals(self.apple):
                return True
        return False

    def new_apple_position(self):
        self.apple.x = randrange(self.width)
        self.apple.y = randrange(self.height)
        if self.is_apple_on_snake():
            self.new_apple_position()

    def display(self):
        clear()

        field = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                row.append(Field.EMPTY)
            field.append(row)

        for body_part in self.snake:
            field[body_part.y][body_part.x] = Field.BODY

        field[self.apple.y][self.apple.x] = Field.APPLE

        for y in range(self.height):
            for x in range(self.width):
                match field[y][x]:
                    case Field.EMPTY:
                        print("⬜", end="")
                    case Field.BODY:
                        print("🟩", end="")
                    case Field.APPLE:
                        print("🟥", end="")
            print()

    def is_turn_possible(self, new_direction: Direction):
        return (not ((self.direction == Direction.UP and new_direction == Direction.DOWN) or
                    (self.direction == Direction.RIGHT and new_direction == Direction.LEFT) or
                    (self.direction == Direction.DOWN and new_direction == Direction.UP) or
                    (self.direction == Direction.LEFT and new_direction == Direction.RIGHT)) or
                len(self.snake) == 1)


    # Moves the snake one step. Returns False if the snake died.
    # Other scripts (like the AI) can call this to control the snake.
    def step(self, direction: Direction) -> bool:
        if self.is_turn_possible(direction):
            new_position = self.snake[0].neighbor(direction)
            self.direction = direction
        else:
            new_position = self.snake[0].neighbor(self.direction)

        self.snake.insert(0, new_position)
        if not self.is_new_head_position_valid():
            return False

        if self.apple.equals(new_position):
            self.new_apple_position()
        else:
            self.snake.pop()

        return True

    def play(self):
        while True:
            new_direction = self.direction
            t_end = time.time() + 1
            while time.time() < t_end:
                if keyboard.is_pressed("up arrow"):
                    new_direction = Direction.UP
                elif keyboard.is_pressed("right arrow"):
                    new_direction = Direction.RIGHT
                elif keyboard.is_pressed("down arrow"):
                    new_direction = Direction.DOWN
                elif keyboard.is_pressed("left arrow"):
                    new_direction = Direction.LEFT

            if not self.step(new_direction):
                break

            self.display()

# This only runs when you start main.py directly, not when another script imports it
if __name__ == "__main__":
    snake = Snake(10, 10)
    snake.play()