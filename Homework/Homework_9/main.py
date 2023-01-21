import sqlite3
from telegram import Update, Bot
from random import randint
from token_1 import TOKEN
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters


bot_token = TOKEN
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher
conn = sqlite3.connect('phonebook.db', check_same_thread=False)
cursor = conn.cursor()


def start(update, context):
    context.bot.send_message(
        update.effective_chat.id, 'Привет! Я - телефонный справочник.\nСписок команд:\n/show_all - показать всех\n/find - Найти контакт\n/add - Добавить контакт\n/delete - удалить контакт\n/exit - выход')


def exit(update, context):
    context.bot.send_message(update.effective_chat.id, 'До новых встреч!')


def find(update, context):
    context.bot.send_message(update.effective_chat.id, 'Введите фамилию.')
    return 1


def stop(update, context):
    update.message.reply_text("Всего доброго!")
    return ConversationHandler.END


def search(update, context):
    surname = update.message.text
    cursor.execute(f"SELECT * FROM phonebook WHERE surname like '%{surname}%'")
    results = cursor.fetchall()
    print(results)
    update.message.reply_text(
        f"Контакт {results}\nВведите новую фамилию для поиска\nили введите /start для возврата в главное меню")


def show_all(update, context):
    cursor.execute("SELECT * FROM phonebook")
    results = cursor.fetchall()
    print(results)
    update.message.reply_text(
        f"Список абонентов: {results}\nвведите /start для возврата в главное меню")


def add(update, context):
    surname = 'Степанов'
    name = 'Антон'
    number = 777
    cursor.execute(
        f"INSERT INTO phonebook (surname, name, number)"
        f"VALUES ('{surname}', '{name}', {number})")
    conn.commit()


def delete(update, context):
    context.bot.send_message(update.effective_chat.id,
                             'Введите ID для удаления')
    id = 6
    cursor.execute(f"DELETE FROM phonebook WHERE id={id}")
    conn.commit()


find_handler = ConversationHandler(
    entry_points=[CommandHandler('find', find)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, search)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

show_handler = ConversationHandler(
    entry_points=[CommandHandler('show_all', show_all)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, show_all)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

add_handler = ConversationHandler(
    entry_points=[CommandHandler('add', add)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, add)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

delete_handler = ConversationHandler(
    entry_points=[CommandHandler('delete', delete)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, delete)],
    },
    fallbacks=[CommandHandler('stop', stop)]
)

start_handler = CommandHandler('start', start)
exit_handler = CommandHandler('exit', exit)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(exit_handler)
dispatcher.add_handler(find_handler)
dispatcher.add_handler(show_handler)
dispatcher.add_handler(add_handler)
dispatcher.add_handler(delete_handler)
updater.start_polling()
updater.idle()


conn.commit()
conn.close()
