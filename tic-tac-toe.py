"""
Created by: Josephine Mueni 
Date: 9/6/2022
"""
from operator import length_hint
import random
import re
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

def clear_input():
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
		return None:

def computer_move():





	




		








	

	