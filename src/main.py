import telebot
import os
from loguru import logger
from telebot import types
from src.utils import create_keyboard
from src.constants import keyboards

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
            parse_mode='HTML'
        )

        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.respond_text = self.bot.message_handler(func=lambda message: True )(self.respond_text)


    def send_welcome(self, message):
        self.set(message)

        # markup = types.ReplyKeyboardMarkup(row_width=2)
        # itembtn1 = types.KeyboardButton('a')
        # itembtn2 = types.KeyboardButton('v')
        # itembtn3 = types.KeyboardButton('d')
        # markup.add(itembtn1, itembtn2, itembtn3)
        self.bot.send_message(message.chat.id, "Choose", reply_markup=create_keyboard(['Connect', 'Settings']))
        # self.bot.reply_to(message, f'Hii <b>{self.name}</b>!')

    def respond_text(self, message):
        self.set(message)
        self.bot.send_message(message.chat.id, f"hiii {self.name}")

    def set(self, message):
        self.name = message.chat.first_name
        if message.chat.last_name:
            self.name = f'{self.name} {message.chat.last_name}'
    def run(self):
        logger.info("Running Bot")
        self.bot.polling()


if __name__ == '__main__':
    bot = Bot()
    bot.run()


# You can set parse_mode by default. HTML or MARKDOWN


