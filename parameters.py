import os

pbp: str = "\\Data\\pbp\\"
# gl = str("\\Data\\gl\\")
wd: str = os.getcwd()
file_name = "2000ANA.EVA"

# These are the keywords for parsing the play by play txt documents from https://www.retrosheet.org

pbp_kw_id: str = 'id'
pbp_kw_version: str = 'version'
pbp_kw_info: str = 'info'
pbp_kw_start: str = 'start'
pbp_kw_play: str = 'play'
pbp_kw_sub: str = 'sub'
pbp_kw_data: str = 'data'
crlf: str = '\r\n'