from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler
from random import randint
from token_1 import TOKEN
import sqlite3

bot_token = TOKEN
bot = Bot(bot_token)
updater = Updater(bot_token, use_context=True)
dispatcher = updater.dispatcher

conn = sqlite3.connect('phonebook.db')
cursor = conn.cursor()

# поиск записи
# surname = 'Иванов'
# cursor.execute(f"select * from phonebook where surname like '%{surname}%'")
# results = cursor.fetchall()
# print(results)

# # добавить студента
# name = 'Степан'
# surname = 'Степанов'
# phone = 45648
# description = 'Инженер'
# cursor.execute(
#     f"insert into phonebook (name, surname, phone, description) "
#     f"values ('{name}', '{surname}', {phone}, '{description}')")
# conn.commit()

# # удалить студента
# id = 5
# cursor.execute(
#     f"delete from phonebook where id={id}"
# )
# conn.commit()

# # обновить данные о студенте
# id = 3
# cursor.execute(
#     f"update phonebook set name='Юрий' where id={id}"
# )
# conn.commit()
# conn.close()


def start(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        'Привет! Я - бот-справочник.\nСписок команд:\n/show - показать контакты\n/add - добавить новый контакт\n/delete - удалить контакт\n/find - найти контакт'
    )


def show(update, context):
    context.bot.send_message(update.effective_chat.id,
                             cursor.execute("select * from phonebook"),
                             results=cursor.fetchall())
    #  print(results)


# def roll(update, context):
#     context.bot.send_message(update.effective_chat.id, text=str(randint(1, 6)))

start_handler = CommandHandler('start', start)
show_handler = CommandHandler('show', show)
# roll_handler = CommandHandler('roll', roll)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(show_handler)
# dispatcher.add_handler(roll_handler)
updater.start_polling()
updater.idle()