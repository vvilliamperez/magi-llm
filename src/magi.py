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
        self.current_decision = None
        self.machine_results = []

    def decide(self):
        self.machine_results = []
        for machine in self.machines:
            result = machine.decide()
            self.machine_results.append(result)
        
        #print(f"results from the 3 machines: {self.machine_results}")
        self.current_decision = self.machine_results.count(True) > 1
        #print(f"total result from machines: {self.current_decision}")
        return self.current_decision

    def set_query(self, query):
        for machine in self.machines:
            machine.set_query(query)

    def get_tree_representation(self, prefix=""):
        obj_id = hex(id(self))
        tree = f"{prefix}Magi {obj_id} -> {self.current_decision}\n"
        for machine, result in zip(self.machines, self.machine_results):
            machine_name = machine.__class__.__name__
            machine_id = hex(id(machine))
            tree += f"{prefix}├── {machine_name} {machine_id} -> {result}\n"
        return tree


