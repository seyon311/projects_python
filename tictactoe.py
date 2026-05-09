import random

board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

available_moves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def printboard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def checkwin(player, board):
    if (board['7'] == board['8'] == board['9'] == player):
        return True
    elif (board['4'] == board['5'] == board['6'] == player):
        return True
    elif (board['1'] == board['2'] == board['3'] == player):
        return True
    elif (board['7'] == board['4'] == board['1'] == player):
        return True
    elif (board['8'] == board['5'] == board['2'] == player):
        return True
    elif (board['9'] == board['6'] == board['3'] == player):
        return True
    elif (board['7'] == board['5'] == board['3'] == player):
        return True
    elif (board['9'] == board['5'] == board['1'] == player):
        return True
    else:
        return False
          

def startgame():
    while True:
        who = input("Do you want to be X or O? ").upper()
        if who in ['X', 'O']:
            break
        print("Invalid input. Please choose X or O.")    

    player = who
    if player == 'X':
        computer = 'O'
    else:
        computer = 'X'

    print("The board is numbered as follows:")
    print("7|8|9\n-+-+-\n4|5|6\n-+-+-\n1|2|3")

    print(f"You are {player}. Computer is {computer}.")


    if player == 'X':
        for i in range(9):
            move = input("Enter your move (1-9): ")
            if available_moves == []:
                    print("\nIt's a tie!")
                    break
            if move in available_moves:
                board[move] = player
                available_moves.remove(move)
                print('\n')
                printboard(board)
                if checkwin(player, board):
                    print("\nCongratulations! You win!")
                    break
                if available_moves == []:
                    print("\nIt's a tie!")
                    break
                computer_move = random.choice(available_moves)
                available_moves.remove(computer_move)
                board[computer_move] = computer
                print(f"Computer chooses {computer_move}.")
                print('\n')
                printboard(board)
                if checkwin(computer, board):
                    print("\nComputer wins! Better luck next time.")
                    break
                
    else:
        for i in range(9):
            if available_moves == []:
                    print("\nIt's a tie!")
                    break
            computer_move = random.choice(available_moves)
            available_moves.remove(computer_move)
            board[computer_move] = computer
            print(f"Computer chooses {computer_move}.")
            print('\n')
            printboard(board)
            if checkwin(computer, board):
                print("\nComputer wins! Better luck next time.")
                break
            if available_moves == []:
                    print("\nIt's a tie!")
                    break
            move = input("Enter your move (1-9): ")
            if move in available_moves:
                board[move] = player
                available_moves.remove(move)
                print('\n')
                printboard(board)
                if checkwin(player, board):
                    print("\nCongratulations! You win!")
                    break
                               
startgame()