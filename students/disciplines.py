from .test_rate import TestRate
from .test_name import TestName

__all__ = ['Discipline']

# диапазон оценок по предметам
_MIN_RATE = 2
_MAX_RATE = 5

# диапазон оценок по тестам
_MIN_TEST = 0
_MAX_TEST = 100


class Discipline:
    """Класс дисциплина."""
    rate_value = TestRate(_MIN_RATE, _MAX_RATE)
    test_value = TestRate(_MIN_TEST, _MAX_TEST)
    name = TestName()

    def __init__(self, name: str, rate_value: int, test_value: int):
        self.name = name
        self.rate_value = rate_value
        self.test_value = test_value

    def __str__(self):
        return f'{self.name} - {self.rate_value}, {self.test_value}'

    def __repr__(self):
        return f'Discipline({self.name}, {self.rate_value}, {self.test_value})'

    def __eq__(self, other):
        """Сравнение объектов дисциплина."""
        if self.name == other.name:
            return True
        return False

    def __hash__(self):
        """Хэш объекта."""
        return hash((self.name, self.rate_value, self.test_value))
