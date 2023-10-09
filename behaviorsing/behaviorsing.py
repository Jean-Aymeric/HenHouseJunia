from abc import ABC, abstractmethod


class BehaviorSing(ABC):
    @abstractmethod
    def sing(self) -> str :
        ...
