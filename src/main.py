import telebot
import base
from utils import call_llama

bot = telebot.TeleBot(base.TOKEN)
print('bot created')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(chat_id=message.chat.id,
                           text='Hello. Is there something I can help you with or would you like to chat?')


@bot.message_handler(func=lambda message: True)
def handle_user_message(message):
    model = 'llama3.2:1b'
    response = call_llama(model, message.text).get('response')
    bot.send_message(chat_id=message.chat.id, text=response)


if __name__ == '__main__':
    bot.infinity_polling()
