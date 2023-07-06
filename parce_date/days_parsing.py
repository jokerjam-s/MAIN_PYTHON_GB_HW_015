# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
import logging
from datetime import datetime, timedelta

from parce_date.days_except import ParceDaysExceptions, WrongFormatDate, WeekNumberError, WeekDayNameError, \
    MonthNameError
from log_saver.log_saver import Log

__all__ = ['TextToDate']


class TextToDate:
    """
    Класс поиска даты по строке вида “1-й четверг ноября”, “3-я среда мая”
    """
    _MONTHS = {'янв': 1, 'фев': 2, 'мар': 3, 'апр': 4, 'май': 5, 'мая': 5, 'июн': 6,
               'июл': 7, 'авг': 8, 'сен': 9, 'окт': 10, 'ноя': 11, 'дек': 12,
               }
    _WEEK_DAYS = {'понедельник': 0, 'вторник': 1, 'среда': 2, 'четверг': 3, 'пятница': 4, 'суббота': 5,
                  'воскресенье': 6, }

    _WEEK_NO_MIN = 1
    _WEEK_NO_MAX = 4

    def __init__(self):
        """
        Инициализация экземпляра объекта перевода текста в дату.
        """
        self.text = None
        self._date_value = None

    def _calc_date(self) -> None | ParceDaysExceptions:
        """
        Если текст, передаваемый для анализа пуст или имеет ошибки - выбрасывает соответствующее исключение

        :return: None или исключение в случае ошибок в тексте для анализа
        """
        week, day, month = self.text.split()
        week_no = int(week[0])
        day_no = self._parse_day(day)
        month_no = self._parse_month(month)

        if day_no is None:
            raise WeekDayNameError()
        if week_no not in range(self._WEEK_NO_MIN, self._WEEK_NO_MAX):
            raise WeekNumberError()
        if month_no is None:
            raise MonthNameError()

        year = datetime.now().year
        date_start = datetime(year, month_no, 1)

        while date_start.weekday() != day_no:  # найти первый нужный день недели в месяце
            date_start += timedelta(days=1)

        self._date_value = date_start + timedelta(days=7 * (week_no - 1))  # Прибавить необходимое количество недель
        return

    def _parse_day(self, day_text) -> int | None:
        return self._WEEK_DAYS.get(day_text, None)

    def _parse_month(self, month_text) -> int | None:
        if len(month_text) > 3:
            month_text = month_text[:3]
        return self._MONTHS.get(month_text, None)

    @Log('date_log.log', __name__)
    def __call__(self, text: str) -> datetime | ParceDaysExceptions:
        self.text = text
        self._calc_date()
        return self._date_value

    @property
    def date(self) -> datetime:
        """
        Последняя полученная дата
        :return: datetime
        """
        return self._date_value
