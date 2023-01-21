from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import *
from token_1 import TOKEN
import emoji
import random

bot_token = TOKEN
reply_keyboard = [['/rules', '/game'],
                  ['/exit']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

candies = 0


def start(update, context):
    update.message.reply_text(
        f"Привет, давай сыграем в игру на {emoji.emojize(':candy:')}\n/rules - Правила игры\n/game - Начать игру\n/exit - Выйти из игры",
        reply_markup=markup)


def game(update, context):
    update.message.reply_text(
        f"Введите количество {emoji.emojize(':candy:')} для игры",
        reply_markup=ReplyKeyboardRemove())
    return 1


def rules(update, context):
    update.message.reply_text(
        f"Игроки берут конфеты {emoji.emojize(':candy:')} по очереди. За один ход можно взять не более 28 конфет {emoji.emojize(':candy:')}. Выигрывает тот, кто возьмёт последнюю конфету{emoji.emojize(':candy:')}")


def exit(update, context):
    update.message.reply_text(
        "До новых встреч!", reply_markup=ReplyKeyboardRemove())


def stop(update, context):
    update.message.reply_text(
        "Всего доброго!", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


def init_game(update, context):
    global candies
    try:
        candies = int(update.message.text)
        update.message.reply_text(
            f"В игре {candies} конфет{emoji.emojize(':candy:')}")
        update.message.reply_text(
            f"Сколько конфет{emoji.emojize(':candy:')} возьмёте?")
        return 2
    except:
        update.message.reply_text(f"Введите число!")


def next_step(update, context):
    global candies
    candies1 = int(update.message.text)
    if candies1 > 28 or candies1 < 1:
        update.message.reply_text(
            'Введите число из указанного диапазопа [1; 28]')
        return 2
    candies -= candies1
    if candies >= 29:
        update.message.reply_text(
            f"В игре осталось {candies} конфет{emoji.emojize(':candy:')}. Ход бота")
        candies2 = candies % 29
        if candies2 == 0:
            candies2 = random.randint(1, 28)
        update.message.reply_text(
            f"Бот взял {candies2} конфет{emoji.emojize(':candy:')}. Твоя очередь")
        candies -= candies2
        if candies >= 29:
            update.message.reply_text(
                f"В игре {candies} конфет{emoji.emojize(':candy:')}")
            update.message.reply_text(
                f"Сколько конфет{emoji.emojize(':candy:')} возьмёте?")
            return 2
        else:
            update.message.reply_text(
                f"Поздравляю с победой {emoji.emojize(':tada:')}", reply_markup=markup)
    else:
        update.message.reply_text(
            f"Ты проиграл {emoji.emojize(':cry:')}", reply_markup=markup)
    return ConversationHandler.END


game_handler = ConversationHandler(
    entry_points=[CommandHandler('game', game)],
    states={
        1: [MessageHandler(Filters.text & ~Filters.command, init_game)],
        2: [MessageHandler(Filters.text & ~Filters.command, next_step)]
    },
    fallbacks=[CommandHandler('stop', stop)]
)


def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(game_handler)
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(CommandHandler("stop", stop))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
