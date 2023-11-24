#!/usr/bin/python3

from random import choice

import telebot

token = ''

bot = telebot.TeleBot(token)

RANDOM_TASKS = ['Написать письмо Деду Морозу', 'Выучить новое английское слово', 'Записаться на курс в Нетологию', 'Заварить чаю']

todos = dict()

HELP = '''
Список доступных команд:
/help - Напечатать список команд
/print, /show  - напечать все задачи на заданную дату
/add, /todo - добавить задачу
/done - отметить задачу выполненной
/random - добавить на сегодня случайную задачу
'''


def add_todo(date, task):
    date = date.lower()
    todos.setdefault(date, [])
    todos[date].append(task)


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = (choice(RANDOM_TASKS), 0)
    add_todo('сегодня', task)
    bot.send_message(message.chat.id, f'Задача {task[0]} добавлена на сегодня')


@bot.message_handler(commands=['add', 'todo'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = (' '.join([tail]), 0)
    add_todo(date, task)
    bot.send_message(message.chat.id, f'Задача {task[0]} добавлена на дату {date}')

@bot.message_handler(commands=['done'])
def add(message):
    _, date, tail = message.text.split(maxsplit=2)
    task = (' '.join([tail]), 0)
    if date in todos:
        for task in todos[date]:
            if task[0] == tail:
                todos[date].remove(task)
                todos[date].append((task[0], 1))
                break
    bot.send_message(message.chat.id, f'Задача {task[0]} выполнена')

@bot.message_handler(commands=['show', 'print'])
def print_(message):
    date = "сегодня"
    command = message.text.split()
    if len(command) >= 2:
        date = command[1].lower()
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f'[{"X" if task[1] else " "}] {task[0]}\n'
    else:
        tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)


bot.polling(none_stop=True)