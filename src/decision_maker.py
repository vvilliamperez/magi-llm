from abc import ABC, abstractmethod


class DecisionMaker(ABC):
    def __init__(self):
        self.decision = None

    @abstractmethod
    def decide(self):
        pass

    @abstractmethod
    def set_query(self, query):
        pass
