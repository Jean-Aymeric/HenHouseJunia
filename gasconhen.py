from behaviorsing.behaviorsingcotcotcon import BehaviorSingCotCotCon
from hen import Hen


class GasconHen(Hen):

    def __init__(self, name: str, nickname=""):
        super().__init__(name, BehaviorSingCotCotCon(), nickname)


