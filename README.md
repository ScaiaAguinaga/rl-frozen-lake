# Q-Learning GridWorld Agent

This project demonstrates a simple Q-learning agent trained to navigate a 4x4 grid-based environment using reinforcement learning principles. The agent is visualized using the `pygame` library and is designed to learn the optimal policy for reaching a goal tile while avoiding holes.

---

## 🧠 Overview

The environment consists of a 4x4 grid with the following cell types:

- 🟩 `S` - Start position (green)
- 🧊 `F` - Frozen safe tile (light cyan)
- 🕳️ `H` - Hole (midnight blue): ends the episode with negative reward
- 🏁 `G` - Goal (gold): ends the episode with positive reward

The agent learns using the **Q-learning algorithm**, where it explores different paths and updates a Q-table to optimize decision-making over time.

---

## 🚀 Features

- **Q-Learning Agent** with epsilon-greedy strategy
- **Training loop** with customizable number of episodes
- **Visualization** of the grid environment using `pygame`
- **Stochastic dynamics**: 40% chance to "slip" to adjacent direction on movement
- Agent **learns to avoid holes** and reach the goal effectively over time

---

## 📂 File Structure

- `main.py`: Runs the training loop and starts the Pygame visualization
- `reinforcement_agent.py`: Contains the Q-learning agent class and environment transition logic

---

## 🛠️ How It Works

### Q-Learning Formula

The Q-values are updated using the following rule:
Q(s, a) ← Q(s, a) + α * [r + γ * max(Q(s', a')) - Q(s, a)]


Where:
- `α` (alpha): Learning rate
- `γ` (gamma): Discount factor
- `ε` (epsilon): Probability of exploring random actions

### Training Process

1. Start at `S`
2. Choose an action (ε-greedy)
3. Apply the action (with 40% chance of slipping)
4. Update Q-table based on received reward and next state
5. Repeat until the agent reaches a terminal state (`H` or `G`)

---

## 🎮 Controls & Visualization

- Run `main.py` to start training and launch the visualization.
- Once training is complete, the agent will navigate the board visually using its learned policy.
- The red circle represents the agent's current position.

---

## 📦 Requirements

Install the required dependencies:

```bash
pip install pygame numpy
