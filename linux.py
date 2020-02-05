import random
import telebot
import requests
from time import time
bot = telebot.TeleBot('989825137:AAEIuzOL8Xpdc7p26AclSnuFpW7FeKkfhWY')
r = str(random.randint(0, 10))
from telebot import types
xp = 3
ll = 1
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(-1001495083425, 'УВАГА!!!УВАГА!!!УВАГА!!!\nВ бота добавилася нова функція якщо ти напишеш\n/russianroulette\nто у тебе є шанс 1 із 10 що ти получиш мут на день пробуй)\nмут - незмога писати повідомлень')
@bot.message_handler(commands=['me'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет ' + str(message.from_user.first_name) + ' у тебя: '+ str(xp) + 'XP')
@bot.message_handler(commands=['russianroulette'])
def send_text(message):
    o = str(random.randint(1, 10))
    print(o)
    bot.send_message(-1001495083425, str(message.from_user.first_name) + ' Чтобы не было спама, лови мут на 2 минуты:)' )
    #bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date=time()+120)
    if message.chat.type == 'supergroup':
        if message.chat.title == 'Python Developers (on linux)':
            if o == '1':
                bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date=time()+86400)
                bot.send_message(-1001495083425, str(message.from_user.first_name) + ' мут на день) твоє число: ' + '1')
            if o != '1':
                bot.send_message(-1001495083425, str(message.from_user.first_name) +' ти везунчик тебе випало: ' + o)  
@bot.message_handler(content_types=['text'])
def send_text1(message):
    if message.chat.type == 'supergroup':
        if message.chat.title == 'Python Developers (on linux)':
            if message.text.lower() == 'k':
                xp += 1
                bot.send_message(-1001495083425, str(message.from_user.first_name) + str(xp))
            if message.text.lower() == 'бум':
                bot.restrict_chat_member(message.chat.id,message.from_user.id, until_date=time()+20000)
            if message.text.lower() == 'привет':
                bot.send_document(message.chat.id,'https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif',caption='привет мой друг '+ str(message.from_user.first_name) + ' я хочю тебе сказать привет)')
@bot.message_handler(content_types=['new_chat_members'])
def send_text2(message):

    bot.send_document(message.chat.id,'https://media.giphy.com/media/Cmr1OMJ2FN0B2/giphy.gif',caption='привет мой друг '+ str(message.from_user.first_name) + ' я хочю тебе сказать привет)')

bot.polling(none_stop=True)
   