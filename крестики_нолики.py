#КРЕСТИКИ-НОЛИКИ

#основные переменные
x='X'
o='O'
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
board_desk='\t-------------\n\t| {0[0]} | {0[1]} | {0[2]} |\n\t-------------\n\t\
| {0[3]} | {0[4]} | {0[5]} |\n\t-------------\n\t| {0[6]} | {0[7]} | {0[8]} |\n\t-------------'




#кто ходит первым?
def players_input(symbol_1=input('\nКаким символом будет ходить игрок 1?: ').upper()):
    while True:
        if symbol_1==o or symbol_1==x:
            break
        else:
            symbol_1=input('\nКаким символом будет ходить игрок 1?: ').upper()
    print(f'\nИгрок 1 играет за "{symbol_1}".')
    if symbol_1=='O':
        symbol_2='X'
    elif symbol_1=='X':
        symbol_2='O'
    print(f'Игрок 2 играет за "{symbol_2}".')    
    return symbol_1, symbol_2

symb1,symb2=players_input()


def player_1_turn ():
    turn_str_1=input('\nХод игрока 1!\nВведите номер клетки: ')
    turn_1=int(turn_str_1)-1
    while True:
        if turn_1 in [0,1,2,3,4,5,6,7,8] and (board[turn_1] not in (symb1,symb2)):
            board[turn_1]=symb1
            break
        else:
            turn_str_1=input('\nНеправильное значение, игрок 1!\nВведите номер клетки: ')
            turn_1=int(turn_str_1)-1
    board_desk_1=board_desk.format(board)
    print(board_desk_1)
    return board



def player_2_turn ():
    turn_str_2=input('\nХод игрока 2!\nВведите номер клетки: ')
    turn_2=int(turn_str_2)-1
    while True:
        if turn_2 in [0,1,2,3,4,5,6,7,8] and (board[turn_2] not in (symb1,symb2)):
            board[turn_2]=symb2
            break
        else:
            turn_str_2=input('\nНеправильное значениеб игрок 2!\nВведите номер клетки: ')
            turn_2=int(turn_str_2)-1
    board_desk_2=board_desk.format(board)
    print(board_desk_2)
    return board

def play_again():
    answer=''
    while answer!='нет':
        answer=input('Хотите начать игру заново (ответ "да" или "нет")? ').lower()
        if answer=='да':
            global board
            board=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
            x_o_game()
        elif answer=='нет':
            print('Спасибо за игру!')
            return
    
        


def x_o_game():
    print(board)
    print('\t-------------\n\t| 1 | 2 | 3 |\n\t-------------\n\t\
| 4 | 5 | 6 |\n\t-------------\n\t| 7 | 8 | 9 |\n\t-------------')
    for i in range(1,6):
       
        player_1_turn()
        print(board)
        l1=[board[0],board[4],board[8]]
        l2=[board[2],board[4],board[6]]
        l3=[board[0],board[3],board[6]]
        l4=[board[1],board[4],board[7]]
        l5=[board[2],board[5],board[8]]
        l6=[board[0],board[1],board[2]] 
        l7=[board[3],board[4],board[5]]
        l8=[board[6],board[7],board[8]]

        lists=[l1,l2,l3,l4,l5,l6,l7,l8]
        win1=0
        win2=0
        
        for a in lists:
            if a == [symb1,symb1,symb1]:
                print('Поздравляем Игрока 1 с победой!')
                win1=1
                return win1

        #for a in lists:
        if (' ' not in board and win1==0 and win2==0):
            print('Ничья!')
            return
             
        player_2_turn()
        print(board)
        l1=[board[0],board[4],board[8]]
        l2=[board[2],board[4],board[6]]
        l3=[board[0],board[3],board[6]]
        l4=[board[1],board[4],board[7]]
        l5=[board[2],board[5],board[8]]
        l6=[board[0],board[1],board[2]] 
        l7=[board[3],board[4],board[5]]
        l8=[board[6],board[7],board[8]]

        lists=[l1,l2,l3,l4,l5,l6,l7,l8]
        for a in lists:   
            if a == [symb2,symb2,symb2]:
                print('Поздравляем Игрока 2 с победой!')
                win2=1
                return win2

       # if win1==0 and win2==0:

    
   # if board!=['1','2','3','4','5','6','7','8','9']
        
    """for a in lists:
            if a != [symb1,symb1,symb1] and a !=[symb2,symb2,symb2]:
                print('Ничья!')
                return"""
        
x_o_game()
play_again()