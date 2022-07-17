# Информация о системе
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

import subprocess

from vacore import VACore


def start(core: VACore):
    manifest = {
        "name": "Информация о системе",
        "version": "1.0",
        "require_online": False,

        "commands": {
            "статистика|о системе|ресурсы|инфо":  get_system_info,
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

def get_values_from(data: str):
    tmp = data.split('/')
    first = tmp[0].replace("b'"," ")
    tmp = tmp[1].replace("%", "").split(" ")
    second = tmp[0]
    third = tmp[1]
    return (first, second, third)
    
		
def get_system_info(core: VACore, phrase: str):
    cmd = "ip route get 1.2.3.4 | awk '{print $7}'"
    IP = subprocess.check_output(cmd, shell = True)
    cmd = "top -bn1 | grep load | awk '{printf \"%.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"%s/%s %.2f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | awk '$NF==\"/\"{printf \"%d/%d %s\", $3,$2,$5}'"
    Disk = subprocess.check_output(cmd, shell = True)
    
    text = "АйПи адресс: " + str(IP[0:-2]).replace(".", " точка ").replace("b'", " ") + " !"
    core.play_voice_assistant_speech(text)
    
    text = "Загрузка процессора " + str(CPU).replace("b'", " ") + " !"
    core.play_voice_assistant_speech(text)
    
    mem = get_values_from(str(MemUsage))
    text = "Свободно оперативной памяти {0} из {1} {2}".format(mem[0], mem[1], compute_suffix(mem[1], ["мегабайтов", "мегабайт", "мегабайта"]))
    percent = int(round(float(mem[2].replace("'", ""))))
    text = text + "Что составляет {0} {1} от доступного объема памяти".format(percent, compute_suffix(str(percent), ["процентов", "процент", "процента"]))
    core.play_voice_assistant_speech(text)

    dsk = get_values_from(str(Disk))
    text = "Свободно на носителе {0} из {1} {2}".format(dsk[0], dsk[1], compute_suffix(mem[1], ["гигабайтов", "гигабайт", "гигабайта"]))
    percent = int(round(float(dsk[2].replace("'", ""))))
    text = text + "Что составляет {0} {1} от доступного объема памяти".format(percent, compute_suffix(str(percent), ["процентов", "процент", "процента"]))
    core.play_voice_assistant_speech(text)
