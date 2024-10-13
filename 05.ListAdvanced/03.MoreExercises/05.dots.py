# Directions for moving up, down, left, and right
DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def is_valid_move(board, visited, row, col):
    return (0 <= row < len(board) and
            0 <= col < len(board[0]) and
            board[row][col] == '.' and
            not visited[row][col])

def dfs(board, visited, row, col):
    # Mark the current dot as visited
    visited[row][col] = True
    count = 1  # Start with the current dot

    # Explore all possible directions
    for d_row, d_col in DIRECTIONS:
        new_row, new_col = row + d_row, col + d_col
        if is_valid_move(board, visited, new_row, new_col):
            count += dfs(board, visited, new_row, new_col)  # Count connected dots

    return count

def largest_connected_dots(board):
    n = len(board)
    visited = [[False] * len(board[0]) for _ in range(n)]
    max_count = 0

    for row in range(n):
        for col in range(len(board[row])):
            if board[row][col] == '.' and not visited[row][col]:
                # Start DFS from this dot
                count = dfs(board, visited, row, col)
                max_count = max(max_count, count)  # Update the maximum count

    return max_count

# Example usage
n = int(input())  # Number of rows in the board
board = [input().strip().split() for _ in range(n)]  # Reading the board as a list of lists

# Find the largest connected dots
result = largest_connected_dots(board)
print(result)
