import random

options = ['paper', 'scissors', 'rock']
points = 0
name = ''
option = ''
beat = []
defeat = []


def read_file():
    dict_rating = {}
    global name, points

    new_file = open('rating.txt', 'r')

    for line in new_file:
        key, value = line.split()
        dict_rating[key] = value

    new_file.close()

    if name in dict_rating.keys():
        points = int(dict_rating[name])


def check_input():
    while True:
        user_input = input()
        if user_input == '!exit':
            print('Bye!')
            break
        elif user_input in options:
            who_win(user_input)
        elif user_input == '!rating':
            print('Your rating:', points)
        else:
            print('Invalid input')


def new_options(new_rules):
    global options, option, beat, defeat

    if new_rules:
        options = new_rules.split(',')
        print("Okay, let's start")

    option = random.choice(options)
    option_index = options.index(option)

    new_list = options[option_index + 1:] + options[:option_index]
    beat = new_list[:round(len(new_list) / 2)]
    defeat = new_list[round(len(new_list) / 2):]


def user_win():
    global points

    print(f'Well done. The computer chose {option} and failed')
    points += 100


def user_lose():
    print(f'Sorry, but the computer chose {option}')


def draw():
    global points

    print(f'There is a draw ({option})')
    points += 50


def who_win(user_input):
    new_options('')
    if user_input == option:
        draw()
    elif user_input in beat:
        user_win()
    elif user_input in defeat:
        user_lose()


def main():
    global name

    name = input('Enter your name: ')
    print('Hello,', name)
    read_file()

    new_rules = input()
    new_options(new_rules)

    check_input()


main()
