def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
def diagonal_winner(board):
    diag1 = board[0][0] + board[1][1] + board[2][2]
    diag2 = board[0][2] + board[1][1] + board[2][0]
    return (
        (diag1[0] == diag1[1] == diag1[2]) or 
        (diag2[0] == diag2[1] == diag2[2])
        )

assert_equal(
    diagonal_winner(
        [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'O', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['X', 'X', 'O'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
    ),
    True
)

assert_equal(
    diagonal_winner(
        [
            ['O', 'X', 'O'],
            ['X', 'X', 'X'],
            ['O', 'O', 'X']
        ]
    ),
    False
)