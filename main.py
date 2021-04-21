# Импортируем необходимые классы.
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackContext,
)
from config import *
from elemantary_servey import *


def cancel(update, contex):
    update.message.reply_text(
        'Хорошо, ты в любой момент можешь вернуться к этому пункту, написав "Заполнить". Чтобы ознакомиться с полным '
        'списком моих возможностей нажми /setings'
    )
    return ConversationHandler.END

def start(update, context):
    update.message.reply_text(f'Привет, {update.message.chat.first_name}. Я могу помочь тебе в кино мире. Напиши '
                              f'названия того, что ты смотрел, это поможет мне лучше узнать тебя, это займет'
                              f' немного времени. Можешь пропустить этот этап, написав /cancle. Ты готов?'
    )
    return ELEM_1


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)

    conv_handler = ConversationHandler(
        entry_points=[start_handler],
        states={ELEM_1: [MessageHandler(Filters.text, elementary_survey_1)],
                ELEM_2: [MessageHandler(Filters.text, elementary_survey_2)],
                ELEM_3: [MessageHandler(Filters.text, elementary_survey_3)],
                ELEM_4: [MessageHandler(Filters.text, elementary_survey_4)],
                ELEM_5: [MessageHandler(Filters.text, elementary_survey_5)],
                ELEM_6: [MessageHandler(Filters.text, elementary_survey_6)]
        },
    fallbacks=[CommandHandler('cancle', cancel)],
    )
    dp.add_handler(conv_handler)
    updater.start_polling()


    updater.idle()

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()