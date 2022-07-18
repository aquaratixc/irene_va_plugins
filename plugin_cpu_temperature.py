# Информация о температуре процессора
# author: Oleg Bakharev (inspired by Vladislav Janvarev)


import subprocess

from vacore import VACore


def start(core: VACore):
    manifest = {
        "name": "Температура Ирины",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "твоя температура|температура|температура процессора|нагрев":  get_temperature,
        }
    }

    return manifest


# вычисляет вариант текста для конкретного числительного из набора вариантов
def compute_suffix(value: str, variants: list):
	n = int(value.strip()[-1])
	if (n == 0) or (n >= 5):
		suffix = variants[0]
	elif (n == 1):
		suffix = variants[1]
		if len(value) >= 2:
			if value.strip()[-2] == '1':
				suffix = variants[2]
	else:
		suffix = variants[2]
	return suffix

		
def get_temperature(core: VACore, phrase: str):
    cmd = "cat /sys/class/thermal/thermal_zone0/temp | awk '{print $1 / 1000}'"
    
    temperature = str(subprocess.check_output(cmd, shell = True))
    temperature = round(float(temperature[2:-3]))
    temperature = str(temperature)
    
    text = 'Моя температура ' + temperature + ' ' + compute_suffix(temperature, ('градусов', 'градус', 'градуса'))
    core.play_voice_assistant_speech(text)
