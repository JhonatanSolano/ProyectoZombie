## 🧟‍♂️ Vivir o Morir: Simulación de Supervivencia

## 🎯 Descripción

**Vivir o Morir** es un proyecto de simulación desarrollado en **Python** que modela una partida entre un *sobreviviente inteligente* y una *horda de zombies* dentro de un entorno bidimensional.

El **sobreviviente**, controlado por un agente **Expectimax**, busca **maximizar su probabilidad de supervivencia** durante 10 turnos, mientras los **zombies**, guiados por una estrategia **Minimax local (greedy)**, intentan atraparlo reduciendo la distancia entre ellos.  
La simulación incluye una **visualización animada** en tiempo real usando `matplotlib`, donde se observan los movimientos y estrategias de ambos bandos.

## 🧠 Lógica del Proyecto

| Agente | Estrategia | Tipo de decisión | Racionalidad |
| ------- | ----------- | ---------------- | ------------- |
| **Sobreviviente** | Expectimax | Basada en expectativas (mundo estocástico) | No asume que el enemigo es perfecto |
| **Zombies** | Minimax local (greedy) | Basada en minimización (mundo determinista) | Persigue y rodea al sobreviviente |

- **Expectimax**: el sobreviviente evalúa múltiples escenarios posibles (muestreados aleatoriamente) y elige el movimiento con **mayor esperanza de supervivencia**.  
- **Minimax local**: los zombies actúan **miopemente**, buscando minimizar la distancia al sobreviviente sin prever el futuro global.  
- El juego termina cuando el sobreviviente **dura 10 turnos** (victoria) o es **atrapado** (derrota).

## ⚙️ Estructura del Proyecto

## Estructura del Proyecto

* **ProyectoZombie/**
    * `config.py` # Parámetros globales (tamaño del mapa, turnos, direcciones, etc.)
    * `strategies.py` # Implementación de Expectimax (sobreviviente) y Minimax local (zombies)
    * `simulation.py` # Lógica principal de la simulación y manejo del estado del juego
    * `visualization.py` # Visualización animada en tiempo real con Matplotlib
* `main.py` # Archivo principal para ejecutar el proyecto
* `requirements.txt` # Dependencias del entorno
* `Proyecto_2_IA.pdf` # Informe académico completo
* `README.md` # Este documento

## 📄 Reporte del Proyecto
[📘 Ver o descargar el informe en PDF](Proyecto_2___IA.pdf)

## 📋 Requisitos

Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
