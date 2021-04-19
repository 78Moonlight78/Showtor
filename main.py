import telebot
import config
from data import db_session


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Привет, {message.from_user.first_name}. Я буду твоим наставником в мире кино. Напиши'
                          f' названия того, что ты смотрел, это поможет мне лучше узнать тебя, это займет немного времени. '
                          f'Ты можешь пропустить этот этап /skip')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == '/skip':
        bot.send_message(message.from_user.id, f'{message}')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')


bot.polling(none_stop=True)