import telebot
import config
import openweathermap as weather
from telebot import types

bot = telebot.TeleBot(config.telegram_token)


@bot.message_handler(content_types=['text'])
def get_weather(message):
    print(message)
    print(message.text)
    city = message.text
    bot.send_message(message.chat.id, message.date)
    name, description, temp = weather.get(city)
    bot.send_message(message.chat.id, name)
    bot.send_message(message.chat.id, description)
    bot.send_message(message.chat.id, temp)




bot.polling(none_stop=True)