from datetime import datetime


class Player:
    __LVL = 1
    __HEALTH = 100

    # В __slots__ нужно указывать искаженные имена для приватных переменных
    __slots__ = ["_Player__lvl", "_Player__health", "_Player__born"]

    def __init__(self) -> None:
        self.__lvl = Player.__LVL
        self.__health = Player.__HEALTH
        self.__born = datetime.now()

    @property
    def lvl(self):

        time_diff = datetime.now() - self.__born
        return self._Player__lvl, str(time_diff)

    @lvl.setter
    def lvl(self, numeric: int):
        self._Player__lvl += Player.__type_test(numeric)
        if self._Player__lvl >= 100:
            self._Player__lvl = 100

    @classmethod
    def set_cls_field(cls):
        cls.__LVL = Player.__type_test(20)
        cls.__HEALTH = Player.__type_test(200)

    # Метод проверки типов (статический, а не property)
    @staticmethod
    def __type_test(value: int):
        if isinstance(value, int):
            return value
        raise TypeError("Это не число!")


user1 = Player()
print(user1.lvl)

Player.set_cls_field()

user2 = Player()
print(user2.lvl)
