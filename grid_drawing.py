from turtle import width
import pygame
import initializations
import classss

grid = []										# nested list that hold all the cube/node
def make_grid(rows, width):							# plain white screen withy cube/node stored(which cannoit be visualized as of yet)
	gap = width // rows								# width of each cube(Node)
	for i in range(rows):
		grid.append([]) 							# first
		for j in range(rows):
			spot = classss.Node(i, j, gap, rows)
			grid[i].append(spot)					# appends each cube as a list left to right

	return grid



def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):                                                            	# to draw horizontal lines
		pygame.draw.line(win, initializations.black, (0, i * gap), (width, i * gap))  	# keeping y constant x is varied (two brackets represent points where we want the start line and the end line)
	for j in range(rows):														 		# to draw vertical lines
		pygame.draw.line(win, initializations.black, (j * gap, 0), (j * gap, width)) 	# keeping x constant y is varied (two brackets represent points where we want the start line and the end line


def draw(win, grid, rows, width):

	for row in grid:
		for spot in row:
			spot.draw(win)																# colouring each cube/node

	draw_grid(win, rows, width)															# calling the function to draw
	pygame.display.update()																# updating


def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col

# def clickWall(pos, state):
#     row = pos[0] // width
#     column = pos[1] // width
#     grid[row][column].wall = state
