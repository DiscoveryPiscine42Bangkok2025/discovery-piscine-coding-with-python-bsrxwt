def checkmate(board):
    grid = []
    for row in board.splitlines():
        if row.strip() != "":
            grid.append(list(row))

    size = len(grid)
    if size == 0:
        print("Fail")
        return

    for row in grid:
        if len(row) != size:
            print("Fail")
            return

    king_row, king_col = -1, -1
    for i in range(size):
        for j in range(size):
            if grid[i][j] == "K":
                king_row, king_col = i, j

    if king_row == -1:
        print("Fail")
        return

    pawn_moves = [(1, -1), (1, 1)]
    for dr, dc in pawn_moves:
        r = king_row + dr
        c = king_col + dc
        if 0 <= r < size and 0 <= c < size:
            if grid[r][c] == "P":
                print("Success")
                return

    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    for dr, dc in directions:
        r, c = king_row, king_col
        while True:
            r += dr
            c += dc
            if r < 0 or r >= size or c < 0 or c >= size:
                break
            piece = grid[r][c]
            if piece != ".":
                if piece == "R" or piece == "Q":
                    print("Success")
                    return
                break

    directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
    for dr, dc in directions:
        r, c = king_row, king_col
        while True:
            r += dr
            c += dc
            if r < 0 or r >= size or c < 0 or c >= size:
                break
            piece = grid[r][c]
            if piece != ".":
                if piece == "B" or piece == "Q":
                    print("Success")
                    return
                break

    print("Fail")