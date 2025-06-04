from game import Board, TicTacToe, CenterBot, CornerBot, DownBot, NextBot, RandomBot
from player import Player
import random

BATTLES = 10_000


def main():
    bots = [CenterBot, CornerBot, DownBot, NextBot, RandomBot]

    print("Battle through", BATTLES, "games")
    print("Win/Draw/Lose")
    for botclass in bots:
        bot = botclass(2)
        winners: dict[int, int] = {}
        for i in range(BATTLES):
            player_starting = random.choice([True, False])
            if player_starting:
                p1 = Player(1)
                p2 = bot
            else:
                p1 = bot
                p2 = Player(1)
            game = TicTacToe(Board(4, 4), p1, p2)
            winner = game.run()
            winners[winner] = winners.get(winner, 0) + 1
        print(
            f"VS {bot.name()}: {winners.get(1, 0)}/{winners.get(0, 0)}/{winners.get(2, 0)}"
        )


if __name__ == "__main__":
    main()
