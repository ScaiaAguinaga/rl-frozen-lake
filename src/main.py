import pygame

# pygame setup
pygame.init()
screen_dimensions = (1080, 1080)
screen_width, screen_height = screen_dimensions
screen = pygame.display.set_mode(screen_dimensions)
clock = pygame.time.Clock()
running = True

# Test Data
board_size = 4
board = [["S", "F", "F", "F"], ["F", "H", "F", "H"], ["F", "F", "F", "H"], ["H", "F", "F", "G"]]

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    cell_size = (screen_width - 96) // board_size

    # Draw cells without borders
    for row in range(board_size):
        for col in range(board_size):
            x = 48 + col * cell_size
            y = 48 + row * cell_size
            cell_type = board[row][col]
            if cell_type == "S":
                color = "green"
            elif cell_type == "F":
                color = "lightcyan"
            elif cell_type == "H":
                color = "midnightblue"
            elif cell_type == "G":
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



    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()