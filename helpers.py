from typing import Any
from parameters import *
from classes import *
import json

info_attrs: list[str] = ["visteam", "hometeam", "site", "date", 
                           "number", "starttime", "daynight", "usedh", 
                           "innings", "tiebreaker", "umphome", "ump1b", 
                           "ump2b", "ump3b", "umplf", "umprf", "pitches", 
                           "temp", "winddir", "windspeed", "fieldcond", 
                           "precip", "sky", "timeofgame", "attendence", 
                           "wp", "lp", "save"]

json_file = open('game_map.json', 'r')
game_map: dict[str,str] = json.load(json_file)
json_file.close()

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
            elif splitText[0] == pbp_kw_info:
                split_text_value = splitText[2]
                for attr in info_attrs:
                    if attr == splitText[1]:
                        if attr.find('ump') != -1:
                            game.misc.umpires.append(split_text_value)
                        elif attr == 'date':
                            game.date_time.date = datetime.strptime(split_text_value, '%Y/%m/%d').date()
                        elif attr == 'starttime':
                            game.date_time.starttime = datetime.strptime(split_text_value, '%I:%M%p').time()
                        else:
                            first_layer = game_map[attr]
                            member_object = getattr(game, first_layer)
                            setattr(member_object, attr, split_text_value)
                        break

    return games


def WritePlays(plays):
    return