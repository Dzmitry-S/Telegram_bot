import telebot
from telebot import types
from secret import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')

@bot.message_handler(content_types=['/ster'])
def get_user_text(message):
    if message.text == 'hello':
        bot.send_message(message.chat.id, 'Hey)', parse_mode='html')
    elif message.text == 'id':
        bot.send_message(message.chat.id, f'your id:{message.from_user.id} ', parse_mode='html')
    elif message.text == 'photo':
        photo = open('Снимок экрана 2022-04-01 в 19.25.29.png', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'Hm?...', parse_mode='html')

    # bot.send_message(message.chat.id, message, parse_mode='html')

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, ' Wow beautiful photo!')


@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Go web site',url="https://steambuy.com/"))
    bot.send_message(message.chat.id,  "Gooooo", reply_markup=markup )


@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    website = types.KeyboardButton('Web site')
    start = types.KeyboardButton('start')
    markup.add(website,start)
    bot.send_message(message.chat.id,  "Gooooo", reply_markup=markup )


bot.polling(none_stop=True)
