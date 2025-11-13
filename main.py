from simulation import simulate_game
from visualization import visualize_step
import statistics

if __name__ == "__main__":
    print("=== VIVIR O MORIR: Simulación en vivo ===\n")

    levels = [2, 4, 8, 16, 32]
    summary = []

    for zombies in levels:
        print(f"\n🧟 Nivel con {zombies} zombies (2 rondas):")
        round_results = []
        for r in range(1, 3):
            print(f"\n--- Ronda {r} ---")
            result, steps = simulate_game(zombies, visualize_step)
            round_results.append((result, steps))
            print(f"Resultado: {result.upper()} en {steps} turnos.")

        wins = sum(1 for r, _ in round_results if r == "win")
        avg_steps = statistics.mean(s for _, s in round_results)
        summary.append((zombies, wins, avg_steps))

        print(f"\n🏁 Resultado global {zombies} zombies → Victorias: {wins}/2 | Promedio: {avg_steps:.1f}")

    print("\n=== RESULTADOS FINALES ===")
    for z, w, st in summary:
        print(f"Zombies: {z:>2} | Victorias: {w}/2 | Promedio turnos: {st:.1f}")

    print("\nJuego terminado 🧠💀")
