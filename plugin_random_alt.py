# Случайный выбор
# author: Oleg Bakharev

import random
from vacore import VACore

# стартовая процедура
def start(core: VACore):
    manifest = { 
        'name': 'Случайный выбор', 
        'version': '1.1',
        'require_online': False, 

        'commands': {
            'подбрось монетку|подбрось монету|брось монету|брось монетку|кинь монету|кинь монетку|монетка|орёл или решка' : play_coin,
            'подбрось кубик|брось кубик|брось кость|кинь кубик|кубик' : play_dice,
            'подбрось кости|брось кости|кинь кости' : play_dices,
            'случайное число|число' : play_number,
            }
    }
    return manifest

def play_coin(core: VACore, phrase: str):
    variants = [
        'выпал орел',
        'выпала решка'
    ]
    text = 'На монетке ' + variants[random.randint(0, len(variants) - 1)]
    core.play_voice_assistant_speech(text)

def play_dice(core: VACore, phrase: str):
    variants = random.randint(1, 6)
    text = 'На кубике выпало число ' + str(variants)
    core.play_voice_assistant_speech(text)

def play_dices(core: VACore, phrase: str):
    variants = random.randint(1, 12)
    text = 'На костях выпало число ' + str(variants)
    core.play_voice_assistant_speech(text)


def play_number(core: VACore, phrase: str):
    variants = random.randint(1, 100)
    text = 'Выпало число ' + str(variants)
    core.play_voice_assistant_speech(text)
