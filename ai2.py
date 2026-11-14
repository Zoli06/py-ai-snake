from ai1 import is_safe, distance
from main import Snake, Direction

def inspect_direction(game: Snake, direction: Direction):
    head = game.snake[0]
    new_head = head.neighbor(direction)

    dead = 0 if is_safe(game, new_head) else 1
    closer = 1 if distance(new_head, game.apple) < distance(head, game.apple) else 0

    return [dead, closer]