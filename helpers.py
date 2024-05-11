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
            elif splitText[0] == pbp_kw_info:
                split_text_value = splitText[2]
                match splitText[1]:
                    case "visteam":
                        game.misc.visit_team = split_text_value
                    case "hometeam":
                        game.misc.home_team = split_text_value
                    case "site":
                        game.misc.site = split_text_value
                    case "date":
                        game.date_time.date = split_text_value
                    case "number":
                        game.misc.game_num =  split_text_value
                    case "starttime":
                        game.date_time.start_time = split_text_value
                    case "daynight":
                        game.weather.daynight = split_text_value
                    case "usedh":
                        game.misc.usedh = split_text_value
                    case "innings":
                        game.misc.innings = split_text_value
                    case "tiebreaker":
                        game.misc.tiebreaker = split_text_value
                    case "umphome":
                        game.misc.umpires.append(split_text_value)
                    case "ump1b":
                        game.misc.umpires.append(split_text_value)
                    case "ump2b":
                        game.misc.umpires.append(split_text_value)
                    case "ump3b":
                        game.misc.umpires.append(split_text_value)
                    case "umplf":
                        game.misc.umpires.append(split_text_value)
                    case "umprf":
                        game.misc.umpires.append(split_text_value)
                    case "pitches":
                        game.pitcher_info.pitches = split_text_value
                    case "temp":
                        game.weather.temp = split_text_value
                    case "winddir":
                        game.weather.winddir = split_text_value
                    case "windspeed":
                        game.weather.windspeed = split_text_value
                    case "fieldcond":
                        game.weather.fieldcond = split_text_value
                    case "precip":
                        game.weather.precip = split_text_value
                    case "sky":
                        game.weather.sky = split_text_value
                    case "timeofgame":
                        game.date_time.timeofgame = split_text_value
                    case "attendence":
                        game.misc.attendence = split_text_value
                    case "wp":
                        game.pitcher_info.winning_pitcher = split_text_value
                    case "lp":
                        game.pitcher_info.losing_pitcher = split_text_value
                    case "save":
                        game.pitcher_info.save = split_text_value
    return games