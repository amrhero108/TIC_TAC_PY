import os  # In order to clear Command window
import random  # In order to make computer play
from time import sleep  # In order to delay


class Player:  # Player class
    def __init__(self):
        self.systemBoard = []  # the player plays

    def set_Play(self, play):  # To store player plays
        if play not in self.systemBoard:
            self.systemBoard.append(play)

    def if_Win(self):  # Check winning
        if len(self.systemBoard) < 4:
            return False
        winning_combinations = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [1, 5, 9, 13],
                                [2, 6, 10, 14], [3, 7, 11, 15], [4, 8, 12, 16], [1, 6, 11, 16],
                                [4, 7, 10, 13]]  # Winning conditions
        for ls in winning_combinations:
            if all(play in self.systemBoard for play in ls):
                return True
        return False


class Computer(Player):  # Computer class for Computer Vs Plater
    def set_Play(self):
        x = random.choice(board)
        if x != 'X' and x != 'O':
            self.systemBoard.append(x)
            board[x - 1] = 'O'
        else:
            player2.set_Play()
        return x


def mainBoard(play=-1):
    global clock
    if 16 >= play > 0:
        if clock % 2 == 0:
            try:
                board.insert(board.index(play), 'X')
                board.remove(play)
                player1.set_Play(play)  # Use 'play' instead of 'plays'
                clock += 1
            except:
                print("Error Player 1 : This number is TAKEN")
        else:
            try:
                board.insert(board.index(play), 'O')
                board.remove(play)
                player2.set_Play(play)  # Use 'play' instead of 'plays'
                clock += 1
            except:
                print("Error Player 2 : This number is TAKEN")
    elif play == -1:
        player2.set_Play()
        clock += 1
    printBoard()


def printBoard():
    row_1 = f"{board[0]}\t|{board[1]}\t|{board[2]}\t|{board[3]}"
    row_2 = f"{board[4]}\t|{board[5]}\t|{board[6]}\t|{board[7]}"
    row_3 = f"{board[8]}\t|{board[9]}\t|{board[10]}\t|{board[11]}"
    row_4 = f"{board[12]}\t|{board[13]}\t|{board[14]}\t|{board[15]}"
    print(f"{row_1}\n{row_2}\n{row_3}\n{row_4}\n")


board = [i for i in range(1, 17)]
clock = 0
player1 = Player()
comp_player = input("Player 2 or Computer? (P/C): ").upper()
player2 = Computer() if comp_player == 'C' else Player()
printBoard()
while True:
    if clock % 2 == 0:
        plays = int(input("ENTER Player 1:"))
        os.system('cls')
        mainBoard(plays)
    else:
        if comp_player == 'C':
            os.system('cls')
            mainBoard()
        else:
            plays = int(input("ENTER Player 2:"))
            os.system('cls')
            mainBoard(plays)
    if clock >= 4:  # Winning condition can be checked after 4 moves
        if player1.if_Win():
            print("Player 1 wins!")
            break
        elif player2.if_Win():
            print("Player 2 wins!")
            break
        elif clock == 16:  # If no winner after 16 moves, it's a draw
            print("It's a draw!")
            break
sleep(10)