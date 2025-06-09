def step(pos, action, board):
  row, col = pos
  if action == 1:  # UP
    row = max(0, row - 1)
  if action == 2:  # RIGHT
    col = min(len(board[0]) - 1, col + 1)
  if action == 3:  # DOWN
    row = min(len(board) - 1, row + 1)
  if action == 4:  # LEFT
    col = max(0, col - 1)

  new_pos = [row, col]
  tile = board[row][col]
  
  if tile == "H":
    return new_pos, -1, True  # Fell in hole
  elif tile == "G":
    return new_pos, +1, True  # Found goal
  else:
    return new_pos, 0, False  # Normal step