from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters
from random import randint
from token_1 import TOKEN

bot_token = TOKEN
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(
        update.effective_chat.id, 'Привет! Я - бот-калькулятор.\nСписок команд:\n/calc - решить пример\n/convert - перевод кг в г\n/exit - выход')


def exit(update, context):
    context.bot.send_message(update.effective_chat.id, 'До новых встреч!')


def calc(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите выражение.')
    return 1


def convert(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите массу в кг для получения ответа в г')
    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def calculate(update, context):
    primer = update.message.text
    update.message.reply_text(
        f"Ответ: {eval(primer)}\nВведите новый пример для решения\nили введите /stop")


def converter(update, context):
    massa = update.message.text
    update.message.reply_text(
        f"Ответ: {(float(massa)*1000)} грамм\nВведите другую массу\nили введите /stop")


conv_handler = ConversationHandler(
    entry_points=[CommandHandler('calc', calc)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, calculate)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

convert_handler = ConversationHandler(
    entry_points=[CommandHandler('convert', convert)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, converter)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)


start_handler = CommandHandler('start', start)
exit_handler = CommandHandler('exit', exit)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(exit_handler)
dispatcher.add_handler(conv_handler)
dispatcher.add_handler(convert_handler)
updater.start_polling()
updater.idle()
