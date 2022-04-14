import telebot
import config
import random

a = 0
count = 0

bot = telebot.TeleBot(config.telegram_token)

@bot.message_handler(commands=['start'])
def start(message):
    print(message)
    bot.send_message(message.chat.id, 'Hi there')

@bot.message_handler(commands=['propose1'])
def propose1(message):
    print(message)
    global a
    a = random.randint(0, 100)
    bot.send_message(message.chat.id, 'guess what number')

@bot.message_handler(content_types=['text'])
def guess(message):
    print(message)
    global count
    if count == 4:
        bot.send_message(message.chat.id, 'you lost')
    elif int(message.text) == a and count != 13:
        bot.send_message(message.chat.id, 'you are right')
    else:
        bot.send_message(message.chat.id, 'try again')
        count += 1

bot.polling(none_stop= True)

