__all__ = ['TestName']


class TestName:
    """Проверка правильности ввода ФИО. Имена должны быть только буквами и начинаться с заглавных."""

    def __set_name__(self, owner, name):
        """Установить имя проверяемого атрибута."""
        self.param_name = name

    def __get__(self, instance, owner):
        """Вернуть значение атрибута."""
        return instance.__dict__[self.param_name]

    def __set__(self, instance, value: str):
        """Установить значение атрибута."""
        if not value.isalpha() or not value.istitle():
            raise ValueError("Неверные данные для ФИО!")
        instance.__dict__[self.param_name] = value
