import telebot
import os
from loguru import logger

class Bot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(
            os.environ['TelegramBotToken'],
            parse_mode=None

        self.send_welcome(self.bot.message_handler(commands=['start', 'help']))
        
@bot.message_handler(filters)
def function_name(message):
	bot.reply_to(message, "This is a message handler")
    
    def run(self):
        logger.info("Running Bot")
        self.bot.polling()
    

    if __name__ == '__main__':
        Bot.run()


) # You can set parse_mode by default. HTML or MARKDOWN


