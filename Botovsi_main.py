from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
import random


TOKEN = '1591047164:AAGPm_L7jDwhNds_vMlEiCfiw0b6xY1s5zU'


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
    '/start - запуск бота\n/user - посмотреть инфо о себе\n/stop - остановить бота\nНо тебе уже ничего не поможет(',
    'Ты жалок! Ты просишь помщи у бота!\n/start - запуск бота\n/user - посмотреть инфо о себе\n/stop - остановить бота',
    'Сам разбирайся кожанный )'
]
stoping = [
    'Ты уверен?',
    'Иди поспи.',
    'Кожанный мешок хочет остановить бота. Хорошая попытка.'

]
stick = [
    'Вот твое фото',
    'Фоточка тобi на',
    'живи с этим'
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
    some = MessageHandler(Filters.text, do_some)
    sticker = CommandHandler('sticker', do_text)

    dispather.add_handler(start_handler)
    dispather.add_handler(handler)
    dispather.add_handler(some)
    dispather.add_handler(stop_handler)
    dispather.add_handler(sticker)
    dispather.add_handler(name)
    dispather.add_handler(handlerbull)

    updater.start_polling()
    updater.idle()


def do_echo(update, context):
    update.message.reply_text(randomizer.choice(what))


def do_start(update, context):

    update.message.reply_text(randomizer.choice(hi)
)


def do_bulling(update, context):
    keyboard = [['1', '2', '3'],
                ['4', '5', '6']]
    update.message.reply_text(randomizer.choice(helper),
    reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True))


def do_stop(update, context):
    update.message.reply_text(randomizer.choice(stoping))


def do_user(update: Update, context):
    user_id = update.message.from_user.id
    name = update.message.from_user.name
    update.message.reply_text(text=f'Твой disgusting name:{name}\nТвой disgusting id:{user_id}')


def do_text(update, context):
        img = 'https://imbt.ga/dBmlYLNaCQ'
        update.message.reply_text(randomizer.choice(stick))
        update.message.reply_text(f'{img}')


def do_some(update: Update, context):
    text = update.message.text
    if text == '1':
        update.message.reply_text('Это 1', reply_markup=ReplyKeyboardRemove())
    elif text == '2':
        update.message.reply_text('Это 2', reply_markup=ReplyKeyboardRemove())
    elif text == '3':
        update.message.reply_text('Это 3', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text(randomizer.choice(what), reply_markup=ReplyKeyboardRemove())


main()