# - *- coding: utf- 8 - *-
import os
import sys
import telebot
from telebot import types
# reload(sys)
# sys.setdefaultencoding('utf-8')


TOKEN = "YOUR_TOKEN"
bot = telebot.TeleBot(TOKEN, parse_mode='html')


eco_dict = {}
class Eco:
    def __init__(self, location):
        self.location = location
        self.img_video = None
        self.phone = None
        keys = ['description', 'name']
        for key in keys:
            self.key = ""


@bot.message_handler(commands=['start'])
def start(message):
    try:
        user_name = message.from_user.first_name
        chat_id = message.chat.id

        response = "Assalomu alaykum {0}. Navoiy viloyati hududida ekologik qonunbuzarliklarni xabar qilish botiga xush kelibsiz.".format(user_name)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
        button_menu = types.KeyboardButton(text="\U0001F331 Ekologik qonunbuzarlikni xabar qilish")
        markup.add(button_menu)
        msg = bot.send_message(chat_id=chat_id, text=response, reply_markup=markup)

        bot.register_next_step_handler(msg, menu)
    except Exception as e:
        print(repr(e))


def cancel(message):
    chat_id = message.chat.id

    response = "Operatsiya bekor qilindi!"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    button_menu = types.KeyboardButton(text="\U0001F331 Ekologik qonunbuzarlikni xabar qilish")
    markup.add(button_menu)

    msg = bot.send_message(chat_id=message.chat.id, text=response, reply_markup=markup)
    bot.clear_step_handler_by_chat_id(chat_id=chat_id)
    bot.register_next_step_handler(msg, menu)


@bot.message_handler(content_types=['text'])
def menu(message):
    try:
        chat_id = message.chat.id
        if message.text == "\U0001F331 Ekologik qonunbuzarlikni xabar qilish":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
            button_geo = types.KeyboardButton(text="\U0001F4CD Hudud joylashuvini yuborish", request_location=True)
            button_cancel = types.KeyboardButton(text="\U0001F61E Bekor qilish")
            markup.add(button_geo)
            markup.add(button_cancel)
            bot.send_message(chat_id=chat_id, text="Huquqbuzarlik qayd etilgan hudud geolokatsiyasini yuboring", reply_markup=markup)

            # bot.register_next_step_handler(msg, handle_location)
    except Exception as e:
        print(repr(e))


bot.enable_save_next_step_handlers(delay=2)
bot.load_next_step_handlers()


if __name__ == '__main__':
    # RUN
    bot.polling(none_stop=True)
