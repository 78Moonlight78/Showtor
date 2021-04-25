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


