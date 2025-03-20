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
        self.current_decision = None
        self.decision_maker_results = []
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
        self.decision_maker_results = []
        for decision_maker in self.decision_makers:
            result = decision_maker.decide()
            self.decision_maker_results.append(result)

        #print(f"results from the 3 child objects: {self.decision_maker_results}")

        if self.leaf_node:
            self.current_decision = self.decision_maker_results[0]
        else:
            self.current_decision = self.decision_maker_results.count(True) > 1
            
        #print(f"total result from the child objects: {self.current_decision}")
        return self.current_decision

    def get_tree_representation(self, prefix=""):
        obj_id = hex(id(self))
        tree = f"{prefix}MagiNetwork(L{self.level}) {obj_id} -> {self.current_decision}\n"
        
        for i, decision_maker in enumerate(self.decision_makers):
            is_last = i == len(self.decision_makers) - 1
            current_prefix = prefix + ("└── " if is_last else "├── ")
            next_prefix = prefix + ("    " if is_last else "│   ")
            tree += decision_maker.get_tree_representation(current_prefix)
        
        return tree


