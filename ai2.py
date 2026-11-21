import random
import time

from sklearn.tree import DecisionTreeClassifier, export_text

from ai1 import is_safe, distance, choose_direction
from main import Snake, Direction, Position

def count_room(game: Snake, start: Position):
    if not is_safe(game, start):
        return 0

    reached = [(start.x, start.y)]
    to_visit = [start]

    while len(to_visit) > 0:
        field = to_visit.pop()
        for direction in Direction:
            neighbor = field.neighbor(direction)
            if is_safe(game, neighbor) and (neighbor.x, neighbor.y) not in reached:
                reached.append((neighbor.x, neighbor.y))
                to_visit.append(neighbor)

    return len(reached)

def inspect_direction(game: Snake, direction: Direction):
    head = game.snake[0]
    new_head = head.neighbor(direction)

    dead = 0 if is_safe(game, new_head) else 1
    closer = 1 if distance(new_head, game.apple) < distance(head, game.apple) else 0

    room = 1 if count_room(game, new_head) >= len(game.snake) else 0

    return [dead, closer, room]

examples = []
results = []

game = Snake(10, 10)
for i in range(5000):
    if random.random() < 0.3:
        direction = random.choice(list(Direction))
        while not game.is_turn_possible(direction):
            direction = random.choice(list(Direction))
    else:
        direction = choose_direction(game)

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

model = DecisionTreeClassifier()
model.fit(examples, results)

print("A kovetkezoket tanultam: ")
print(export_text(model, feature_names=["dead", "closer", "room"]))
input("Enter a jatekhoz")

def choose_direction(game: Snake):
    best_direction = Direction.UP
    best_score = -1

    for direction in Direction:
        if not game.is_turn_possible(direction):
            continue

        inspection_result = inspect_direction(game, direction)
        score = model.predict([inspection_result])[0]
        if score > best_score:
            best_score = score
            best_direction = direction

    return best_direction

game = Snake(10, 10)
while True:
    time.sleep(0.2)
    if not game.step(choose_direction(game)):
        break
    game.display()

print("Game over! Length: ", len(game.snake) - 1)