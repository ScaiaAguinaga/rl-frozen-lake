import numpy as np
import random

class QLearningAgent:
  def __init__(self, board_size=4):
    self.board_size = board_size
    # Q-table: rows are states, columns are actions (up, right, down, left)
    self.q_table = np.zeros((board_size * board_size, 4))
    self.alpha = 0.1  # How fast to learn
    self.gamma = 0.99  # How much to care about the future
    self.epsilon = 0.9  # How often to explore the unknown
  
  # Converts row and col into a single state number
  def get_state(self, pos):
    row, col = pos
    state = row * self.board_size + col
    return state
  
  # Epsilon-greedy action selection: explore vs. exploit
  def choose_action(self, state):
    if random.random() < self.epsilon:
      return random.randint(0, 3)
    else:
      return np.argmax(self.q_table[state])
  
  # Q-learning update rule
  def update(self, state, action, reward, next_state, done):
    q_curr = self.q_table[state][action]
    if done:
      target = reward  # No future reward upon episode end
    else:
      q_next_max = np.max(self.q_table[next_state])
      target = reward + self.gamma * q_next_max
    self.q_table[state][action] = q_curr + self.alpha * (target - q_curr)

# Simulates environment respons to the agent's action
def step(pos, action, board):
  slip = random.randint(1,5)  # 40% chance to slip (change to adjacent direction)
  slip_cc = {0: 3, 1: 0, 2: 1, 3: 2}  # Couinter-clockwise slip
  slip_cw = {0: 1, 1: 2, 2: 3, 3: 0}  # Clockwise slip
  row, col = pos

  # Apply slip with 40% probability
  if slip == 1:
    action = slip_cc[action]
  elif slip == 2:
    action = slip_cw[action]

  # Move agent based on action (0=UP, 1=RIGHT, 2=DOWN, 3=LEFT)
  if action == 0:  # UP
    row = max(0, row - 1)
  elif action == 1:  # RIGHT
    col = min(len(board[0]) - 1, col + 1)
  elif action == 2:  # DOWN
    row = min(len(board) - 1, row + 1)
  elif action == 3:  # LEFT
    col = max(0, col - 1)

  new_pos = [row, col]
  tile = board[row][col]
  
  # Determine reward and whether the episode is done
  if tile == "H":
    return new_pos, -1, True  # Fell in hole
  elif tile == "G":
    return new_pos, +1, True  # Found goal
  else:
    return new_pos, 0, False  # Normal step