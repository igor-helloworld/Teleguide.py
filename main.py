import telebot
from telebot import types # для указание типов
import config

bot = telebot.TeleBot(config.token) # токен лежит в файле config.py

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("CSS docs", url='https://developer.mozilla.org/en-US/docs/Web/CSS')
    markup.add(button1)
    button2 = types.InlineKeyboardButton("HTML docs", url='https://developer.mozilla.org/en-US/docs/Web/HTML')
    markup.add(button2)
    bot.send_message(message.chat.id, "Привет, {0.first_name}! Нажми на кнопку и перейди на сайт :)".format(message.from_user), reply_markup=markup)
bot.polling(none_stop=True)