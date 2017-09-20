#include <stdlib.h>
#include <conio.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>

int printmatrix(int matrix[3][3]){  //function to print matrix
    int i,j;
    char printmatrix[3][3];
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            if(matrix[i][j]==0){
                printmatrix[i][j] = 'O';
            }
            else if(matrix[i][j]==1){
                printmatrix[i][j]= 'X';
            }
            else{
                printmatrix[i][j] = ' ';
            }
        }
    }
    for(i=0;i<3;i++){
        printf("     %c | %c | %c \n",printmatrix[i][0],printmatrix[i][1],printmatrix[i][2]);
        printf("     ---------\n");
    }
}

int modeselect(char mode[3]){
    int mode_return;
    switch(mode[0]){
        case '1':
            mode_return=0;
            break;
        case 'l':
            mode_return=0;
            break;
        case 'p':
            mode_return=1;
            break;
        default:
            printf("Wrong format\n");
            mode_return=2;
    }
    return mode_return;

}

int play(char pos[3], int a[3][3]){    //input by player
    int x,y;
    bool format=true;
    switch(pos[0]){
        case '1':
            x = 0;
            break;
        case '2':
            x = 1;
            break;
        case '3':
            x = 2;
            break;
    }
    switch(pos[2]){
        case '1':
            y = 0;
            break;
        case '2':
            y = 1;
            break;
        case '3':
            y = 2;
            break;
    }
    a[x][y] = 1;
}

int play1(char pos[3], int a[3][3]){
    int x,y;
    bool format=true;
    switch(pos[0]){
        case '1':
            x = 0;
            break;
        case '2':
            x = 1;
            break;
        case '3':
            x = 2;
            break;
    }
    switch(pos[2]){
        case '1':
            y = 0;
            break;
        case '2':
            y = 1;
            break;
        case '3':
            y = 2;
            break;
    }
    a[x][y] = 0;
}

int formerinput_pc(int matrix[3][3],int i,int j){
    bool available;
    if(matrix[i][j]==5){
        available = true;
    }
    else{
        available = false;
    }
    return available;

}
int resetmatrix(int matrix[3][3]){       //reset the matrix
    int i,j;
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            matrix[i][j] = 5;
        }
    }
}

int wincheck(int matrix[3][3]){     //check if the player or the computer  has won
    int i,j;
    int saveX[3][3]={0},saveO[3][3]={0};
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            if (matrix[i][j]==1){
                saveX[i][j] = 1;
            }
            else if(matrix[i][j]==0){
                saveO[i][j] = 1;
            }
        }
    }
    int saveX_hor[3]={0},saveX_ver[3]={0},saveO_hor[3]={0},saveO_ver[3]={0};
    int saveX_diag[2]={0},saveO_diag[2]={0};
    for(j=0;j<3;j++){
        saveX_hor[0] += saveX[0][j];
        saveX_hor[1] += saveX[1][j];
        saveX_hor[2] += saveX[2][j];
        saveX_ver[0] += saveX[j][0];
        saveX_ver[1] += saveX[j][1];
        saveX_ver[2] += saveX[j][2];
        saveX_diag[0] += saveX[j][j];
        saveX_diag[1] += saveX[j][2-j];

        saveO_hor[0] += saveO[0][j];
        saveO_hor[1] += saveO[1][j];
        saveO_hor[2] += saveO[2][j];
        saveO_ver[0] += saveO[j][0];
        saveO_ver[1] += saveO[j][1];
        saveO_ver[2] += saveO[j][2];
        saveO_diag[0] += saveO[j][j];
        saveO_diag[1] += saveO[j][2-j];
    }
    bool pc=true,player=true,tie=false;
    int check = 0;

    if((saveX_hor[0]+saveO_hor[0])==3&&(saveX_hor[1]+saveO_hor[1])==3&&(saveX_hor[2]+saveO_hor[2])==3){
        tie = true;
    }

    for(j=0;j<3;j++){
        switch(saveX_hor[j]){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                player=false;
                break;
        }
        switch(saveX_ver[j]){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                player = false;
                break;
        }
        switch(saveO_hor[j]){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                pc = false;
                break;
        }
         switch(saveO_ver[j]){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                pc = false;
                break;
         }
    }
    for(j=0;j<2;j++){
        switch(saveX_diag[j]){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                player = false;
                break;
        }
        switch(saveO_diag[j]){
            case 0:
                break;
            case 1:
                break;
            case 2:
                break;
            case 3:
                pc = false;
                break;
        }
    }
    if(player==false){
        check = 1;
    }
    if(pc==false){
        check = 2;
    }
    if(tie==true&&player==true&&pc==true){
        check = 3;
    }
    return check;
}

int charactercheck(char position[3],bool format){ //check if the input is correct
    switch(position[0]){
        case '1':
            format = true;
            break;
        case '2':
            format = true;
            break;
        case '3':
            format = true;
            break;
        default :
            printf("Format not supported,try again.\n");
            sleep(1);
            format = false;
    }
    switch(position[2]){
        case '1':
            format = true;
            break;
        case '2':
            format = true;
            break;
        case '3':
            format = true;
            break;
        default :
            printf("Format not supported,try again.\n");
            sleep(1);
            format = false;
    }
    return format;
}

int formerinput(char position[3],bool format,int matrix[3][3]){ //check if the spot is not yet taken
    int i,j;
    switch(position[0]){
        case '1':
            i = 0;
            break;
        case '2':
            i = 1;
            break;
        case '3':
            i = 2;
            break;
    }
    switch(position[2]){
        case '1':
            j = 0;
            break;
        case '2':
            j = 1;
            break;
        case '3':
            j = 2;
            break;
    }
    if(format==true){
        if(matrix[i][j]==1||matrix[i][j]==0){
            format = false;
            printf("This spot is already taken!\n");
        }
        else{
            format = true;
        }
    }
    return format;
}

int max_position(int array[3][3],int p){
    int i,j,max = 0;
    int position[2];
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            if(array[i][j]>max){
                max = array[i][j];
                position[0]=i;
                position[1]=j;
            }
        }
    }
    return position[p];
}

int move_picker(int score[][3],int max_loops,int p){
    int i,player[3][3],computer[3][3];
    int best[2];
    for(i=0;i<max_loops;i++){
        switch(score[i][2]){
            case 1:
                player[score[i][0]][score[i][1]]+= 3;
                computer[score[i][0]][score[i][1]]-= 1;
                break;
            case 2:
                computer[score[i][0]][score[i][1]]+= 3;
                player[score[i][0]][score[i][1]]-= 1;
                break;
            case 3:
                computer[score[i][0]][score[i][1]]+= 1;
                player[score[i][0]][score[i][1]]+= 1;
                break;
        }
    }
    best[0] = max_position(computer,0);
    best[1] = max_position(computer,1);
    return best[p];
}

int computer(int matrix[3][3]){  //input by computer
    int i,j,counter=0,winner,first_time;
    int max_loops=10000;
    int matrix_test[3][3], nextmove[2];
    int score[max_loops][3];
    bool available;
    //random generator
    srand((unsigned) time(NULL));
    while(counter<max_loops){
        for(i=0;i<3;i++){
            for(j=0;j<3;j++){
                matrix_test[i][j] = matrix[i][j];
            }
        }
        winner=0;
        first_time=0;
        while(winner==0){
            if(winner==0){
                available = false;
                while(available==false){
                    i = rand() %3;
                    j = rand() %3;
                    available = formerinput_pc(matrix_test,i,j);
                }
                matrix_test[i][j] = 0;
                if(first_time==0){
                    score[counter][0] = i;
                    score[counter][1] = j;
                }
            }
            winner = wincheck(matrix_test);
            if(winner==0){
                available = false;
                while(available==false){
                    i = rand()%3;
                    j = rand()%3;
                    available = formerinput_pc(matrix_test,i,j);
                }
                matrix_test[i][j]=1;
            }
            winner = wincheck(matrix_test);
            first_time++;
        }
    score[counter][2] = winner;
    counter++;
    }

    nextmove[0] = move_picker(score,max_loops,0);
    nextmove[1] = move_picker(score,max_loops,1);

    matrix[nextmove[0]][nextmove[1]] = 0;

}

int matrix[3][3]={{5,5,5},{5,5,5},{5,5,5}};
int instructionmatrix[3][3]={{5,5,5},{5,5,5},{5,5,5}};
int instructionmatrix1[3][3]={{5,5,5},{5,5,5},{5,5,1}};

int main(){
    int input,start=1,mode;
    char position[3],mode_select[3];
    bool gameloop=true,format;
    while(gameloop==true){
        system("cls");
        printf("Press <ENTER> to start a new game.\n");
        input = getchar();
        if(input==10){
            start = 0;
        }
        mode = 2;
        while(mode==2){
            printf("Do you want to play 1v1 or against the computer?\n");
            printf("Type '1v1' or 'pc'\n");
            scanf("%s",mode_select);
            mode = modeselect(mode_select);
        }
        if(mode==0){
            while(start==0){
                system("cls");
                printf("TIC TAC TOE\n\n\n");
                printmatrix(matrix);
                printf("\n\n\n");
                format = false;
                while(format==false){
                    printf("Type '<x>,<y>' to put an X at that position.\n");
                    printf("Player 1, make a move:  ");
                    scanf("%s",position);
                    format = charactercheck(position,format);
                    format = formerinput(position,format,matrix);
                }
                play(position,matrix);
                start = wincheck(matrix);
                if(start == 1||start==2||start==3){
                    goto menu;
                }
                system("cls");
                printf("TIC TAC TOE\n\n\n");
                printmatrix(matrix);
                printf("\n\n\n");
                format = false;
                while(format==false){
                    printf("Type '<x>,<y>' to put an O at that position.\n");
                    printf("Player 2, make a move:  ");
                    scanf("%s",position);
                    format = charactercheck(position,format);
                    format = formerinput(position,format,matrix);
                }
                play1(position,matrix);
                start = wincheck(matrix);
                menu:
                while(start == 1||start==2||start==3){
                    system("cls");
                    printf("TIC TAC TOE\n\n\n");
                    printmatrix(matrix);
                    printf("\n\n\n");
                    if (start ==1){
                        printf("Player 1 won!\n");
                    }
                    else if(start == 2){
                        printf("Player 2 won!\n");
                    }
                    else if(start==3){
                        printf("It is a tie!\n");
                    }
                    resetmatrix(matrix);
                    printf("Press <n> to start a new game.\n");
                    printf("Press <q> to quit.\n");
                    fflush(stdin);
                    input = getchar();
                    if(input == 110){
                        resetmatrix(matrix);
                        start = 0;
                    }
                    else if(input == 113){
                        break;
                    }
                }
            }
        }
        else if (mode==1){
            while(start==0){
                system("cls");
                printf("TIC TAC TOE\n\n\n");
                printmatrix(matrix);
                printf("\n\n\n");
                format = false;
                while(format==false){
                    printf("Type '<x>,<y>' to put an X at that position.\n");
                    printf("Make a move:  ");
                    scanf("%s",position);
                    format = charactercheck(position,format);
                    format = formerinput(position,format,matrix);
                }
                play(position,matrix);
                start = wincheck(matrix);
                if(start == 1||start==2||start==3){
                    goto menu2;
                }
                system("cls");
                printf("TIC TAC TOE\n\n\n");
                printmatrix(matrix);
                printf("\n\n\n");
                computer(matrix);
                start = wincheck(matrix);
                menu2:
                while(start == 1||start==2||start==3){
                    system("cls");
                    printf("TIC TAC TOE\n\n\n");
                    printmatrix(matrix);
                    printf("\n\n\n");
                    if (start ==1){
                        printf("Congratulations, you won!\n");
                    }
                    else if(start == 2){
                        printf("Oh dear, the computer won, better luck next time!\n");
                    }
                    else if(start==3){
                        printf("It is a tie!\n");
                    }
                    resetmatrix(matrix);
                    printf("Press <n> to start a new game.\n");
                    printf("Press <q> to quit.\n");
                    fflush(stdin);
                    input = getchar();
                    if(input == 110){
                        resetmatrix(matrix);
                        start = 0;
                    }
                    else if(input == 113){
                        break;
                    }
                }
            }
        }
    }
    return 0;

}
