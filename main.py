from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
)
from telegram_bot.config import *
from telegram_bot.elemantary_servey import *
from telegram_bot.adding_new import *


#стартавая функция
def start(update, context):
    update.message.reply_text(f'Привет, {update.message.chat.first_name}. Я могу помочь тебе в кино мире. Напиши '
                              f'названия того, что ты смотрел, это поможет мне лучше узнать тебя, это займет'
                              f' немного времени. Можешь пропустить этот этап, написав /cancel. Ты готов?'
    )
    return ELEM_1

#Выводит настройки
def settings(update, contex):
    update.message.reply_text(f'Я могу \n'
                              f'1) Дать персональную рекомендацию(/personal)\n'
                              f'2) Мне повезет(/luck)\n'
                              f'3) Просмотренное(/skaned)\n'
                              f'4) Добавить что-то новое(/new)')

#Выводит рандомную рекомендация пользователь
#Подсоеденить
def luck(update, contex):
    update.message.reply_text(f'')


#функция, которая выводит просмотренное
def skaned(update, contex):
    return KIND


#радомная рекомендация мемов
def meme(update, contex):
    update.message.reply_text(f'')


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    start_handler = CommandHandler('start', start)
    settings_handler = CommandHandler('settings', settings)
    lucky_handle = CommandHandler('luck', luck)
    scaned_handle = CommandHandler('skaned', skaned)
    conv_handler_elem = ConversationHandler(
        entry_points=[start_handler],
        states={ELEM_1: [MessageHandler(Filters.regex('^да|Да|$'), elementary_survey_1),
                         MessageHandler(Filters.regex('нет'),spong_bob_1),
                         MessageHandler(Filters.regex('ДА, КАПИТАН'), spong_bob_2),
                         MessageHandler(Filters.regex('ТАК ТОЧНО, КАПИТАН'), spong_bob_3)],
                ELEM_2: [MessageHandler((Filters.text ^ Filters.regex('/cancel')), elementary_survey_2)],
                ELEM_3: [MessageHandler((Filters.text ^ Filters.regex('/cancel')), elementary_survey_3)],
                ELEM_4: [MessageHandler((Filters.text ^ Filters.regex('/cancel')), elementary_survey_4)],
                ELEM_5: [MessageHandler((Filters.text ^ Filters.regex('/cancel')), elementary_survey_5)],
                ELEM_6: [MessageHandler((Filters.text ^ Filters.regex('/cancel')), elementary_survey_6)]
        },
    fallbacks=[CommandHandler('cancel', cancel)],
    )
    conv_handler_new = ConversationHandler(
        entry_points=[scaned_handle],
        states={ KIND: [MessageHandler(Filters.regex('^фильм|сериал|аниме|мультфильм|мультсериал$'), add_new_kind)],
                 NEW_FILM: [MessageHandler(Filters.text, add_new_film)]

        },
    fallbacks=[CommandHandler('cancel', cancel)],
    )

    dp.add_handler(conv_handler_elem)
    dp.add_handler(settings_handler)
    dp.add_handler(lucky_handle)
    dp.add_handler(conv_handler_new)
    dp.add_handler(scaned_handle)
    updater.start_polling()


    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()