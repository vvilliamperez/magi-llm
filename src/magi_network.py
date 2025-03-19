from decision_maker import DecisionMaker
from magi import Magi

"""
Recursive trinary decision tree

If it's a leaf node, it contains 3 machina as a magi.
If it's not a leaf node, it contains 3 MagiNetworks as a magi.
"""

class MagiNetwork(DecisionMaker):


    def __init__(self, level):
        super().__init__()
        self.level = level
        self.leaf_node = True if level == 1 else False
        self.decision_makers = []
        self._set_up_magi_network()

    def _set_up_magi_network(self):
        if self.leaf_node:
            self.decision_makers = [Magi()]
        else:
            for i in range(3):
                self.decision_makers.append(MagiNetwork(self.level - 1))


    def set_query(self, query):
        for decision_maker in self.decision_makers:
            decision_maker.set_query(query)


    def decide(self):
        results = []
        for decision_maker in self.decision_makers:
            result = decision_maker.decide()
            results.append(result)
        # Majority vote from a list of bools.
        # Count the number of True values and return True if the count is greater than 1
        print(f"results from the 3 child objects: {results}")

        if self.leaf_node:
            total_network_result = results[0]
        else:
            total_network_result = results.count(True) > 1
        print(f"total result from the child objects: {total_network_result}")
        return total_network_result


