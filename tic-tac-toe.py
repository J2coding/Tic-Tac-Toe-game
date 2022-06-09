"""
Created by: Josephine Mueni 
Date: 9/6/2022
"""

import random

#A tic tac toe game in which two players seek in
# alternate turns to complete a row,column or
#a diagonal with either three x's or three o's 
# drawn in the spaces of a grid of nine squares.
def main(board):
	print('Welcome to Tic Tac Toe game')
	print(' | | ')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print(' | | ')
	print('--------------')
	print(' | | ')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print(' | | ')
	print('--------------')
	print(' | | ')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print(' | | ')
	print('/n')

def player_input():
	#Gets player inputs
	marker = ' '
	while marker != 'X'  and marker != 'O':
		marker = input('player 1, choose X or O: ').upper()
	if marker == 'X':
		return ('X', 'O')
	else:
		return ('O','X')

def who_goes_first():
	#randomly chooes who goes first
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'

def play_again():
	#ask if player wants to play again
	answer = input('would you like to play again? (y/n): ').lower()
	if answer == 'y':
		return True
	else:
		return False

def make_move(board,marker,position):
	#place maker on the board
	board[position] = marker

def check_win(board,marker):
	#check if player have won
	return ((board[7] == marker and board[8] == marker and board[9]== marker) or
	(board[4] == marker and board[5] == marker and board[6]== marker )or
	(board[1] == marker and board[2] == marker and board[3] == marker) or 
	(board[7] == marker and board[4] == marker and board[1]== marker)or 
	(board[8] == marker and board[5] == marker and board[2]== marker)or
	(board[9] == marker and board[6] == marker and board[3]== marker)or
	(board[7] == marker and board[5] == marker and board[3]== marker)or
	(board[9] == marker and board[5] == marker and board[1]== marker)) 

def get_board_copy(board):
	#make a duplicate of board list and return it
	dupBoard = []
	for i in board:
		dupBoard.append(i)
	return dupBoard

def space_free(board,position):
	#return true if the space is free
	return board[position] == ' '

def get_player_move(board):
	#let the player type in their move
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not space_free(board,int(move)):
		move = input('whats is your next move? (1-9): ') 
	return int(move)

def choose_random(board,movesList):
	#return a valid move from passed list on the first board
	# return none if their is invalid move
	possibleMoves = []
	for i in movesList:
		if space_free(board,i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0: 
		return random.choice(possibleMoves)
	else:
		return None

def computer_move(board,computerMarker):
	#computer will choose a random move from available moves
	if computerMarker =='X':
		playerMarker = 'O'

	else:
		playerMarker = 'X'

	for i in range(1,10):
		copy = get_board_copy(board)
		if space_free(copy,i):
			make_move(copy,computerMarker,i)
			if check_win(copy,computerMarker):
				return i
	move = choose_random(board,[1,3,7,9])
	if move != None:
		return move
	if space_free(board,5):
		return 5,
	return choose_random(board,[2,4,6,8])
	
def board_full(board):
	#return true is every space on the board has been taken
	for i in range(1,10):
		if space_free(board,i):
			return False
	return True

print('welcome to Tic Tac Toe')

while True:
	#reset the board
	theBoard = [' ']*10
	playerMarker,computerMarker = player_input()
	turn = who_goes_first()
	print(turn + 'will go first')
	gamePlaying = True


	while gamePlaying:
		if turn == 'player':
			#players turn
			main(theBoard)
			move = get_player_move(theBoard)

			make_move(theBoard,playerMarker,move)

			if check_win(theBoard,playerMarker):
				main(theBoard)
				print('Congratulation you have won the game!')

				gamePlaying = False
			else:
				if board_full(theBoard):
					main(theBoard)
					print('The game is tie')
					break
				else:
					turn = 'computer'
			
		else:
			#computers turn to play
			move = computer_move(theBoard,computerMarker)
			make_move(theBoard,computerMarker,move)
			if check_win(theBoard,computerMarker):
				main(theBoard)
				print('The computer has beaten! you lose')
				gamePlaying = False
			else:
				if board_full(theBoard):
					main(theBoard)
					print('the game is tie')
					break
				else:
					turn = 'player'
		
	if not play_again():
		break
	



			




		
	

	








	




		








	

	