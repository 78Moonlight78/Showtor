from telegram.ext import ConversationHandler


ELEM_1, ELEM_2, ELEM_3,ELEM_4, ELEM_5, ELEM_6= range(6)

def elementary_survey_1(update, context):
    if update.message.text == '/start':
        update.message.reply_text('Прости, но повернуть время назад мы не можем, но мы можем идти вперед!')
    else:
         update.message.reply_text(f'Отлично, перечисли, через точку, фильмы или мультфильмы, которые ты смотрел и они тебе'
                                   f' понравились.(Ты в любой момент можешь пропуститить любой пункт, используя /next)')
    return ELEM_2

def spong_bob_1(update, context):
    if update.message.text == '/start':
        update.message.reply_text('Прости, но повернуть время назад мы не можем, но мы можем идти вперед!')
    else:
        update.message.reply_text(f'ВЫ ГОТОВЫ, ДЕТИ?')
    return ELEM_1

def spong_bob_2(update, context):
    update.message.reply_text(f'Я ВАС НЕ СЛЫШУ!')
    return ELEM_1

def spong_bob_3(update, context):
    update.message.reply_text(f'Отлично, перечисли, через точку, фильмы или мультфильмы, которые ты смотрел и они тебе'
                              f' понравились.(Ты в любой момент можешь пропуститить любой пункт, используя /next)')
    return ELEM_2

def elementary_survey_2(update, context):
    update.message.reply_text(f'Теперь напиши, какие фильмы или мультфильмы тебе не понравились.')
    return ELEM_3


def elementary_survey_3(update, context):
    update.message.reply_text(f'Отлично, с фильмами закончили. Теперь приступим к сериалам. Какие сериалы или'
                              f' мультсериалы, которые ты смотрел, тебе понравились?')
    return ELEM_4


def elementary_survey_4(update, context):
    update.message.reply_text('А какие не понравились?')
    return ELEM_5


def elementary_survey_5(update, context):
    update.message.reply_text('Может ты смотрел аниме? Если да, то напиши, что тебе больше всего понравилось?')
    return ELEM_6


def elementary_survey_6(update, context):
    update.message.reply_text('Мы почти на финише, а какие аниме тебе не понравились?')
    return ConversationHandler.END


def cancel(update, contex):
    update.message.reply_text(
        'Хорошо, ты в любой момент можешь вернуться к этому пункту, написав "Заполнить". Чтобы ознакомиться с полным '
        'списком моих возможностей нажми /settings'
    )
    return ConversationHandler.END

