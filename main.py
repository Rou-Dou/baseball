import os
from classes import *
from enum import Enum
from typing import Any
import mypy


pbp: str = "\\Data\\pbp\\"
# gl = str("\\Data\\gl\\")
wd: str = os.getcwd()

# These are the keywords for parsing the play by play txt documents from https://www.retrosheet.org

pbp_kw_id: str = 'id'
pbp_kw_version: str = 'version'
pbp_kw_info: str = 'info'
pbp_kw_start: str = 'start'
pbp_kw_play: str = 'play'
pbp_kw_sub: str = 'sub'
pbp_kw_data: str = 'data'
crlf: str = '\r\n'


playHeader: str = 'game_id, inning, homay, batter_id, balls, strikes, pitchresult, deepLore'

def main():
    readerpbp("2000ANA.EVA")
    # readergl(str("gl2000.txt"))


def readerpbp(file):
    # Using readlines()
    file = pbp + file
    game: Game = Game()
    games: list[Game] = []
    # Strips the newline character
    with open(wd+file, "r") as f:
        for line in f:
            line = line.rstrip(crlf)  # strip out all tailing whitespace
            splitText = line.split(',')
            if splitText[0] == pbp_kw_id:
                game = Game()
                games.append(game)
                game.game_id = splitText[1]
            elif splitText[0] == pbp_kw_play: # play,1,0,knobc001,21,CBBX,S7/7S
                play = Play()
                game.plays.append(play)
                play.inning = int(splitText[1])
                play.homay = int(splitText[2])
                play.batter_id = splitText[3]
                play.balls = int(splitText[4][0])
                play.strikes = int(splitText[4][1])
                play.pitchresult = splitText[5]
                play.deepLore = splitText[6]

    for itrgame in games:
        for itrplay in itrgame.plays:
            print(f'{itrgame} {itrplay}')


def WritePlays(plays):
    return


if __name__ == "__main__":
    main()

