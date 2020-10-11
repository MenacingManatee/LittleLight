#!/usr/bin/env python3
'''Module that is used for file storage'''
import os
import pickle


class FileStorage():
    '''class FileStorage'''

    # path to save game file
    __file_path = 'save_game.py'

    @classmethod
    def save(save_game):
        '''FileStorage module to create a saved game'''
        save_game.__achievements.append(achievement.check_achievements())
        with open('save_game.py', 'w') as file:
            pickle.dump(save_game, file)
        return

    @classmethod
    def load_save():
        '''FileStorage method to load a saved game'''
        with open('save_game.py', 'rb') as file:
            return pickle.load(file)

    @classmethod
    def delete_save():
        '''FileStorage method to delete previous saved game'''
        if os.path.exists('save_game.py'):
            os.remove('save_game.py')
        else:
            print('No save data found')
