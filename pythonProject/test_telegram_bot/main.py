import telebot

bot  = telebot.TeleBot('5557676318:AAFfB4PDsMMb_gpUom5vx8CCNsnoPtGm4ro')

@bot.message_handler(commands=['start'])#декоратор обрабатывающий команды.
def start(message):#параметр message даёт информацию относительно чата и пользователя
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name} </u></b>'#from_user от кого идёт сообщение.first_name-имя,last_name-Фамилия.
    bot.send_message(message.chat.id,mess,parse_mode='html')

@bot.message_handler(content_types=['text'])#обработка random text
def get_user_text(message):
    if message.text == "Hello":
        bot.send_message(message.chat.id,"И тебе привет", parse_mode='html')
    elif message.text.lower() == "id":
        bot.send_message(message.chat.id,f'Твой ID:{message.from_user.id}', parse_mode='html')
    elif message.text == "photo":
        photo = open('584197deb3fa1158c0393e11.png','rb')
        bot.send_photo(message.chat.id,photo)
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю!", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id,"Вау,красивое фото")

bot.polling(none_stop=True)#Параметр устанавливающий постоянную работу бота