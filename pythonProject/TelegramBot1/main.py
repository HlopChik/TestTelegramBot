import telebot#импортируем библиотеку
from telebot import types

bot = telebot.TeleBot('5387129205:AAH70u9paZnpKFxmi0WErrzuBLSCcOOagYs')#создаём переменную для хранения TOKEN.

#отслеживание команд!
#from_user-Обращение к пользователю.
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Рад знакомству,<b><u>{message.from_user.first_name} {message.from_user.last_name},' \
           f'данный бот понимает такие команды , как:( /start , /help ) , ' \
           f' так же вы моежете общаться с ним,отправляя сообщения: Hello ,Как у тебя дела?, Photo  ' \
           f' Бот знает ваш id</u></b> , '

    bot.send_message(message.chat.id,mess,parse_mode='html')

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить веб сайт",  url="https://www.google.com/"))
    bot.send_message(message.chat.id,'Перейдите на сайт',reply_markup=markup)

@bot.message_handler(commands=['buttons'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True , row_width=1)
    website = types.KeyboardButton('Поиск информации')
    start = types.KeyboardButton('Start')
    markup.add(website,start)
    bot.send_message(message.chat.id,'Перейдите на сайт',reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    mess1 = f'<b><u>{message.from_user.first_name} {message.from_user.last_name}</u></b>,чем я могу тебе помочь?'
    bot.send_message(message.chat.id,mess1,parse_mode='html')

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text.capitalize() == "Hello":
        bot.send_message(message.chat.id,f'И тебе привет <b>{message.from_user.first_name} {message.from_user.last_name}</b>', parse_mode='html')
    elif message.text.capitalize() == "Как у тебя дела?":
        bot.send_message(message.chat.id,f'<b>Всё хорошо,спасибо что спросил.</b>', parse_mode='html')
    elif message.text.upper() == "ID":
        bot.send_message(message.chat.id,f'Пожалуйста твой ID: <b>{message.from_user.id}</b>', parse_mode='html')
    elif message.text.capitalize() == "Photo":
        photo = open('python-featured.width-1440.jpg','rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, f'Я тебя не понимаю!', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id,'Красивое фото!')





bot.polling(none_stop=True)#Постоянная работа бота.

