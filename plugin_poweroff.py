# Плагин для отключения/перезагрузки компьютера
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

# Голосовое отключение компьютера
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

import subprocess

from vacore import VACore

def start(core: VACore):
    manifest = {
        'name': 'Отключение и перезагрузка компьютера',
        'version': '1.0',
        'require_online': False,

        'commands': {
            'выключи компьютер|отключить питание|отключи питание|выключить компьютер|отключение|выключение':  poweroff,
            'перезагрузи компьютер|перезагрузить компьютер|перезагрузка':  reboot,
        }
    }

    return manifest
    
# отключение питания    
def poweroff(core: VACore, phrase: str):
	try:
		core.play_voice_assistant_speech('Выполняю выключение компьютера')
		cmd = subprocess.Popen(['poweroff'])
		cmd.wait()
		return
	except Exception as e:
		pass
		
# перезагрузка		
def reboot(core: VACore, phrase: str):
	try:
		core.play_voice_assistant_speech('Выполняю перезагрузку компьютера')
		cmd = subprocess.Popen(['reboot'])
		cmd.wait()
		return
	except Exception as e:
		pass