from datetime import datetime, time

class Game:
    def __init__(self) -> None:
        self.game_id: str = ''
        self.plays: list[Play] = []
        self.misc: GameInfoMisc = GameInfoMisc()
        self.weather: GameInfoWeather = GameInfoWeather()
        self.date_time: GameInfoDateTime = GameInfoDateTime()
        self.pitcher_info: GameInfoPitcher = GameInfoPitcher()
    def __str__(self):
        return f'{self.game_id},'

# class to store play information from text file
class Play:
    def __init__(self) -> None:
        self.game_id: str = ''
        self.inning: int = 0
        self.homay: int = 2
        self.batter_id: str = ''
        self.balls: int = -1
        self.strikes: int = -1
        self.pitchresult: str = 'Z'
        self.deepLore: str = ''

    def __str__(self):
        return f'{self.inning}, {self.homay}, {self.batter_id}, {self.balls}, {self.strikes}, {self.pitchresult}, {self.deepLore}'
    
class GameInfoDateTime:
    def __init__(self) -> None:
        self.date: str = ''
        self.start_time: time = time(12, 0, 0, 0, tzinfo=None)
        self.timeofgame: int = 0

class GameInfoWeather:
    def __init__(self) -> None:
        self.daynight: str = ''   
        self.temp: int = 0
        self.winddir: str = ''
        self.windspeed: int = 0
        self.fieldcond: str = 'unknown'
        self.precip: str = 'none'
        self.sky: str = ''

class GameInfoMisc:
    def __init__(self) -> None:
        self.game_num: int = 0
        self.visit_team: str = ''
        self.home_team: str = ''
        self.site: str = ''
        self.innings: int = 9
        self.tiebreaker: int = 2
        self.usedh: bool = True
        self.umpires: list[str] = []
        self.attendence:int = 0

class GameInfoPitcher:
    def __init__(self) -> None:
        self.winning_pitcher: str = ''
        self.losing_pitcher: str = ''
        self.save: str = ''