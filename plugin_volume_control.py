# Управление громкостью через amixer
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

import subprocess

from vacore import VACore



def start(core:VACore):
    manifest = {
        "name": "Управление громкостью через amixer",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "без звука|выключи звук|заглушить звук|выключить звук|убрать звук|тишина" :  off_volume,
            "восстановить звук|включи звук|включить звук|верни звук|конец тишине" :  on_volume,
            "тише|уменьши громкость|уменьшить громкость|понизить громкость" : down_volume,
            "громче|увеличь громкость|увеличить громкость|повысить громкость" : up_volume,
            "полная громкость|звук на максимум|максимальная громкость" : maximal_volume,
            "минимум звука|звук на минимум|минимальная громкость" : minimal_volume,
        }
    }

    return manifest
    
    
def pass_arg_to_amixer(arg: str):
	try:
		cmd = subprocess.Popen(["amixer", "set", "Master", arg])
		cmd.wait()
		return
	except Exception as e:
		pass
    
def off_volume(core:VACore, phrase: str):
	pass_arg_to_amixer("mute")
		
		
def on_volume(core:VACore, phrase: str):
	pass_arg_to_amixer("unmute")
		
		
def down_volume(core:VACore, phrase: str):
	pass_arg_to_amixer("5%-")


def up_volume(core:VACore, phrase: str):
	pass_arg_to_amixer("5%+")
		
		
def maximal_volume(core:VACore, phrase: str):
	pass_arg_to_amixer("100%")
		
		
def minimal_volume(core:VACore, phrase: str):
	pass_arg_to_amixer("10%")

