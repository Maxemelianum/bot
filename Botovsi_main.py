from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import random

TOKEN = '1591047164:AAHZ_9l-rKzWnosUc8nAaj3vtd-xgIN3_MI'

what = [
    'Идиот, я же не понимаю нихрена!',
    'А команды тебе просто так даны?',
    'У тебя IQ как у хлебушка! Используй команды!'
]

hi = [
    'Ну привет кожанный.',
    'Готовь свои нервы.',
    'Удачи, кожанный ублюдок.'
]

helper = [
    'Тебе уже ничего не поможет(',
    'Ты жалок! Ты просишь помщи у бота!',
    'Сам разбирайся кожанный )'
]
stoping = [
    'Ты уверен?',
    'Иди поспи.',
    'NOOOOOOOOOOOOOOOO!'

]

randomizer = random.SystemRandom()


def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    handlerbull = MessageHandler(Filters.all, do_echo)
    handler = CommandHandler('help', do_bulling)
    start_handler = CommandHandler('start', do_start)
    stop_handler = CommandHandler('stop', do_stop)
    name = CommandHandler('user', do_user)

    dispather.add_handler(start_handler)
    dispather.add_handler(handler)
    dispather.add_handler(stop_handler)
    dispather.add_handler(name)
    dispather.add_handler(handlerbull)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text(randomizer.choice(what))


def do_start(update, context):
    update.message.reply_text(randomizer.choice(hi))


def do_bulling(update, context):
    update.message.reply_text(randomizer.choice(helper))


def do_stop(update, context):
    update.message.reply_text(randomizer.choice(stoping))


def do_user(update: Update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.name
    update.message.reply_text(text=f'Твой disgusting name:{name}\nТвой disgusting id:{user_id}')


main()