from telegram.ext import ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests
from telegram_bot.config import *


CINEMA_TYPE, MIN_DURATION, MAX_DURATION, REALEASE_DATE, GENRE, NUMBER_OF_EPISODE = ['' for _ in range(6)]
PERSONAL_REC_1, PERSONAL_REC_2, PERSONAL_REC_3, PERSONAL_REC_4, PERSONAL_REC_5 = range(5)


def personal_recommendation_1(update, contex):
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
    print(ID)

    update.message.reply_text(f'Что ты хочешь посмотреть?', reply_markup=reply_markup)
    return PERSONAL_REC_2


def personal_recommendation_2_film(update, contex):
    query = update.callback_query
    query.answer()
    CINEMA_TYPE = query.data.lower()
    keyboard = [
        [
            InlineKeyboardButton("До 1 часа", callback_data="0 3600"),
            InlineKeyboardButton("1-2 часа", callback_data="3600 7200"),
            InlineKeyboardButton("Больше 2 часов", callback_data="7200 12000"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Какая продолжительность?", reply_markup=reply_markup
    )
    return PERSONAL_REC_3


def personal_recommendation_2_tv_show(update, contex):
    query = update.callback_query
    CINEMA_TYPE = query.data.lower()
    query.answer()

    query.edit_message_text(
        text="Какое максимальное количесвтов серий?")
    return PERSONAL_REC_3

def personal_recommendation_3_tv_show(update, contex):
    NUMBER_OF_EPISODE = update.message.text
    keyboard = [
        [
            InlineKeyboardButton("Драма", callback_data="Drama"),
            InlineKeyboardButton("Комедия", callback_data="Comedy"),
            InlineKeyboardButton("Романтика", callback_data="Romance"),
        ], [
            InlineKeyboardButton("Приключения", callback_data="Adventure"),
            InlineKeyboardButton("Ужасы", callback_data="Horror"),
            InlineKeyboardButton("Романтика", callback_data="Romance")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(f'Супер, в каком жанре ты бы хотел посмотреть?', reply_markup=reply_markup)
    return PERSONAL_REC_4


def personal_recommendation_3_film(update, contex):
    query = update.callback_query
    MIN_DURATION, MAX_DURATION = query.data.split()
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Драма", callback_data="Drama"),
            InlineKeyboardButton("Комедия", callback_data="Comedy"),
            InlineKeyboardButton("Романтика", callback_data="Romance"),
        ], [
            InlineKeyboardButton("Приключения", callback_data="Adventure"),
            InlineKeyboardButton("Ужасы", callback_data="Horror"),
            InlineKeyboardButton("Романтика", callback_data="Romance")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text='Супер, в каком жанре ты бы хотел посмотреть?', reply_markup=reply_markup)
    #update.message.reply_text(f'Супер, в каком жанре ты бы хотел посмотреть?', reply_markup=reply_markup)
    return PERSONAL_REC_4


def personal_recommendation_4(update, contex):
    query = update.callback_query
    GENRE = query.data
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("Старое", callback_data='old'),
            InlineKeyboardButton("Новое", callback_data="new"),
            InlineKeyboardButton("/skip", callback_data="skip")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(text='Новое или что-то аутентичное? Можешь пропустить этот момент.',
                            reply_markup=reply_markup)
    return PERSONAL_REC_5


def personal_recommendation_5(update, contex):
    global CINEMA_TYPE, MIN_DURATION, MAX_DURATION, REALEASE_DATE, GENRE, NUMBER_OF_EPISODE
    query = update.callback_query
    query.answer()
    if query.data != 'skip':
        REALEASE_DATE = query.data
    else:
        REALEASE_DATE = "not specified"
    response = requests.get('http://127.0.0.1:5000/api/testing', json={"net_id": ID,
                                                                        "net": NET,
                                                                        "command": "personal recommend",
                                                                        "argument": {
                                                                            "cinema_type": CINEMA_TYPE,
                                                                            "min duration": MIN_DURATION,
                                                                            "max duration": MAX_DURATION,
                                                                            "release date": REALEASE_DATE,
                                                                            "genre": GENRE
                                                                        }
                                                                        }
                            )
    json_response = response.json()
    print(json_response)
    query.edit_message_text(text=json_response["film_info"]["film_name"])

    CINEMA_TYPE, MIN_DURATION, MAX_DURATION, REALEASE_DATE, GENRE, NUMBER_OF_EPISODE = ['' for _ in range(6)]
    return ConversationHandler.END


