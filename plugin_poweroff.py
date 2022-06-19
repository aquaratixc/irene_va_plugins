# Голосовое отключение компьютера
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

import subprocess

from vacore import VACore



def start(core:VACore):
    manifest = {
        "name": "Голосовое отключение компьютера",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "выключи компьютер|отключить питание|отключи питание|выключить компьютер|отключение|выключение" :  poweroff,
            "перезагрузи компьютер|перезагрузить компьютер|перезагрузка" :  poweroff,
        }
    }

    return manifest
    
    
def poweroff(core:VACore, phrase: str):
	try:
		core.play_voice_assistant_speech("Выполняю выключение компьютера")
		cmd = subprocess.Popen(["poweroff"])
		cmd.wait()
		return
	except Exception as e:
		pass
		
		
def reboot(core:VACore, phrase: str):
	try:
		core.play_voice_assistant_speech("Выполняю перезагрузку компьютера")
		cmd = subprocess.Popen(["reboot"])
		cmd.wait()
		return
	except Exception as e:
		pass
