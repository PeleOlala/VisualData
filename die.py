from random import randint

class Die:
    """ Один кубік"""
    def __init__(self,num_side=6):
        self.num_side=num_side
    def roll(self):
        """кинемо кубик"""
        return randint(1, self.num_side)
