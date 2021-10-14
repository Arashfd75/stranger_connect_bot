import telebot
import os
from loguru import logger
# print(os.environ['TelegramBotToken'])
# bot = telebot.TeleBot(os.environ['TelegramBotToken'],parse_mode=None)
# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")
# print('starting bot')
# bot.polling()
class Bot:
    def __init__(self) -> None:
        self.bot = telebot.TeleBot(
            os.environ['TelegramBotToken'],
            parse_mode=None
        )

        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)


    def send_welcome(self, message):
	    bot.reply_to(message, "This is a message handler")

    def run(self):
        logger.info("Running Bot")
        self.bot.polling()


if __name__ == '__main__':
    bot = Bot()
    bot.run()


# You can set parse_mode by default. HTML or MARKDOWN


