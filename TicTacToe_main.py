# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:04:17 2017

@author: jan.verheyen
"""
import Take_picture
import TicTacToe_game
import TicTacToe_move

import numpy as np

game = True
game_matrix = np.array(([5,5,5],[5,5,5],[5,5,5]))

while game == True:
    
    whoplays = input()    
    
    Take_picture.take_picture()
    
    game_matrix = TicTacToe_move.find_move('tic-tac-toe')
            
    TicTacToe_game.computer(game_matrix,whoplays)
        
    #insert code to make robot move