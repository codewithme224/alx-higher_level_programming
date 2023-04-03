import sys

def nqueens(n):
    # Check that n is a valid input
    try:
        n = int(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
        
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
        
    # Initialize an empty board
    board = [['.' for _ in range(n)] for _ in range(n)]
    
    # Recursive function to place queens on the board
    def place_queen(row):
        # If all rows have been filled, print the solution
        if row == n:
            for i in range(n):
                print(' '.join(board[i]))
            print()
            return
        
        # Check each column in the current row to see if a queen can be placed
        for col in range(n):
            if is_valid_placement(board, row, col):
                # Place the queen on the board
                board[row][col] = 'Q'
                # Call the function recursively with the next row
                place_queen(row + 1)
                # Remove the queen from the board to backtrack
                board[row][col] = '.'
    
    # Function to check if a queen can be placed at a given position
    def is_valid_placement(board, row, col):
        # Check the column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        
        # Check the diagonal
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check the other diagonal
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False
        
        return True
    
    # Start the recursive function at the first row
    place_queen(0)
    
    
if __name__ == '__main__':
    # Check that the program was called with the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    nqueens(sys.argv[1])

