import time

from main import Snake, Position, Direction

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

def choose_direction(game: Snake):
    head = game.snake[0]

    best_direction = Direction.UP
    best_distance = distance(game.snake[0], game.apple)

    for direction in Direction:
        if not game.is_turn_possible(direction):
            continue

        new_head = head.neighbor(direction)

        if not is_safe(game, new_head):
            continue

        new_distance = distance(new_head, game.apple)

        if new_distance < best_distance:
            best_direction = direction
            best_distance = new_distance

    return best_direction

if __name__ == "__main__":
    game = Snake(10, 10)
    game.display()

    while True:
        time.sleep(0.2)
        direction = choose_direction(game)
        if not game.step(direction):
            break
        game.display()

        print("Game over! Length: " + str(len(game.snake) - 1))