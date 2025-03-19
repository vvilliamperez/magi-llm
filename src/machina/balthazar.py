from machina.machina import Machina


class Balthazar(Machina):

    def __init__(self):
        super().__init__()
        self.query = None
        self.prompt_prelude = "You are Balthazar"

