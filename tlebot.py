import telebot
from decouple import config

BOT_TOKEN = config('BOT_TOKEN')

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commads=["start","help"])
def welcome(msg):
    bot.send_message(msg.chat.id, "hello to my bot what you whant?")
    
bot.polling()
