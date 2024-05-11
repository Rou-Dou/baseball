from helpers import *
import mypy

playHeader: str = 'game_id, inning, homay, batter_id, balls, strikes, pitchresult, deepLore'

def main():
    games: list[Game] = readerpbp(file_name)

    # for itrgame in games:
    #     for itrplay in itrgame.plays:
    #         print(f'{itrgame} {itrplay}')

    for itrgame in games:
        print(f'{itrgame.date_time.date}, {itrgame.date_time.starttime}, {itrgame.date_time.timeofgame}')


if __name__ == "__main__":
    main()

