import telebot

token = ""

# подключаемся к телеграму
bot = telebot.TeleBot(token=token)

@bot.message_handler(commands=['start', 'help'])
def help(message):
    user = message.chat.id
    bot.send_message(user, "Это бот попугай, просто напиши и я повторю!")

# content_types=['text'] - сработает, если нам прислали текстовое сообщение
@bot.message_handler(content_types=['text'])
def echo(message):
    # message - входящее сообщение
    # message.text - это его текст
    # message.chat.id - это номер его автора
    text = message.text
    user = message.chat.id

    #отправляем картинку с попугаем
    bot.send_photo(user, "https://i.ytimg.com/vi/R-RbmqzRC9c/maxresdefault.jpg")

    #отправляем сообщение тому же пользователю с тем же текстом
    bot.send_message(user, text)

# поллинг - вечный цикл с обновлением входящих сообщений
bot.polling(none_stop=True)