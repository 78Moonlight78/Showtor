from telegram.ext import ConversationHandler

PERSONAL_REC_1, PERSONAL_REC_2, PERSONAL_REC_3, PERSONAL_REC_4, PERSONAL_REC_5 = range(5)

def personal_recommendation_1(update, contex):
    update.message.reply_text(f'Что ты хочешь посмотреть?( Фильм, сериал, мультфильм или аниме). Помни, что если не '
                              f'знаешь однозначного ответа на вопрос, то просто напиши /skip.')
    return PERSONAL_REC_2


def personal_recommendation_2(update, contex):
    if 'фильм' in update.message.text.lower():
        update.message.reply_text(f'Какая продолжительность? (1-2 час, до 1 часа...)')
        return PERSONAL_REC_3
    else:
        update.message.reply_text(f'Какое максимальное количество серий?')
        return PERSONAL_REC_3

def personal_recommendation_3(update, contex):
    update.message.reply_text(f'Супер, в каком жанре ты бы хотел посмотреть?')
    return PERSONAL_REC_4

def personal_recommendation_4(update, contex):
    update.message.reply_text(f'Новое или что-то аутентичное?')
    return PERSONAL_REC_5

def personal_recommendation_5(update, contex):
    #Добавить вывод на основе всех вопросов
    return ConversationHandler.END


