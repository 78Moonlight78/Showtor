# Импортируем необходимые классы.
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler, ConversationHandler
from config import *


def start(update, context):
    update.message.reply_text(f'Привет, {update.message.chat.first_name}. Я могу помочь тебе в кино мире. Напиши '
                              f'названия того, что ты смотрел, это поможет мне лучше узнать тебя, это займет'
                              f' немного времени. Можешь пропустить этот этап, написав /skip. Ты готов?')


def elementary_survey_1(update, context):
    update.message.reply_text(f'Отлично, перечисли, через точку, фильмы или мультфильмы, которые ты смотрел и они тебе'
                              f' понравились.(Ты в любой момент можешь пропуститить любой пункт, используя /next)')


def elementary_survey_1(update, context):
    update.message.reply_text(f'Теперь напиши, какие фильмы или мультфильмы тебе не понравились.')


def elementary_survey_2(update, context):
    update.message.reply_text(f'Отлично, с фильмами закончили. Теперь приступим к сериалам. Какие сериалы или'
                              f' мультсериалы, которые ты смотрел и они тебе понравились?')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    updater.start_polling()

    # Ждём завершения приложения.
    # (например, получения сигнала SIG_TERM при нажатии клавиш Ctrl+C)
    updater.idle()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()