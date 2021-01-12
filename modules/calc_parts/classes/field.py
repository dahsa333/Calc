import random as rnd
from .variable import Variable


class Field():
    def __init__(self):
        #variable_dict
        self.variable_dict = {}
        #value_dict
        self.v = {}

    def Gen_varibale_id(self, variable_dict):
        while True:
            is_unique = True
            id = rnd.randint(0, 999999)
            for curr_variable in variable_dict.items():
                if id == curr_variable[1].id:
                    is_unique = False
            if is_unique is True:
                break
        return id

    def add_variable(self, name, value, latex_name):
        var = Variable(name, value, self.Gen_varibale_id(self.variable_dict), latex_name)
        self.variable_dict.update({var.name: var})
        self.v.update({var.name: var.value})