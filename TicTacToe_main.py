# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 17:04:17 2017

@author: jan.verheyen
"""
import Take_picture
import TicTacToe_game
import TicTacToe_move
import test_example
import time

import numpy as np

game_matrix = np.array(([5,5,5],[5,5,5],[5,5,5]))
position = np.zeros(2) #position the Robot has to play

#is the first move the ROBOT has to do 0= put a O, 1= put an X
firstmove = input("Select first move: ")
game = 0
image_name = 'test'

while game == 0:
    
    if firstmove == 0:

        print game_matrix
        
        game = TicTacToe_game.wincheck(game_matrix)

        time.sleep(5)
    
        Take_picture.take_picture()
        
        game_matrix = TicTacToe_move.find_move(image_name,game_matrix,firstmove)
                    
        position = TicTacToe_game.computer(game_matrix,firstmove)
            
        #insert code to make robot move

        test_example.SetO(position[0],position[1])
        
        game = TicTacToe_game.wincheck(game_matrix)
            
    if firstmove == 1:

        print game_matrix
        
        position = TicTacToe_game.computer(game_matrix,firstmove)

        game = TicTacToe_game.wincheck(game_matrix)
        
        #insert code to make robot move
        test_example.SetX(position[0], position[1])

        #wait a little bit for the robot to finish and oponent to play

        time.sleep(5)
        Take_picture.take_picture()
        
        game_matrix = TicTacToe_move.find_move(image_name,game_matrix,firstmove)
        
    
            
