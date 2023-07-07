"""
Логирование действий. Для ведения лога используется декорируемый вызов.
"""
import logging
from typing import Callable

FORMAT_LOG = "{levelname:<8} {asctime} {name} {msg}"


class Log:
    """
    Класс логирования операций
    """

    def __init__(self, file_name: str, name: str, log_level=logging.INFO):
        """
        Инициализация экземпляра класса логирования.

        :param file_name: Файл для сохранения лога.
        :param name: Имя модуля.
        :param log_level: Уровень логирования.
        """
        logging.basicConfig(filename=file_name, level=log_level, format=FORMAT_LOG, style='{', encoding='utf-8')
        self.logger = logging.getLogger(name)
        self.level = log_level

    def __call__(self, func: Callable):
        """
        Создание лога для обертываемой функции/метода.

        :param func: Логируемая функция/метод
        :return: результат выполнения func
        """

        def wrapper(*args, **kwargs):
            result = None
            if len(args) > 1:
                _, params = args
            else:
                params = None

            try:
                result = func(*args, **kwargs)
                self.logger.info(f"'{params}' - Ok")
            except Exception as ex:
                self.logger.error(f"'{params}' - {ex}")
            return result

        return wrapper
