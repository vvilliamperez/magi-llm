from random import randint
from pydantic import BaseModel
from decision_maker import DecisionMaker
from openai import OpenAI


class Machina(DecisionMaker):

    def __init__(self):
        super().__init__()
        self.query = None
        self.current_decision = None
        self.prelude = ""
        self.confidence = 0.0
        self.notes = ""

    def set_query(self, query):
        self.query = query

    """
    Decide on a boolean value
    """
    def decide(self):
        if self.query is None:
            raise Exception("Query not set.")

        self.send_api_request()
        # random bool from random number generator
        # self.current_decision = bool(randint(0, 1))
        return self.current_decision

    def get_current_decision(self):
        return self.current_decision

    def get_current_confidence(self):
        return self.confidence

    def get_current_notes(self):
        return self.notes

    def send_api_request(self):

        client = OpenAI()

        class OpenAIDecision(BaseModel):
            decision: bool
            confidence: float
            notes: str

        completion = client.beta.chat.completions.parse(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": self.prelude},
                {"role": "user", "content": self.query}
            ],
            response_format=OpenAIDecision,
        )
        event = completion.choices[0].message.parsed


        self.current_decision = event.decision
        self.confidence = event.confidence
        print(f"Decision: {self.current_decision} with confidence {self.confidence}")












