#Tic tac toe

from random import randint
import os

ejecutar = True

pos = [1,2,3,4,5,6,7,8,9]
movimientos = 0

#---------------------------------------------------------------------------------------------
#Funciones

#Tablero

def ImpTab():
    print(f"""
            -----------------------------------
            |          |          |           |
            |     {pos[0]}    |     {pos[1]}    |     {pos[2]}     |   
            |          |          |           |
            -----------------------------------
            |          |          |           |
            |     {pos[3]}    |     {pos[4]}    |     {pos[5]}     |   
            |          |          |           |
            -----------------------------------
            |          |          |           |
            |     {pos[6]}    |     {pos[7]}    |     {pos[8]}     |   
            |          |          |           |
            -----------------------------------
    """)

def Jugador():

    global turno,movimientos
    ok = False

    while ok == False:
        p = int(input('Ingrese su proxima posición:'))

        if p-1 >= 0 and p-1 <= 8:
            if pos[p-1] == 'X' or pos[p-1] == 'O':
                print('\nPosición no disponible, seleccione una nueva posición')
            else:
                pos[p-1] = 'X'
                movimientos = movimientos + 1
                ok = True
                turno = 1
        else:
            print('\nPosición invalida')

def pc():

    global turno,movimientos
    ok = False

    while ok == False:
        p = randint(0,8)
        if pos[p] != 'X' and pos[p] != 'O':
            pos[p] = 'O'
            movimientos = movimientos + 1
            ok = True
            turno = 0

def Revisar():

    global ejecutar

#Ganaste

    if pos[0] == 'X' and pos[1] == 'X' and pos[2] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False
    elif pos[3] == 'X' and pos[4] == 'X' and pos[5] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False
    elif pos[6] == 'X' and pos[7] == 'X' and pos[8] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False

    elif pos[0] == 'X' and pos[3] == 'X' and pos[6] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False
    elif pos[1] == 'X' and pos[4] == 'X' and pos[7] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False
    elif pos[2] == 'X' and pos[5] == 'X' and pos[8] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False

    elif pos[0] == 'X' and pos[4] == 'X' and pos[8] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False
    elif pos[2] == 'X' and pos[4] == 'X' and pos[6] == 'X':
        print('\nHaz ganado, felicidades\n')
        ejecutar = False


#Perdiste

    elif pos[0] == 'O' and pos[1] == 'O' and pos[2] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False
    elif pos[3] == 'O' and pos[4] == 'O' and pos[5] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False
    elif pos[6] == 'O' and pos[7] == 'O' and pos[8] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False

    elif pos[0] == 'O' and pos[3] == 'O' and pos[6] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False
    elif pos[1] == 'O' and pos[4] == 'O' and pos[7] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False
    elif pos[2] == 'O' and pos[5] == 'O' and pos[8] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False

    elif pos[0] == 'O' and pos[4] == 'O' and pos[8] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False
    elif pos[2] == 'O' and pos[4] == 'O' and pos[6] == 'O':
        print('\nHaz perdido\n')
        ejecutar = False


#Empate

    if movimientos == 9:
        print('\nNadie ha ganado esta partida\n')
        ejecutar = False

#Reiniciar

def Reiniciar():
    global pos,movimientos,ejecutar

    pos = [1,2,3,4,5,6,7,8,9]
    movimientos = 0
    ejecutar = True


#---------------------------------------------------------------------------------------------

turno = 0

while ejecutar:

    os.system('clear')
    
    print('\n----------------------------------------------------------\n               TIC TAC TOE/GATO/TRES EN RAYA\n----------------------------------------------------------')

    #Imprimir tablero
    ImpTab()

    #Turnos
    if turno == 0:
        Jugador()
    else:
        pc()

    ImpTab()

    #Revisar tablero
    Revisar()

    if ejecutar == False:
        #print(menu)
        op = int(input('\n1)-Jugar de nuevo\n2)-Salir\n'))
        if op == 1:
            Reiniciar()










