from typing import Union


class MissedDeadlineError(Exception):
    """
    Поднимается, когда фиплёнок пропустил дедлайн.
    """


class FiplPipl:
    """
    Фиплёнок, который прокрастинирует домашку.
    """
    def __init__(self, deadline: Union[int, float] = 1):
        """
        :param deadline: сколько часов осталось до дедлайна. Дефолтное значение: 1.
        """
        self.deadline = deadline

    def postpone(self, hours: Union[int, float]) -> Union[int, float]:
        """
        Отложить дедлайн фиплёнка.
        :param hours: на сколько часов откладывается дедлайн.
        :return: оставшееся кол-во часов до дедлайна.
        """
        if hours < 0:
            raise ValueError('Кол-во часов должно быть положительным!')
        self.deadline += hours
        return self.deadline

    def procrastinate(self, hours: Union[int, float]) -> Union[int, float]:
        """
        Прокрастинировать дедлайн и уменьшать часы до него.
        :param hours: сколько часов фиплёнок прокрастинирует.
        :return: оставшееся кол-во часов до дедлайна.
        """
        if hours < 0:
            raise ValueError('Кол-во часов должно быть положительным!')
        if hours >= self.deadline:
            raise MissedDeadlineError('Допрокрастинировался... Дедлайн пропущен!')
        self.deadline -= hours
        return self.deadline

    def check_deadline(self) -> Union[int, float]:
        """
        Проверить, скоро ли дедлайн.
        :return: оставшееся кол-во часов до дедлайна.
        """
        return self.deadline
