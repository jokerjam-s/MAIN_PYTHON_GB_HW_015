# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.

from date_parser.days_parsing import TextToDate
import argparse

if __name__ == '__main__':
    arg_pars = argparse.ArgumentParser(description='Определение даты из строки')
    arg_pars.add_argument('texts', metavar='S', type=str, nargs='*', help='дата в виде: "1-й четверг ноября"')
    args = arg_pars.parse_args()

    ttd = TextToDate()
    if len(args.texts) > 0:
        print('Run set of user\'s tests')
        for text in args.texts:
            print(ttd(text))
    else:
        print('Run set of tests default')
        print(ttd('1-й четверг ноября'))  # 2023-11-02
        print(ttd('3-я среда мая'))  # 2023-05-17
        print(ttd.date)  # без лога, обращение к параметру
        print(ttd('5-я среда мая'))  # WeekNumberError
        print(ttd('2-я середина мая'))  # WeekDayNameError
        print(ttd('2-я среда травня'))  # MonthNameError
        print(ttd())  # Wrong Argument
        print(ttd(''))  # Wrong Argument
