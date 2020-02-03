import random
import telebot
import requests
from time import time
bot = telebot.TeleBot('989581265:AAFBf3qwuJ7gyqh8QI-KtL062xgLxSJKaaI')
r = str(random.randint(0, 10))
from telebot import types
a = types.ReplyKeyboardMarkup(resize_keyboard=True)
a1 = types.KeyboardButton("включи бойлер")
a2 = types.KeyboardButton("виключи бойлер")
a.add(a1,a2)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(-1001495083425, 'УВАГА!!!УВАГА!!!УВАГА!!!\nВ бота добавилася нова функція якщо ти напишеш\n/russianroulette\nто у тебе є шанс 1 із 10 що ти получиш мут на день пробуй)\nмут - незмога писати повідомлень')
@bot.message_handler(commands=['help'])
def start_message(message):

    bot.send_message(message.chat.id, 'Привіт я бот тімоха мої команди \nпривіт\n бувай\n хто розробник\n на якій мові ти написаний')
@bot.message_handler(commands=['russianroulette'])
def send_text1(message):
    o = str(random.randint(1, 10))
    bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date=time()+120)
    if message.chat.type == 'supergroup':
         if message.chat.title == 'Линуксоиды':
             if o == '1':
                 bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date=time()+86400)
                 bot.send_message(-1001495083425, 'мут на день) твоє число: ' + '1')
             if o != '1':
                 print(o)
                 bot.send_message(-1001495083425, 'ти везунчик тебе випало: ' + o)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.chat.type == 'supergroup':
         if message.chat.title == 'Линуксоиды':
             if message.text.lower() == 'BOOM':
                 bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date=time()+20000)
             if message.text.lower() == 'привет':

                 bot.send_message(-1001495083425, 'привет ')  
bot.polling(none_stop=True)
