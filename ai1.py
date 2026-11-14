from main import Snake, Position

def is_safe(game: Snake, position: Position) -> bool:
    if position.x < 0 or position.x >= game.width:
        return False
    if position.y < 0 or position.y >= game.height:
        return False

    for body_part in game.snake:
        if body_part.equals(position):
            return False

    return True

def distance(a: Position, b: Position):
    return abs(a.x - b.x) + abs(a.y - b.y)

