# Управление плеером mpg123
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

import os
import random
import subprocess

from vacore import VACore

music_dir = 'путь к папке с музыкой'
music_files = os.listdir(music_dir)
number = 0
cmd = None

def start(core: VACore):
    manifest = {
        "name": "Управление плеером mpg123",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "случайная песня|случайная дорожка|случайный трэк|случайный":  random_track,
            "остановить|стоп|остановить проигрывание|музыка стоп":  stop_playing,
            "следующий|следующий трэк|следующая дорожка|дальше|вперёд": next_playing,
            "предыдущий|предыдущий трэк|предыдущая дорожка|назад": prev_playing,
        }
    }

    return manifest
   
    
def pass_arg_to_mpg(arg: str):
	try:
		global cmd
		cmd = subprocess.Popen(["mpg123", arg])
		return
	except Exception as e:
		pass
    
    
def random_track(core: VACore, phrase: str):
    if not cmd == None:
        cmd.kill()
    global number
    number = random.randint(0, len(music_files)-1)
    track = music_files[number]
    pass_arg_to_mpg(music_dir + '/' + track)


def stop_playing(core: VACore, phrase: str):
    if not cmd == None:
        cmd.kill()


def next_playing(core: VACore, phrase: str):
    if not cmd == None:
        cmd.kill()
        global number
        number = (number + 1) % len(music_files)
        track = music_files[number]
        pass_arg_to_mpg(music_dir + '/' + track)


def prev_playing(core: VACore, phrase: str):
    if not cmd == None:
        cmd.kill()
        global number
        if (number - 1) >= 0:
            number = (number - 1)
        else:
            number = 0
        track = music_files[number]
        pass_arg_to_mpg(music_dir + '/' + track)
