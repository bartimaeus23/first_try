import telebot
import config
from telebot import types
import requests


bot = telebot.TeleBot(config.telegram_token)



class Storage():
    storage = {}

    @classmethod
    def store(cls, file_name, link):
        Storage.storage[file_name] = link

def get(link):
    try:
        data = requests.get(link)
        return data
    except Exception as e:
        return e

@bot.message_handler(content_types=["document", "video", "audio"])
def handle_files(message):
    document_id = message.document.file_id
    file_info = bot.get_file(document_id)
    print(document_id) # Выводим file_id
    bot.send_message(message.chat.id, message.document.file_name)   # type(message.document.file_name) = str
    file_name = message.document.file_name
    link = f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}'
    Storage.store(file_name, link)
    # print(f'http://api.telegram.org/file/bot{config.telegram_token}/{file_info.file_path}') # Выводим ссылку на файл
    bot.send_message(message.chat.id, document_id) # Отправляем пользователю file_id

@bot.message_handler(content_types=['text'])
def get_file(message):
    link = Storage.storage[message.text]
    get(link)  # doesn't work as expected
    # bot.send_message(message.chat.id, )
    bot.send_message(message.chat.id, link)

bot.polling(none_stop=True)


# don't forget file with token

