import telebot

bot = telebot.TeleBot('5672004290:AAFowrg-L7DV5UrgK3cX5S1VevhRIvUHlQM')

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat_id, '<b>Hi</b>', parse_mode='html')



bot.polling(none_stop = True)

#@bot.message_