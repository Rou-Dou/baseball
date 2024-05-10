from typing import Any
from parameters import *
from classes import *

def readerpbp(file) -> list[Game]:
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
                
    return games