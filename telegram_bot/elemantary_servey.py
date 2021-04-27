from telegram.ext import ConversationHandler
import requests
from telegram_bot.config import *


ELEM_1, ELEM_2, ELEM_3,ELEM_4, ELEM_5, ELEM_6= range(6)

def elementary_survey_1(update, context):
    if update.message.text == '/start':
        update.message.reply_text('Прости, но повернуть время назад мы не можем, но мы можем идти вперед!')
    else:
         update.message.reply_text(f'Отлично, перечисли, через  ТОЧКУ(я просто еще маленький, чтобы воспринимать '
                                   f'информацию как-то по другому), фильм или мультфильм, который ты смотрел и он тебе'
                                   f' понравились.(Ты в любой момент можешь пропуститить любой пункт, используя /next)')

    return ELEM_2

def spong_bob_1(update, context):
    if update.message.text == '/start':
        update.message.reply_text('Прости, но повернуть время назад мы не можем, но мы можем идти вперед!')
    else:
        update.message.reply_text(f'ВЫ ГОТОВЫ, ДЕТИ?')
    return ELEM_1

def spong_bob_2(update, context):
    update.message.reply_text(f'Я ВАС НЕ СЛЫШУ!')
    return ELEM_1

def spong_bob_3(update, context):
    update.message.reply_text(f'Отлично, перечисли через ТОЧКУ(я просто еще маленький, чтобы воспринимать '
                              f'информацию как-то по другому) фильм или мультфильм, которые ты смотрел и он тебе'
                              f' понравились.(Ты в любой момент можешь пропуститить любой пункт, используя /next)')
    return ELEM_2

def elementary_survey_2(update, context):
    films = update.message.text.split('.')
    response = requests.put('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                       "net":NET,
                                                                       "command": "put film",
                                                                       "argument": {
                                                                           "cinemas": films,
                                                                           "estimation": "like"
                                                                       }
                                                                       }
                            )

    update.message.reply_text(f'Теперь напиши, какие фильмы или мультфильмы тебе не понравились.')
    return ELEM_3


def elementary_survey_3(update, context):
    films = update.message.text.split('.')
    response = requests.put('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                       "net": NET,
                                                                       "command": "put film",
                                                                       "argument": {
                                                                           "cinemas": films,
                                                                           "estimation": "dislike"
                                                                       }
                                                                       }
                            )
    update.message.reply_text(f'Отлично, с фильмами закончили. Теперь приступим к сериалам. Какие сериалы или'
                              f' мультсериалы, которые ты смотрел, тебе понравились?ПОМНИ, что перечислять нужно '
                              f'через точку')
    return ELEM_4


def elementary_survey_4(update, context):
    films = update.message.text.split('.')
    response = requests.put('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                       "net": NET,
                                                                       "command": "put film",
                                                                       "argument": {
                                                                           "cinemas": films,
                                                                           "estimation": "like"
                                                                       }
                                                                       }
                            )
    update.message.reply_text('А какие не понравились?Также через ТОЧКУ')
    return ELEM_5


def elementary_survey_5(update, context):
    films = update.message.text.split('.')
    response = requests.put('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                       "net": NET,
                                                                       "command": "put film",
                                                                       "argument": {
                                                                           "cinemas": films,
                                                                           "estimation": "dislike"
                                                                       }
                                                                       }
                            )
    update.message.reply_text('Может ты смотрел аниме? Если да, то напиши, что тебе больше всего понравилось?')
    return ELEM_6


def elementary_survey_6(update, context):
    update.message.reply_text('Мы почти на финише, а какие аниме тебе не понравились?')
    films = update.message.text.split('.')
    response = requests.put('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                       "net": NET,
                                                                       "command": "put film",
                                                                       "argument": {
                                                                           "cinemas": films,
                                                                           "estimation": "dislike"
                                                                       }
                                                                       }
                            )
    return ConversationHandler.END


def cancel(update, contex):
    update.message.reply_text(
        'У тебя отличные вкусы. Чтобы узнать мои возможности напиши /settings')
    return ConversationHandler.END

