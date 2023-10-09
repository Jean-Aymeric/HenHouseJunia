from hen import Hen
from behaviorsing.behaviorsingpouetpouet import BehaviorSingPouetPouet

class PlasticHen(Hen):

    def __init__(self, name: str, nickname=""):
        super().__init__(name,BehaviorSingPouetPouet(), nickname)


