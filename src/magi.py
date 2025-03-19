
"""
This module contains the Magi class, which is a group of machina that will be used to solve the problem.
It is essentially a trinary decision tree, where the majority vote will be the answer.
"""
from decision_maker import DecisionMaker
from machina.balthazar import Balthazar
from machina.casper import Casper
from machina.melchior import Melchior


class Magi(DecisionMaker):
    def __init__(self):
        super().__init__()
        self.balthazar = Balthazar()
        self.casper = Casper()
        self.melchior = Melchior()
        self.machines = [self.balthazar, self.casper, self.melchior]

    def decide(self):
        results = []
        for machine in self.machines:
            result = machine.decide()
            results.append(result)
        # Majority vote from a list of bools.
        # Count the number of True values and return True if the count is greater than 1
        print(f"results from the 3 machines: {results}")
        total_result = results.count(True) > 1
        print(f"total result from machines: {total_result}")
        return total_result

    def set_query(self, query):
        for machine in self.machines:
            machine.set_query(query)


