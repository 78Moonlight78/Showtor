from telegram.ext import ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup



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
    # Send message with text and appended InlineKeyboard

    update.message.reply_text(f'Что ты хочешь посмотреть?', reply_markup=reply_markup)
    return PERSONAL_REC_2


def personal_recommendation_2_film(update, contex):
    query = update.callback_query
    query.answer()
    keyboard = [
        [
            InlineKeyboardButton("До 1 часа", callback_data="до 1 часа"),
            InlineKeyboardButton("1-2 часа", callback_data="1-2 часа"),
            InlineKeyboardButton("Больше 2 часов", callback_data="больше 2 часов"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    query.edit_message_text(
        text="Какая продолжительность?", reply_markup=reply_markup
    )
    return PERSONAL_REC_3


def personal_recommendation_2_tv_show(update, contex):
    query = update.callback_query
    query.answer()
    query.edit_message_text(
        text="Какое максимальное количесвтов серий?")
    return PERSONAL_REC_3

def personal_recommendation_3_tv_show(update, contex):
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
    update.message.reply_text(f'Новое или что-то аутентичное? Можешь пропустить этот момент /skip')
    return PERSONAL_REC_5


def personal_recommendation_5(update, contex):
    #Добавить вывод на основе всех вопросов
    return ConversationHandler.END


