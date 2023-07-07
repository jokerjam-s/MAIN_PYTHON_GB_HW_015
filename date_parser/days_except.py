"""
Исключения для отлова ошибок в передаваемых для анализа данных
"""

__all__ = ['WrongFormatDate', 'WeekNumberError', 'WeekDayNameError', 'MonthNameError']


class ParceDaysExceptions(Exception):
    pass


class WrongFormatDate(ParceDaysExceptions):
    """
        Исключение - неверный формат даты для анализа
        """

    def __init__(self, message: str = None):
        if message is None:
            message = 'Wrong text format for parsing!'
        self._message = message

    def __str__(self):
        return self._message


class WeekNumberError(ParceDaysExceptions):
    """
    Исключение - недопустимый номер недели
    """

    def __init__(self, message: str = None):
        if message is None:
            message = 'Wrong week number of a month! Week number must be from 1 to 4 included.'
        self._message = message

    def __str__(self):
        return self._message


class WeekDayNameError(ParceDaysExceptions):
    """
    Исключение - неверно задано название дня недели
    """

    def __init__(self, message: str = None):
        if message is None:
            message = 'Wrong name of weekday!'
        self._message = message

    def __str__(self):
        return self._message


class MonthNameError(ParceDaysExceptions):
    """
    Исключение - неверно задано наименование месяца
    """

    def __init__(self, message: str = None):
        if message is None:
            message = 'Wrong month name!'
        self._message = message

    def __str__(self):
        return self._message
