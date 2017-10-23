import random
import numpy as np

def wincheck(matrix_test):
    saveX = np.zeros((3,3))
    saveO = np.zeros((3,3))
    for i in xrange(3):
        for j in xrange(3):
            if matrix_test[i][j] == 1:
                saveX[i][j] = 1
            if matrix_test[i][j] == 0:
                saveO[i][j] = 1
                    
    saveX_hor = np.zeros(3)
    saveX_ver = np.zeros(3)
    saveO_hor = np.zeros(3)
    saveO_ver = np.zeros(3)
    saveX_diag = np.zeros(2)
    saveO_diag = np.zeros(2)
    for i in xrange(3):
        for j in xrange(3):
            saveX_hor[i] += saveX[i][j]
            saveX_ver[i] += saveX[j][i]
            saveO_hor[i] += saveO[i][j]
            saveO_ver[i] += saveO[j][i]
        saveX_diag[0] += saveX[i][i]
        saveX_diag[1] += saveX[i][2-i]
        saveO_diag[0] += saveO[i][i]
        saveO_diag[1] += saveO[i][2-i]
    
    player0 = True
    player1 = True
    tie = False
    check = 0
    
    if (saveX_hor[0]+saveO_hor[0]==3 and saveX_hor[1]+saveO_hor[1]==3 and saveX_hor[2]+saveO_hor[2]==3):
        tie = True
    
    for i in xrange(3):
        if saveX_hor[i] == 3:
            player1 = False
            break
        if saveX_ver[i] == 3:
            player1 = False
            break
        if saveO_hor[i] == 3:
            player0 = False
            break
        if saveO_ver[i] == 3:
            player0 = False
            break
    for i in xrange(2):
        if saveX_diag[i] == 3:
            player1 = False
            break
        if saveO_diag[i] == 3:
            player0 = False
            break
    
    if player1 == False:
        check = 1
    if player0 == False:
        check = 2
    if (tie == True and player1 == True and player0 == True):
        check = 3
        
    return check    
        
def formerinput_pc(matrix_test,i,j):
    if matrix_test[i][j]==5:
        available =True
    else:
        available = False
    return available

def max_position(array):  
    maximum = 0
    position = np.zeros(2,dtype = int)
    for i in xrange(3):
        for j in xrange(3):
            if array[i][j] > maximum:
                maximum = array[i][j]
                position[0] = i
                position[1] = j
    return position
    

def move_picker(score,max_loops,firstmove):
    player1 = np.zeros((3,3))
    player0 = np.zeros((3,3))
    best = np.zeros(2,dtype=int)
    for i in xrange(max_loops):
        if score[i][2] == 1:
            player1[score[i][0]][score[i][1]] += 3
            player0[score[i][0]][score[i][1]] -= 1
        if score[i][2] == 2:
            player1[score[i][0]][score[i][1]] -= 1
            player0[score[i][0]][score[i][1]] += 3
        if score[i][2] == 3:
            player1[score[i][0]][score[i][1]] += 1
            player0[score[i][0]][score[i][1]] += 1
    if firstmove == 0:
        best = max_position(player0)
    if firstmove == 1:
        best = max_position(player1)
    return best
    
def computer(matrix,firstmove):
    counter = 0
    max_loops = 1000    
    score = np.zeros((max_loops,3),dtype = int)
    matrix_test = np.array(([5,5,5],[5,5,5],[5,5,5]))
    while(counter<max_loops):
        for i in xrange(3):
            for j in xrange(3):
                matrix_test[i][j] = matrix[i][j]
        winner = 0
        first_time = 0
        while winner == 0:
            if winner == 0:
                available = False
                while available == False:
                    i = random.randint(0,2)
                    j = random.randint(0,2)
                    available = formerinput_pc(matrix_test,i,j)
                matrix_test[i][j] = firstmove
                if first_time == 0:
                    score[counter][0] = i
                    score[counter][1] = j
            winner = wincheck(matrix_test)
            if winner == 0:
                available = False
                while available == False:
                    i = random.randint(0,2)
                    j = random.randint(0,2)
                    available = formerinput_pc(matrix_test,i,j)
                matrix_test[i][j] = abs(firstmove-1)
            winner = wincheck(matrix_test)
            first_time += 1
        score[counter][2] = winner
        counter += 1

    nextmove = move_picker(score,max_loops,firstmove)
    matrix[nextmove[0]][nextmove[1]] = firstmove
    return nextmove

    
