"""from telegram.ext import ConversationHandler

KIND, NEW_FILM = range(2)

def add_new_kind(update, context):
    update.message.reply_text(f'Классно, что ты просмотрел в этот раз?(Фильм, сериал, аниме, мультфильм или '
                              f'мультсериал)')
    return NEW_FILM

def add_new_film(update, context):
    update.message.reply_text(f'Как называется?')
    return ConversationHandler.END
"""

from telegram.ext import ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_bot.config import *
import requests

NEW_FILM, KIND_FILM, RESULT, IS_LIKE = range(4)
NAME, KIND, LIKE = '', '', ''

def start_new(update, contex):
    update.message.reply_text('Добавим что-то новенькое?')
    return NEW_FILM


def add_new_kind(update, contex):
    global ID
    keyboard = [
        [
            InlineKeyboardButton("Фильм", callback_data="Фильм"),
            InlineKeyboardButton("Сериал", callback_data="Сериал"),
            InlineKeyboardButton('Аниме', callback_data='Аниме')
        ],
        [InlineKeyboardButton("Мультфильм", callback_data="Мультфильм"),
         InlineKeyboardButton('Мультсериал', callback_data='Мультсериал')
         ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    ID = update.message.chat.id

    update.message.reply_text('Классно, что ты просмотрел в этот раз?', reply_markup=reply_markup)
    return KIND_FILM

def add_new_film(update, contex):
    query = update.callback_query
    query.answer()
    KIND = query.data
    query.edit_message_text(text='Как называется?')
    return IS_LIKE


def like_it(update, contex):
    NAME = update.message.text
    keyboard = [
        [
            InlineKeyboardButton("Понравилось", callback_data="Фильм"),
            InlineKeyboardButton("НЕ ПОНРАВИЛОСЬ", callback_data="Сериал"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Тебе понравилось?', reply_markup=reply_markup)
    return RESULT


def result(update, contex):
    query = update.callback_query
    query.answer()
    LIKE = query.data
    response = requests.put('http://127.0.0.1:5000/api/testing', json={"net_id": ID,
                                                                       "net": NET,
                                                                       "command": "put film",
                                                                       "argument": {
                                                                           "cinemas": [NAME, KIND],
                                                                           "estimation": LIKE
                                                                       }
                                                                       }
                            )
    query.edit_message_text(text='Записал')