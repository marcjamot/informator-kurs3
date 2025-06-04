from game import Bot


class Player(Bot):
    def update(self, board):
        # Example implementation only iterating one
        # tile at a time choosing the first available
        for y in range(board.size_y):
            for x in range(board.size_x):
                if board.get(x, y) == 0:
                    board.place(x, y, self.id)
                    return
