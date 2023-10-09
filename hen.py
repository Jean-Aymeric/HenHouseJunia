from abc import ABC

from behaviorsing.behaviorsing import BehaviorSing


class Hen(ABC): #Le ABC indique que Hen est abstrait
    __name: str
    __nickname: str
    __behaviorsing : BehaviorSing

    def __init__(self, name: str,behaviorsing:BehaviorSing, nickname=""):
        self.__name = name
        self.__behaviorsing = behaviorsing
        self.__nickname = nickname

    def getName(self) -> str:
        return self.__name

    def getNickname(self) -> str:
        if self.__nickname == "":
            return self.__name

        return self.__nickname

    def setNickname(self, nickname: str):
        self.__nickname = nickname

    def setBehaviorSing(self, behaviorsing:BehaviorSing):
        self.__behaviorsing=behaviorsing

    def getBehaviorSing(self):
        return self.__behaviorsing

    def sing(self) -> None:
        print(self.getNickname(), ":", self.__behaviorsing.sing())

