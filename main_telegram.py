from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
import requests
from telegram_bot.config import *
from telegram_bot.elemantary_servey import *
from telegram_bot.adding_new import *
from API_module.recourses import *
from telegram_bot.personal_rec import *

#стартавая функция
def start(update, context):
    global ID
    ID = update.message.chat.id
    print(ID, update.message)
    response = requests.post('http://127.0.0.1:5000/api/testing', json={"net_id": ID,
                                                                        "net": "Telegram"})
    json_response = response.json()
    if json_response['error'] == 'success':
        update.message.reply_text(f'Привет, {update.message.chat.first_name}. Я могу помочь тебе в кино мире. '
                                  f'Я ознакомся с моими возможностями.')
        update.message.reply_text(f'Я могу... \n'
                                  f'1) Дать персональную рекомендацию(/personal)\n'
                                  f'2) Мне повезет(/luck)\n'
                                  f'3) Просмотренное(/skaned)\n'
                                  f'4) Добавить что-то новое(/new)')
        #return ELEM_1
    else:
        update.message.reply_text('Ты же уже начал, так продолжай!')
        update.message.reply_text(f'Я могу... \n'
                                  f'1) Дать персональную рекомендацию(/personal)\n'
                                  f'2) Мне повезет(/luck)\n'
                                  f'3) Просмотренное(/skaned)\n'
                                  f'4) Добавить что-то новое(/new)')
        return ConversationHandler.END

#Выводит настройки
def settings(update, contex):
    update.message.reply_text(f'Я могу... \n'
                              f'1) Дать персональную рекомендацию(/personal)\n'
                              f'2) Мне повезет(/luck)\n'
                              f'3) Просмотренное(/skaned)\n'
                              f'4) Добавить что-то новое(/new)')

#Выводит рандомную рекомендация пользователь
#Подсоеденить
def luck(update, contex):
    response = requests.get('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                        "net": "Telegram", 'command': 'random film'})
    json_response = response.json()
    update.message.reply_text(f'{json_response["film_info"]["film_name"]}\n'
                              f'{", ".join(json_response["film_info"]["film_genres"])}')

#функция, которая выводит просмотренное
def skaned(update, contex):
    response = requests.get('http://127.0.0.1:5000/api/testing', json={"net_id": update.message.chat.id,
                                                                       "net": NET,
                                                                       "command": "all watched"
                                                                       }
                            )
    json_response = response.json()
    print(json_response)


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
    personal_handler = CommandHandler('personal', personal_recommendation_1)
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



    conv_handler_personal = ConversationHandler(
        entry_points=[personal_handler],
        states={PERSONAL_REC_2: [CallbackQueryHandler(personal_recommendation_2_film, pattern='^Фильм|Мультфильм$'),
                                 CallbackQueryHandler(personal_recommendation_2_tv_show, pattern='^Сериал|Аниме|'
                                                                                                 'Мультсериал$')],
                PERSONAL_REC_3: [CallbackQueryHandler(personal_recommendation_3_film),
                                                MessageHandler(Filters.text ^ Filters.command,
                                                               personal_recommendation_3_tv_show)],
                PERSONAL_REC_4: [CallbackQueryHandler(personal_recommendation_4)],
                PERSONAL_REC_5: [CallbackQueryHandler(personal_recommendation_5)]
               },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    conv_handler_new = ConversationHandler(
        entry_points=[CommandHandler('new', start_new)],
        states={NEW_FILM: [MessageHandler(Filters.text ^ Filters.command, add_new_kind)],
                KIND_FILM:[CallbackQueryHandler(add_new_film)],
                IS_LIKE:[MessageHandler(Filters.text ^ Filters.command, like_it)],
                RESULT:[ CallbackQueryHandler(result)]
                },
        fallbacks=[CommandHandler('cancel', cancel)]

    )

    dp.add_handler(conv_handler_personal)
    #dp.add_handler(conv_handler_elem)
    dp.add_handler(settings_handler)
    dp.add_handler(lucky_handle)
    dp.add_handler(personal_handler)
    dp.add_handler(scaned_handle)
    dp.add_handler(start_handler)
    dp.add_handler(conv_handler_new)
    updater.start_polling()


    updater.idle()


# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()