from abc import ABC, abstractmethod
import random


class Board:
    board: list[int]
    size_x: int
    size_y: int

    def __init__(self, size_x: int, size_y: int):
        self.board = [0] * (size_x * size_y)
        self.size_x = size_x
        self.size_y = size_y

    def get(self, x, y) -> int:
        return self.board[y * self.size_x + x]

    def place(self, x, y, player):
        if self.board[y * self.size_x + x] != 0:
            raise ValueError("Position already taken")
        self.board[y * self.size_x + x] = player


class Bot(ABC):
    id: int

    def __init__(self, id: int):
        self.id = id

    @abstractmethod
    def update(self, board: Board):
        raise NotImplementedError()

    def name(self) -> str:
        return "Player"


class RandomBot(Bot):
    def update(self, board: Board):
        # Find all available positions (cells with value 0)
        available_positions = []
        for y in range(board.size_y):
            for x in range(board.size_x):
                if board.get(x, y) == 0:
                    available_positions.append((x, y))

        # If there are available positions, place randomly
        if available_positions:
            x, y = random.choice(available_positions)
            board.place(x, y, self.id)

    def name(self) -> str:
        return "Random"


class NextBot(Bot):
    def update(self, board):
        for y in range(board.size_y):
            for x in range(board.size_x):
                if board.get(x, y) == 0:
                    board.place(x, y, self.id)
                    return

    def name(self) -> str:
        return "Next"


class CenterBot(Bot):
    def update(self, board: Board):
        # Try to place in center first
        center_x, center_y = board.size_x // 2, board.size_y // 2
        if board.get(center_x, center_y) == 0:
            board.place(center_x, center_y, self.id)
            return

        # If center is taken, find any available spot
        for y in range(board.size_y):
            for x in range(board.size_x):
                if board.get(x, y) == 0:
                    board.place(x, y, self.id)
                    return

    def name(self) -> str:
        return "Center"


class CornerBot(Bot):
    def update(self, board: Board):
        # Try corners first
        corners = [
            (0, 0),
            (board.size_x - 1, 0),
            (0, board.size_y - 1),
            (board.size_x - 1, board.size_y - 1),
        ]
        for x, y in corners:
            if board.get(x, y) == 0:
                board.place(x, y, self.id)
                return

        # If no corners available, find any spot
        for y in range(board.size_y):
            for x in range(board.size_x):
                if board.get(x, y) == 0:
                    board.place(x, y, self.id)
                    return

    def name(self) -> str:
        return "Corner"


class DownBot(Bot):
    def __init__(self, id: int):
        super().__init__(id)

    def update(self, board: Board):
        # Try to place starting from (2, 0) and going down
        for y in range(board.size_y):
            if board.get(2, y) == 0:
                board.place(2, y, self.id)
                return

        # If exhausted go random
        available_positions = []
        for y in range(board.size_y):
            for x in range(board.size_x):
                if board.get(x, y) == 0:
                    available_positions.append((x, y))

        if available_positions:
            x, y = random.choice(available_positions)
            board.place(x, y, self.id)

    def name(self) -> str:
        return "Down"


class TicTacToe:
    def __init__(self, board: Board, player1: Bot, player2: Bot):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    def check_winner(self) -> int:
        # Check rows
        for y in range(self.board.size_y):
            for x in range(self.board.size_x - 2):
                if (
                    self.board.get(x, y)
                    == self.board.get(x + 1, y)
                    == self.board.get(x + 2, y)
                    != 0
                ):
                    return self.board.get(x, y)

        # Check columns
        for x in range(self.board.size_x):
            for y in range(self.board.size_y - 2):
                if (
                    self.board.get(x, y)
                    == self.board.get(x, y + 1)
                    == self.board.get(x, y + 2)
                    != 0
                ):
                    return self.board.get(x, y)

        # Check diagonals (top-left to bottom-right)
        for y in range(self.board.size_y - 2):
            for x in range(self.board.size_x - 2):
                if (
                    self.board.get(x, y)
                    == self.board.get(x + 1, y + 1)
                    == self.board.get(x + 2, y + 2)
                    != 0
                ):
                    return self.board.get(x, y)

        # Check diagonals (top-right to bottom-left)
        for y in range(self.board.size_y - 2):
            for x in range(2, self.board.size_x):
                if (
                    self.board.get(x, y)
                    == self.board.get(x - 1, y + 1)
                    == self.board.get(x - 2, y + 2)
                    != 0
                ):
                    return self.board.get(x, y)

        return 0

    def is_board_full(self) -> bool:
        for y in range(self.board.size_y):
            for x in range(self.board.size_x):
                if self.board.get(x, y) == 0:
                    return False
        return True

    def run(self) -> int:
        current_bot = self.player1
        winner = 0

        while True:
            current_bot.update(self.board)

            winner = self.check_winner()
            if winner != 0:
                break
            if self.is_board_full():
                break

            current_bot = self.player2 if current_bot == self.player1 else self.player1

        return winner

    def print(self):
        for y in range(self.board.size_y):
            row = []
            for x in range(self.board.size_x):
                cell = self.board.get(x, y)
                if cell == 0:
                    row.append(" ")
                else:
                    row.append(str(cell))
            print("|".join(row))
            if y < self.board.size_y - 1:
                print("-" * (self.board.size_x * 2 - 1))
