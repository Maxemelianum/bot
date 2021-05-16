from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler
from openpyxl import load_workbook

TOKEN = '1746524181:AAHeKnVxSpivr5tW38bbCDAmVNLy6HbtPSY'
book = load_workbook("New Microsoft Excel Worksheet.xlsx")
sheet_1 = book['Лист1']
print(sheet_1["C2"].value
      )
steam = sheet_1["A2"].value

new = sheet_1["E2"].value
minimal = sheet_1["E3"].value
field = sheet_1["E4"].value
well = sheet_1["E5"].value
bad = sheet_1["E6"].value

def main():
    updater = Updater(token=TOKEN)  # объект, который ловит сообщения от Telegrama

    dispather = updater.dispatcher

    start_help = CommandHandler('help', do_help)
    start_handler = CommandHandler('start', do_start)
    search_handler = CommandHandler('search', do_search)
    change_handler = MessageHandler(Filters.text, do_change)
    some_handler = MessageHandler(Filters.text, do_some)
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
                ['Pistols'], ['Heavy Guns'], ['Submachine guns']]
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
        update.message.reply_text('Выбирите оружие', reply_markup=ReplyKeyboardRemove())

    elif text == 'Pistols':
        keyboard = [[sheet_1["C2"].value], [sheet_1["C3"].value], [sheet_1["C4"].value],
                    [sheet_1["C5"].value], [sheet_1["C6"].value], [sheet_1["C7"].value]]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('Выбирите пистолет', reply_markup=reply_markup)

    elif text == 'P2000':
        keyboard = [[sheet_1["D2"].value], [sheet_1["D3"].value], [sheet_1["D9"].value]]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('Выбирите скин', reply_markup=reply_markup)
    elif text == 'Ocean%20Foam':
        keyboard = [[sheet_1["E2"].value], [sheet_1["E3"].value], [sheet_1["E4"].value], [sheet_1["E5"].value], [sheet_1["E6"].value]]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('Выбирите качество', reply_markup=reply_markup)
    elif text == f'{new}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D2"].value}%20{new}')
    elif text == f'{minimal}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D2"].value}%20{minimal}')
    elif text == f'{field}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D2"].value}%20{field}')
    elif text == f'{well}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D2"].value}%20{well}')
    elif text == f'{bad}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D2"].value}%20{bad}')

    elif text == 'Pathfinder':
        keyboard = [[f'{sheet_1["E2"].value}200'], [sheet_1["E3"].value], [sheet_1["E4"].value], [sheet_1["E5"].value], [sheet_1["E6"].value]]
        reply_markup = ReplyKeyboardMarkup(keyboard=keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text('Выбирите качество', reply_markup=reply_markup)
    elif text == f'{sheet_1["E2"].value}200':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D9"].value}%20{sheet_1["E2"].value}')
    elif text == f'{minimal}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D9"].value}%20{minimal}')
    elif text == f'{field}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D9"].value}%20{field}')
    elif text == f'{well}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D9"].value}%20{well}')
    elif text == f'{bad}':
        update.message.reply_text(f'{steam}{sheet_1["C2"].value}%20%7C%20{sheet_1["D9"].value}%20{bad}')


    elif text == 'Heavy Guns':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    elif text == 'Submachine gun':
        update.message.reply_text('Скоро...', reply_markup=ReplyKeyboardRemove())
    else:
        update.message.reply_text('Видимо вы некоректно ввели данные.', reply_markup=ReplyKeyboardRemove())






main()