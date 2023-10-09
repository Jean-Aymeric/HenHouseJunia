from behaviorsing.behaviorsingcotcot import BehaviorSingCotCot
from hen import Hen

class GingerHen(Hen):

    def __init__(self, name: str, nickname=""):
        super().__init__(name,BehaviorSingCotCot(), nickname)


