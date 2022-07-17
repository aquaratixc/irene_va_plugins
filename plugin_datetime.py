# Дата и время
# author: Vladislav Janvarev, Oleg Bakharev

from datetime import datetime
import os

from vacore import VACore

# имя модуля
modname = os.path.basename(__file__)[:-3] 

# начальные настройки
def start(core: VACore):
    manifest = { # возвращаем настройки плагина - словарь
        'name': 'Дата и время', # имя
        'version': '1.2', # версия
        'require_online': False, # требует ли онлайн?

        'default_options': {
            'sayNoon': False, # говорить 'полдень' и 'полночь' вместо 12 и 0 часов
            'skipUnits': False,  # не произносить единицы времени ('час', 'минуты')
            'unitsSeparator': ', ',  # сепаратор при озвучивании 10 часов <sep> 10 минут. Варианты: ' и '
            'skipMinutesWhenZero': True, # не озвучивать минуты, если равны 0
        },

        'commands': { 
            'дата|текущая дата': play_date,
            'время|сколько времени|который час|текущее время': play_time,
            'день недели': play_weekday,
        }
    }
    return manifest


def start_with_options(core: VACore, manifest: dict):
    pass


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

# получить текст для описания дня недели
def get_weekday(date):
	weekday_list = ('понедельник','вторник','среда','четверг','пятница','суббота','воскресенье')
	
	weekday = weekday_list[date.weekday()]
	return weekday


# получить текст для описания даты
def get_date(date):
	day_list = ('первое', 'второе', 'третье', 'четвёртое','пятое', 'шестое', 'седьмое', 'восьмое','девятое', 'десятое', 'одиннадцатое', 'двенадцатое','тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое','семнадцатое', 'восемнадцатое', 'девятнадцатое', 'двадцатое','двадцать первое', 'двадцать второе', 'двадцать третье','двадцать четвёртое', 'двадцать пятое', 'двадцать шестое','двадцать седьмое', 'двадцать восьмое', 'двадцать девятое','тридцатое', 'тридцать первое')
	month_list = ('января', 'февраля', 'марта', 'апреля', 'мая', 'июня','июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря')
	
	day = day_list[date.day - 1]
	weekday = get_weekday(date)
	month = month_list[date.month - 1]
	
	return 'Сегодня {0} {1} {2}'.format(weekday, day, month)
	
# произнести дату
def play_date(core: VACore, phrase: str):
    now = datetime.now()
    text = get_date(now)
    
    core.play_voice_assistant_speech(text)
    
# произнести время    
def play_time(core: VACore, phrase: str): 
    options = core.plugin_options(modname)

    if options['skipUnits']:
        units_minutes = ('', '', '')
        units_hours  =  ('', '', '')
    else:
        units_minutes = ('минут', 'минута', 'минуты')
        units_hours =   ('часов', 'час', 'часа')

    now = datetime.now()
    hours = now.hour
    minutes = now.minute

    if options['sayNoon']:
        if (hours == 0) and (minutes == 0):
            text = 'Сейчас ровно полночь'
        elif (hours == 12) and (minutes == 0):
            text = 'Сейчас ровно полдень'
        core.play_voice_assistant_speech(text)
        return

    text = str(hours) + ' ' + compute_suffix(str(hours), units_hours)
    if minutes > 0 or options['skipMinutesWhenZero'] is not True:
        text = 'Сейчас ' + text
        if not options['skipUnits']:
            text += options['unitsSeparator']
        text += str(minutes) + ' ' + compute_suffix(str(minutes), units_minutes)
    else:
        text = 'Сейчас ровно ' + text

    core.play_voice_assistant_speech(text)


# произнести дату
def play_weekday(core: VACore, phrase: str):
    now = datetime.now()
    text = get_weekday(now)
    
    core.play_voice_assistant_speech(text)
