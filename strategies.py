import random
from config import WIDTH, HEIGHT, DIRECTIONS
from math import exp

def in_bounds(pos):
    x, y = pos
    return 0 <= x < WIDTH and 0 <= y < HEIGHT

def neighbors(pos):
    x, y = pos
    for dx, dy in DIRECTIONS:
        np = (x + dx, y + dy)
        if in_bounds(np):
            yield np

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def survivor_eval(pos, zombies):
    """Evalúa qué tan buena es una posición para el sobreviviente."""
    if not zombies:
        return 100

    d_min = min(manhattan(pos, z) for z in zombies)
    avg_d = sum(manhattan(pos, z) for z in zombies) / len(zombies)

    # Penaliza cercanía extrema
    if d_min == 0:
        danger = -100
    elif d_min == 1:
        danger = -40
    elif d_min == 2:
        danger = -10
    else:
        danger = 0

    return 2.5 * avg_d + danger

def is_caught(survivor, zombies):
    return any(z == survivor for z in zombies)

def zombies_move_adversarial(survivor, zombies):
    """Zombies se mueven para acercarse localmente al sobreviviente."""
    new_positions = []
    for z in zombies:
        best = z
        best_dist = manhattan(z, survivor)
        for nb in neighbors(z):
            d = manhattan(nb, survivor)
            if d < best_dist:
                best_dist = d
                best = nb
        new_positions.append(best)
    return new_positions

def zombies_move_random(zombies):
    """Movimiento aleatorio para simulación Expectimax."""
    return [random.choice(list(neighbors(z))) for z in zombies]

def survivor_expectimax_move(pos, zombies, depth=3, samples=8):
    """Sobreviviente usa Expectimax para maximizar esperanza de supervivencia."""
    def max_layer(p, z, d):
        if is_caught(p, z):
            return -9999, p
        if d == 0:
            return survivor_eval(p, z), p
        best_val, best_move = -float("inf"), p
        for m in neighbors(p):
            val = exp_layer(m, z, d - 1)
            if val > best_val:
                best_val, best_move = val, m
        return best_val, best_move

    def exp_layer(p, z, d):
        vals = []
        for _ in range(samples):
            new_z = zombies_move_random(z)
            v, _ = max_layer(p, new_z, d)
            vals.append(v)
        return sum(vals) / len(vals)

    val, move = max_layer(pos, zombies, depth)
    return move
