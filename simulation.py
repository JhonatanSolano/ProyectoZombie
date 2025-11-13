import random
from config import SURVIVOR_START, MAX_TURNS
from strategies import survivor_expectimax_move, zombies_move_adversarial, is_caught

def simulate_game(num_zombies, visualize_step=None):
    survivor = SURVIVOR_START
    zombies = [(random.randint(0, 14), random.randint(0, 9)) for _ in range(num_zombies)]
    survivor_path = [survivor]
    zombies_paths = [[z] for z in zombies]

    for turn in range(1, MAX_TURNS + 1):
        # Movimiento del sobreviviente
        new_survivor = survivor_expectimax_move(survivor, zombies)
        survivor = new_survivor

        # Movimiento de zombies
        zombies = zombies_move_adversarial(survivor, zombies)
        for i, z in enumerate(zombies):
            zombies_paths[i].append(z)

        # Visualización paso a paso
        if visualize_step:
            visualize_step(turn, survivor, zombies, survivor_path, zombies_paths)

        # Verificar si lo atraparon
        if is_caught(survivor, zombies):
            return "lose", turn

        survivor_path.append(survivor)

    # Si sobrevivió los 10 turnos
    return "win", MAX_TURNS
