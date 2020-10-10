#!/usr/bin/env python3
'''module that defines save class'''
from base_model import Base


class Save(Base):
    '''class to define a player'''

    def __init__(self):
        '''method to be called upon object instantiation'''
        self.user_id = 1
        self.save_point = 0
        self.flags_tripped = 0
