from helpers import *
import mypy

playHeader: str = 'game_id, inning, homay, batter_id, balls, strikes, pitchresult, deepLore'

def main():
    games: list[Game] = readerpbp(file_name)

    for itrgame in games:
        for itrplay in itrgame.plays:
            print(f'{itrgame} {itrplay}')


def WritePlays(plays):
    return


if __name__ == "__main__":
    main()

