import os
from enum import Enum
from typing import Any


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


# this is for determining the home or away status of the team
class Homay(Enum):
    away = 0
    home = 1
    invalid = 2


# this is for determining the pitch result based on the value in the text
class PitchResult(Enum):
    B = 0   # ball
    C = 1   # called strike
    F = 2   # foul
    H = 3   # hit batter
    I = 4   # intentional ball
    K = 5   # strike (unknown type)
    L = 6   # foul bunt
    M = 7   # missed bunt attempt
    N = 8   # no pitch (on balks and interference calls)
    O = 9   # foul tip on bunt
    P = 10  # pitchout
    Q = 11  # swinging on pitchout
    R = 12  # foul ball on pitchout
    S = 13  # swinging strike
    T = 14  # foul tip
    U = 15  # unknown or missed pitch
    V = 16  # called ball because pitcher went to his mouth or automatic ball on intentional walk
    X = 17  # ball put into play by batter
    Y = 18  # ball put into play on pitchout
    Z = -1  # Invalid


playHeader: str = 'game_id, inning, homay, batter_id, balls, strikes, pitchresult, deepLore'

# class to store play information from text file
class Play:
    def __init__(self) -> None:
        self.game_id: str = ''
        self.inning = 0
        self.homay = Homay.invalid
        self.batter_id: str = ''
        self.balls: int = -1
        self.strikes: int = -1
        self.pitchresult: Enum = PitchResult.Z
        self.deepLore: str = ''

    def __str__(self):
        return f'{self.inning}, {self.homay}, {self.batter_id}, {self.balls}, \
                {self.strikes}, {self.pitchresult}, {self.deepLore}'


class Game:
    game_id: str = ''
    plays: list[Play] = []

    def __str__(self):
        return f'{self.game_id}, '


def main():
    readerpbp("2000ANA.EVA")
    # readergl(str("gl2000.txt"))


def readerpbp(file):
    # Using readlines()
    file = pbp + file
    game: Game = {}
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
                play.inning = splitText[1]
                play.homay = splitText[2]
                play.batter_id = splitText[3]
                play.balls = splitText[4][0]
                play.strikes = splitText[4][1]
                play.pitchresult = splitText[5]
                play.deepLore = splitText[6]

    for itrgame in games:
        for itrplay in itrgame.plays:
            print(f'{itrgame} {itrplay}')


def WritePlays(plays):
    return


if __name__ == "__main__":
    main()

