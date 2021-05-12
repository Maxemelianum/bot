from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook

TOKEN = '1746524181:AAHeKnVxSpivr5tW38bbCDAmVNLy6HbtPSY'


def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    start_help = CommandHandler('help', do_help)
    start_handler = CommandHandler('start', do_start)
    search_handler = CommandHandler('search', do_search)
    change_handler = MessageHandler(Filters.text, do_change)
    some_handler =  MessageHandler(Filters.text, do_some)
    echo = MessageHandler(Filters.all, do_echo)

    dispather.add_handler(search_handler)
    dispather.add_handler(start_help)
    dispather.add_handler(start_handler)
    dispather.add_handler(change_handler)
    dispather.add_handler(some_handler)
    dispather.add_handler(echo)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text('ЧаВо?')


def do_start(update, context):
    update.message.reply_text('Привет! Ты здесь в первый раз?'
                              '\nВоспользуйся командой /help чтобы понять то тут происходит.')


def do_help(update, context):
    keyboard = [['Поиск Items'], ['Список недавно просмотренных Items'], ['Отслеживание стоимости Items'],
                ['Список ваших Items']]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Это раздел HELP, который поможет вам при работе с ботом.', reply_markup=reply_markup)


def do_some(update: Update, context):
    text = update.message.text

    if text == 'Поиск Items':
        update.message.reply_text('', reply_markup=ReplyKeyboardRemove())
    elif text == 'Список недавно просмотренных Items':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Отслеживание стоимости Items':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Список ваших Items':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('чаво', reply_markup=ReplyKeyboardRemove())


def do_search(update, context):
    keyboard = [['Knifes'], ['Gloves'], ['Rifles'],
                ['Pistols'], ['Heavy Guns'], ['Submachine gun']]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('Выбирите вид оружия.', reply_markup=reply_markup)


def do_change(update: Update, context):
    text = update.message.text

    if text == 'Knifes':
        keyboard = [['Bowie knife'], ['Falchion knife'], ['Bayonet knife'],
                    ['Butterfly knife'], ['Shadow daggers'], ['Flip knife']]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('Выбирите вид оружия.', reply_markup=reply_markup)
    elif text == 'Gloves':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Rifles':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Pistols':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Heavy Guns':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Submachine gun':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('чаво', reply_markup=ReplyKeyboardRemove())




main()