from emoji.core import emoji_count
import telebot
import os
import emoji
from loguru import logger
from telebot import types
from src.utils import create_keyboard
from src.constants import keyboards
from src.constants import predefined_texts
from src.constants import states
from src.constants import KEYS

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
        self.users = dict()
        self.send_welcome = self.bot.message_handler(commands=['start', 'help'])(self.send_welcome)
        self.respond_text = self.bot.message_handler(func=lambda message: True )(self.respond_text)
    def send_welcome(self, message):
        self.set(message)
        response = f'Hii {self.name}.\n' + predefined_texts.welcome
        self.bot.send_message(message.chat.id, response, reply_markup=keyboards.main)
        self.users[self.chat_id]['state'] = states.init
        self.users[self.chat_id]['name'] = message.chat.first_name
        for uinfo in self.users.values():
            logger.info(uinfo['username'])
            logger.info(uinfo['state'])


    def respond_text(self, message):
        self.set(message)
        message.text = emoji.demojize(message.text)
        if message.text == KEYS.disconnect:
            # self.send_message(predefined_texts.disconncet, reply_markup=keyboards.main)
            # self.set_state(states.init)
            self.disconnect()
        elif  self.get_state() == states.talking:
            self.send_message(message.text, chat_id=self.users[self.chat_id]['random_connect'])
        #trying to connect
        elif message.text == KEYS.random_connect:
            # connect it to a random stranger
            self.send_message(
                ':hourglass_not_done: Waiting for someone to connect...',
                reply_markup=keyboards.back
            )
            self.set_state(states.random_connect)
        elif message.text == KEYS.back:
            self.send_message(predefined_texts.init, reply_markup=keyboards.main)
            self.users[self.chat_id]['state'] = states.init



        # self.send_message(f"hiii {self.name}")

        if self.get_state() == states.random_connect:
            self.connect()

    def send_message(self, bot_response, chat_id = None, reply_markup = None, emojize = True):
        if emojize:
            bot_response = emoji.emojize(bot_response)
        if not chat_id:
            chat_id = self.message.chat.id
        self.bot.send_message(chat_id, bot_response, reply_markup=reply_markup)

    def set(self, message):
        self.message = message
        self.chat_id = message.chat.id
        self.name = message.chat.first_name
        if message.chat.last_name:
            self.name = f'{self.name} {message.chat.last_name}'
        if not self.users.get(self.chat_id):
            self.users[self.chat_id] = dict(
                username = message.chat.username
            )

    def get_state(self):
        return self.users[self.chat_id]['state']

    def set_state(self, state, chat_id = None):
        if chat_id == None:
            chat_id = self.chat_id

        self.users[chat_id]['state'] = state

    def connect(self):
        for chat_id, info in self.users.items():
            if self.chat_id == chat_id:
                continue;

            if self.users[chat_id]['state'] != states.random_connect:
                continue;
            name = self.users[chat_id]['name']
            self.send_message(
                f':check_mark_button: Connected to {name}. Start talking!',
                chat_id=self.chat_id,
                reply_markup=keyboards.talking,
            )
            self.send_message(
                f':check_mark_button: Connected to {self.name}. Start talking!',
                chat_id=chat_id,
                reply_markup=keyboards.talking,
            )

            self.users[self.chat_id]['random_connect'] = chat_id
            self.users[chat_id]['random_connect'] = self.chat_id

            self.set_state(states.talking, self.chat_id)
            self.set_state(states.talking, chat_id)
    def disconnect(self):
        self.send_message(predefined_texts.disconnect,
            reply_markup=keyboards.main
            )
        self.send_message(predefined_texts.disconnect,
            chat_id = self.users[self.chat_id]['random_connect'],
            reply_markup=keyboards.main
            )
        self.set_state(states.init)
        self.set_state(states.init, chat_id = self.users[self.chat_id]['random_connect'])

        # self.users[]
        # for uinfo in self.users.values():
        #     logger.info(uinfo['username'])
        #     logger.info(uinfo['state'])
    def run(self):
        logger.info("Running Bot")
        self.bot.polling()


if __name__ == '__main__':
    bot = Bot()
    bot.run()


# You can set parse_mode by default. HTML or MARKDOWN


