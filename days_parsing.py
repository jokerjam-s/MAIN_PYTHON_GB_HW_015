# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime

_MONTHS = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'мая': 5, 'июн': 6,
           'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12,
           }
_WEEK_DAYS = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5, 'воскресенье': 6, }


class TextToDate:
    """
    Класс поиска даты по строке вида “1-й четверг ноября”, “3-я среда мая”
    """

    def __init__(self, text: str = None, logger: logging = None):
        """
        Инициализация экземпляра объекта перевода текста в дату
        :param text: Текст для обработки
        :param logger: Логгер для обработки ошибок
        """
        self.text = text
        if logger is None:
            format_log = "{levelname} {asctime}: {msg}"
            logging.basicConfig(filename="errors.log", encoding='utf-8', level=logging.ERROR, style="{",
                                format=format_log)
            logger = logging.Logger(__name__)
        self.logger = logger
        self._date_value = None
        self._calc_date()

    def _calc_date(self):
        DAYS_IN_MONTH = 30
        week, day, month = text.split()
        week = int(week[0])
        day = parse_day(day)
        month = parse_month(month)
        year = datetime.now().year
        week_counter = 0
        for i in range(1, DAYS_IN_MONTH + 1):
            data = datetime(day=i, month=month, year=year)
            if data.weekday() == day:
                week_counter += 1
                if week_counter == week:
                    return data

        pass

    def __call__(self, text: str):
        self.text = text
        self._calc_date()
        return self._date_value

    @property
    def date(self):
        return self._date_value
