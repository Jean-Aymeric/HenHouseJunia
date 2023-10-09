from hen import Hen


class Henhouse:
    __hens: [Hen]

    def __init__(self):
        self.__hens = []

    def addHen(self, hen: Hen) -> None:
        self.__hens.append(hen)

    def removeHen(self, hen:Hen)-> None:
        self.__hens.remove(hen)

    def singAll(self):
        for hen in self.__hens:
            hen.sing()

