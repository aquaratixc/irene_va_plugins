# Запуск приложений в орперационной системе Linux 
# author: Oleg Bakharev (inspired by Vladislav Janvarev)
# based on: https://github.com/Lolipol/Irine-plugin/blob/main/plugin_open_win.py (by Lolipop)

import subprocess

from vacore import VACore

# инциалиазация
# ! не забудьте в файл options/plugin_apprunner.json внести свои команды !
def start(core: VACore):
    manifest = {
        'name': 'Открыть программу (в linux) по настраиваемой команде',
        'version': '1.0',
        'require_online': False,

        'commands': {

        },

        'default_options': {
            'cmds': {
                'браузер|веб': 'firefox',
            }
        }
    }
    return manifest


# работа с манифестом
def start_with_options(core: VACore, manifest: dict):
    cmds = {}
    cmdoptions = manifest['options']['cmds']
    
    print(cmdoptions)
    
    for cmd in cmdoptions.keys():
        cmds[cmd]  = (run_via_irene, cmdoptions[cmd])
    manifest['commands'] = cmds
    
    return manifest

# запуск программ через Ирину
def run_via_irene(core: VACore, phrase: str, param: str):
	try:
		core.play_voice_assistant_speech('Запускаю программу')
		cmd = subprocess.Popen(param.split(' '))
		return
	except Exception as e:
		core.play_voice_assistant_speech('Не удалось запустить приложение')
