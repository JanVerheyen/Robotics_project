import random
import numpy as np


def wincheck(matrix):
    saveX = np.zeros((3,3))
    saveO = np.zeros((3,3))
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 1:
                saveX[i][j] = 1
            if matrix[i][j] == 0:
                saveO[i][j] = 1
                    
    saveX_hor = np.zeros(3)
    saveX_ver = np.zeros(3)
    saveO_hor = np.zeros(3)
    saveO_ver = np.zeros(3)
    saveX_diag = np.zeros(2)
    saveO_diag = np.zeros(2)
    for i in range(3):
        for j in range(3):
            saveX_hor[i] += saveX[i][j]
            saveX_ver[i] += saveX[j][i]
            saveO_hor[i] += saveO[i][j]
            saveO_ver[i] += saveO[j][i]
            saveX_diag[0] = saveX[j][j]
            saveX_diag[1] = saveX[j][2-j]
            saveO_diag[0] = saveO[j][j]
            saveO_diag[1] = saveO[j][2-j]
    
    pc = True
    player = True
    tie = False
    check = 0
    
    if(saveX_hor[0]+saveO_hor[0])==3 and (saveX_hor[1]+saveO_hor[1])==3 and(saveX_hor[2]+saveO_hor[2])==3:
        tie = True
    
    for i in range(3):
        if saveX_hor[i] == 3:
            player = False
            break
        if saveX_ver[i] == 3:
            player = False
            break
        if saveO_hor[i] == 3:
            player = False
            break
        if saveO_ver[i] == 3:
            player = False
            break
    for i in range(2):
        if saveX_diag[i] == 3:
            player = False
            break
        if saveO_diag[i] == 3:
            player = False
            break
    if player == False:
        check = 1
    if pc == False:
        check = 2
    if tie == True and player == True and pc == True:
        check =3
    
    return check
        
        
def formerinput_pc(matrix,i,j):
    available = False
    if matrix[i][j]==5:
        available =True
    return available

def max_position(array):  
    maximum = 0
    position = np.zeros(2)
    for i in range(3):
        for j in range(3):
            if array[i][j] > maximum:
                maximum = array[i][j]
                position[0] = i
                position[1] = j
    return position
    

def move_picker(score,max_loops):
    player = np.zeros((3,3))
    computer = np.zeros((3,3))
    best = np.zeros(2)
    for i in range(max_loops):
        if score[i][2] == 1:
            player[score[i][0]][score[i][1]] += 3
            computer[score[i][0]][score[i][1]] += -1
            break
        if score[i][2] == 2:
            player[score[i][0]][score[i][1]] += -1
            computer[score[i][0]][score[i][1]] += 3
            break
        if score[i][2] == 3:
            player[score[i][0]][score[i][1]] += 1
            computer[score[i][0]][score[i][1]] += 1
            break
    best = max_position(computer)
    
def computer(matrix):
    counter = 0
    max_loops = 10    
    score = np.empty((max_loops,3))    
    
    while(counter<max_loops):
        matrix_test = matrix
        winner = 0
        first_time = 0
        while winner == 0:
            if winner == 0:
                available = False
                while available == False:
                    i = random.randint(0,2)
                    j = random.randint(0,2)
                    available = formerinput_pc(matrix_test,i,j)
                matrix_test[i][j] = 0
                if first_time == 0:
                    score[counter][0] = i
                    score[counter][1] = j
            if winner == 0:
                available=False
                while available ==False:
                    i = random.randint(0,2)
                    j = random.randint(0,2)
                    print i
                    available = formerinput_pc(matrix_test,i,j)
                matrix_test[i][j] = 1
            winner = wincheck(matrix_test)
            first_time += 1
        score[counter][2] = winner
        counter += 1
        
    nextmove = move_picker(score,max_loops)
    matrix[nextmove[0]][nextmove[1]] = 0
    print matrix
            