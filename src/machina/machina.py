from random import randint

from decision_maker import DecisionMaker


class Machina(DecisionMaker):

    def __init__(self):
        super().__init__()
        self.query = None
        self.prompt_prelude = ""

    def set_query(self, query):
        self.query = query

    """
    Decide on a boolean value
    """
    def decide(self):
        # random bool from random number generator
        decision = bool(randint(0, 1))

        return decision


    def send_api_request(self):
        pass