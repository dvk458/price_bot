from telebot import TeleBot, types

bot = TeleBot('1960085788:AAFx6PskBD-PhWfmi2qUxxoG7BX29VqFOF4')
@bot.message_handler(commands=['price'])
def start_command(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/AMD')
    itembtn2 = types.KeyboardButton('/NVIDIA')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, text='CHOOSE ONE', reply_markup=markup)

@bot.message_handler(commands=['AMD'])
def amd_command(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('6600')
    itembtn2 = types.KeyboardButton('5800')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, text='CHOOSE MODEL', reply_markup=markup)

bot.polling()

