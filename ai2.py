import random

from ai1 import is_safe, distance
from main import Snake, Direction

def inspect_direction(game: Snake, direction: Direction):
    head = game.snake[0]
    new_head = head.neighbor(direction)

    dead = 0 if is_safe(game, new_head) else 1
    closer = 1 if distance(new_head, game.apple) < distance(head, game.apple) else 0

    return [dead, closer]

examples = []
results = []

game = Snake(10, 10)
for i in range(5000):
    direction = random.choice(list(Direction))
    while not game.is_turn_possible(direction):
        direction = random.choice(list(Direction))

    inspection_result = inspect_direction(game, direction)

    length_before = len(game.snake)
    distance_before = distance(game.snake[0], game.apple)

    alive = game.step(direction)

    if not alive:
        result = 0
        game = Snake(10, 10)
    elif distance(game.snake[0], game.apple) < distance_before:
        result = 2
    elif len(game.snake) > length_before:
        result = 2
    else:
        result = 1

    examples.append(inspection_result)
    results.append(result)