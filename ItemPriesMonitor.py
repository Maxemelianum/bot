from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook

TOKEN = '1746524181:AAHeKnVxSpivr5tW38bbCDAmVNLy6HbtPSY'


def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    start_help = CommandHandler('help', do_help)
    start_handler = CommandHandler('start', do_start)
    echo = MessageHandler(Filters.all, do_echo)

    dispather.add_handler(start_help)
    dispather.add_handler(start_handler)
    dispather.add_handler(echo)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text('ЧаВо?')


def do_start(update, context):
    update.message.reply_text('Привет!')


def do_help(update, context):
    keyboard = [['1'], ['1']]
    reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text('jr', reply_markup=reply_markup)


def do_some(update: Update, context):
    text = update.message.text

    if text == 'Нет':
        update.message.reply_text('****** ответ', reply_markup=ReplyKeyboardRemove())
        update.message.reply_sticker('CAACAgIAAxkBAAECEd1gUd5kmaGDSLkdJEidOZwxCp7C_AACGAADoF_dLYLQt9fbwjB_HgQ')
    elif text == 'Да':
        update.message.reply_text('Вы использовали команду /user', reply_markup=ReplyKeyboardRemove())
    elif text == 'Давай не будем':
        update.message.reply_text('Вы использовали команду /stop', reply_markup=ReplyKeyboardRemove())
    elif text == 'Хватит':
        update.message.reply_text('Вы использовали команду /img', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('чаво', reply_markup=ReplyKeyboardRemove())


main()