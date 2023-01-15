# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


# async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     await update.message.reply_text(f'Hello {update.effective_user.first_name}')


# app = ApplicationBuilder().token("5886666069:AAEL2xLeMSQTBLm5vXSvTyMjqhMUZvm1cZ8").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()








import matplotlib.pyplot as plt
import numpy as np

list = [1,2,3,5,1,5]
plt.plot(list)

plt.show()



# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))



# from progress.bar import Bar
# import time

# bar = Bar('Processing', max=20)
# for i in range(20):
#     time.sleep(0.5)
#     # Do some work
#     bar.next()
# bar.finish()