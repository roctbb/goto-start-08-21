import telebot
import random

token = ""
bot = telebot.TeleBot(token=token)
stickers = []

@bot.message_handler(content_types=['sticker'])
def echo(message):
    user = message.chat.id
    sticker = message.sticker.file_id

    stickers.append(sticker)

    bot.send_sticker(user, random.choice(stickers))

bot.polling(none_stop=True)