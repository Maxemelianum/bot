from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook

TOKEN = '1746524181:AAHeKnVxSpivr5tW38bbCDAmVNLy6HbtPSY'


def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher
    start_handler = CommandHandler('start', do_start)
    echo = MessageHandler(Filters.all, do_echo)

    dispather.add_handler(start_handler)
    dispather.add_handler(echo)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text('ЧаВо?')


def do_start(update, context):
    update.message.reply_text('Привет!')


main()