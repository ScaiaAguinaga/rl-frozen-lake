import pygame
from reinforcement_agent import QLearningAgent, step

# pygame setup
pygame.init()
screen_dimensions = (1080, 1080)
screen_width, screen_height = screen_dimensions
screen = pygame.display.set_mode(screen_dimensions)
clock = pygame.time.Clock()
running = True
board_size = 4

# Environment Data
agent = QLearningAgent()
num_episodes = 10000
board = [["S", "F", "F", "F"], ["F", "H", "F", "H"], ["F", "F", "F", "H"], ["H", "F", "F", "G"]]

# Trains the agent using Q-learning for a select number of episodes
for episode in range(num_episodes):
    agent_pos = [0, 0]  # Start position for each episode
    done = False

    while not done:
        state = agent.get_state(agent_pos)  # Get current state
        action = agent.choose_action(state)  # Choose action
        next_pos, reward, done = step(agent_pos, action, board)  # Take action and collect result data
        next_state = agent.get_state(next_pos)  # Get new state
        agent.update(state, action, reward, next_state, done)  # Update Q-table
        agent_pos = next_pos  # Update agent position

print("Training complete!")
print("Q-Table:", agent.q_table)

agent.epsilon = 0  # Force to exploit data only
agent_pos = [0, 0]  # Reset agent position for visualization
done = False

# Main game loop for visualization
while running and not done:
    # Handle window close event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Agent chooses and takes action
    state = agent.get_state(agent_pos)
    action = agent.choose_action(state)
    next_pos, reward, done = step(agent_pos, action, board)
    agent_pos = next_pos

    # clears screen
    screen.fill("white")

    # cell size calculation
    cell_size = (screen_width - 96) // board_size

    # Draw cells without borders
    # Colors cells based on typing
    for row in range(board_size):
        for col in range(board_size):
            x = 48 + col * cell_size
            y = 48 + row * cell_size
            cell_type = board[row][col]
            if cell_type == "S":  # Start
                color = "green"
            elif cell_type == "F":  # Frozen
                color = "lightcyan"
            elif cell_type == "H":  # Hole
                color = "midnightblue"
            elif cell_type == "G":  # Goal
                color = "gold"
            pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))

    # Draw grid lines
    border_width = 4
    # Vertical lines
    for i in range(board_size + 1):
        x = 48 + i * cell_size
        pygame.draw.line(screen, "black", (x, 48), (x, 48 + board_size * cell_size), border_width)
    # Horizontal lines
    for i in range(board_size + 1):
        y = 48 + i * cell_size
        pygame.draw.line(screen, "black", (48, y), (48 + board_size * cell_size, y), border_width)

    # Draw Agent
    agent_x = 48 + agent_pos[1] * cell_size + cell_size // 2
    agent_y = 48 + agent_pos[0] * cell_size + cell_size // 2
    pygame.draw.circle(screen, "red", (agent_x, agent_y), cell_size // 3)

    # update display
    pygame.display.flip()

    # Wait 100 milliseconds
    pygame.time.wait(100)

    clock.tick(60)  # limits FPS to 60

pygame.quit()