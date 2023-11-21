#!/usr/bin/python3

HELP = """
help - напечатать справку по программе.
add - добавить задачу в список (название задачи запрашиваем у пользователя).
show - напечатать все добавленные задачи."""

today = []
tomorrow = []
other = []

while True:
    command = input("Введите команду: ")
    if command == "help":
        print(HELP)
    elif command == "show":
        print("Задачи на сегодня:", today)
        print("Задачи на завтра:", tomorrow)
        print("Задачи на другие дни:", other)
    elif command == "add":
        date = input("Введите дату выполнения задачи: ")
        task = input("Введите название задачи: ")
        if date == "Сегодня":
            today.append(task)
        elif date == "Завтра":
            tomorrow.append(task)
        else:
            other.append(task)
        print("Задача добавлена")
    elif command == "exit":
        print("Спасибо за использование!")
        break
    else:
        print("Неизвестная команда")
        break

print("До свидания!")