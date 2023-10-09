from hen import Hen
from behaviorsing.behaviorsingcotcot import BehaviorSingCotCot

class KikineHen(Hen):

    def __init__(self, name: str, nickname=""):
        super().__init__(name, BehaviorSingCotCot(), nickname)


