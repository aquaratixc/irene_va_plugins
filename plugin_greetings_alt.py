# Альтернативный модуль приветствий
# author: Oleg Bakharev (inspired by Vladislav Janvarev)

from datetime import datetime
import random

from vacore import VACore

# стартовая процедура
def start(core: VACore):
    manifest = { 
        'name': 'Альтернативный модуль приветствий/прощаний',
        'version': '1.0', 
        'require_online': False, 

        'commands': { 
            'привет|здравствуй|доброго времени суток': general_greetings,
            'пока|прощай|до скорой встречи|до свидания': general_goodbyes,
            'доброе утро|добрый день|добрый вечер|доброй ночи': daytime_greetings,
            'спокойной ночи|сладких снов': goodnights
        }
    }
    return manifest

# общие фразы приветствия
def general_greetings(core: VACore, phrase: str):
	variants = [
		'И я рада тебя видеть!',
		'Здравствуйте!',
		'И вам не хворать!',
		'Какая приятная встреча!',
		'И тебе привет!',
		'Салют!',
		'И снова здравствуйте!',
		'Приветствую'
	]
	core.play_voice_assistant_speech(variants[random.randint(0, len(variants) - 1)])
	

# общие фразы прощания	
def general_goodbyes(core: VACore, phrase: str):
	variants = [
		'До свидания!',
		'До встречи!',
		'Всего доброго!',
		'Всего наилучшего!',
		'До новых встреч!',
		'Прощайте!'
	]
	core.play_voice_assistant_speech(variants[random.randint(0, len(variants) - 1)])

# фразы приветствия в зависмости от времени суток	
def daytime_greetings(core: VACore, phrase: str):
	hour = datetime.now().hour
	
	if (hour >= 0) and (hour < 6):
		text = 'Доброй ночи!'
	elif (hour >= 6) and (hour < 12):
		text = 'Доброе утро!'
	elif (hour >= 12) and (hour < 18):
		text = 'Добрый день!'
	else:
		text = 'Добрый вечер!'
	core.play_voice_assistant_speech(text)
	

# пожелания на ночь
def goodnights(core: VACore, phrase: str):
	core.play_voice_assistant_speech('Спокойной ночи! Сладких снов!')
