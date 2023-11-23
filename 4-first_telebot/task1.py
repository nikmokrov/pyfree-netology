#!/usr/bin/python3

import telebot

token = ''

trigger_name = "Вася"

bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def echo(message):
    msg = message.text
    if trigger_name in message.text:
        msg = "Ба! Знакомые все лица!"
    bot.send_message(message.chat.id, msg)

bot.polling(none_stop=True)
