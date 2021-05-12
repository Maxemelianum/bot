from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook

TOKEN = '1746524181:AAHeKnVxSpivr5tW38bbCDAmVNLy6HbtPSY'


def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    start_help = CommandHandler('help', do_help)
    start_handler = CommandHandler('start', do_start)
    some_handler =  MessageHandler(Filters.text, do_some)
    echo = MessageHandler(Filters.all, do_echo)

    dispather.add_handler(start_help)
    dispather.add_handler(start_handler)
    dispather.add_handler(some_handler)
    dispather.add_handler(echo)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text('ЧаВо?')


def do_start(update, context):
    update.message.reply_text('Привет!')


def do_help(update, context):
    keyboard = [['Поиск Items'], ['Список недавно просмотренных Items'], ['Отслеживание стоимости Items'],
                ['Список ваших Items']]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Это раздел HELP, который поможет вам при работе с ботом.', reply_markup=reply_markup)


def do_some(update: Update, context):
    text = update.message.text

    if text == 'Поиск Items':
        update.message.reply_text('Поиск Items в Steam'
                                  '\n1.Для старта введите команду /search .'
                                  '\n2.Выберите тип предмета (AK-47, P90, FAMAS, Desert Eagle и т.д.).'
                                  '\n3.Выберите свойство предмета (★, StatTrak, Souvenir, Обычн).'
                                  '\n4.Выберите скин.'
                                  '\n5.Вам будет выдана ссылка с лотами этого скина в Steam.'
                                  '\nИскомого предмета может не быть на ТП, либо вы могли некоректно ввести данные.'
                                  '\nПопробуйте ввести данные еще раз.', reply_markup=ReplyKeyboardRemove())
    elif text == 'Список недавно просмотренных Items':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Отслеживание стоимости Items':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Список ваших Items':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('чаво', reply_markup=ReplyKeyboardRemove())


main()