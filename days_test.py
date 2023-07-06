# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.

from parce_date.days_parsing import TextToDate

if __name__ == '__main__':
    ttd = TextToDate()
    print(ttd('1-й четверг ноября'))  # 2023-11-02
    print(ttd('3-я среда мая'))  # 2023-05-17
    print(ttd.date)  # без лога, обращение к параметру
    print(ttd('5-я среда мая'))  # WeekNumberError
    print(ttd('2-я середина мая'))  # WeekDayNameError
    print(ttd('2-я среда травня'))  # MonthNameError
    print(ttd())  # Wrong Argument
    print(ttd(''))  # Wrong Argument
