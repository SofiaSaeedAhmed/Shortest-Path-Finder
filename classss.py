import initializations
import pygame
from pygame.locals import *

class Node:
	def __init__(self, row, col, width, total_rows):
		self.row = row                                      # used for indexing of grid
		self.col = col                                      # used for indexing of grid
		self.x = row * width                                # position of each Node(cube) in grid
		self.y = col * width                                # position of each Node(cube) in grid
		self.color = initializations.white              # color of each Node(cube)
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows                        # tota no of rows
	

	def get_pos(self):
		return self.row, self.col                           # returns the index position

	def is_closed(self):
		return self.color == initializations.light_violet   # returns True if nodes are already visited(in closed set)

	def is_open(self):
		return self.color == initializations.offwhite      # returns True if nodes are in open set

	def is_barrier(self):
		return self.color == initializations.black          # returns True if nodes is a barrier

	def is_start(self):
		return self.color == initializations.orange         # returns True if nodes is a start node

	def is_end(self):
		return self.color == initializations.turquoise      # returns True if nodes is an end node

	def reset(self):
		self.color = initializations.white               # changes color back to white

	def make_start(self):
		self.color = initializations.orange                 # changes node color

	def make_closed(self):
		self.color = initializations.light_violet           # changes node color

	def make_open(self):
		self.color = initializations.navy_blue             # changes node color

	def make_barrier(self):
		self.color = initializations.black                  # changes node color

	def make_end(self):
		self.color = initializations.turquoise              # changes node color

	def make_path(self):
		self.color = initializations.purple                 # changes node color

	def makeVisiting(self):
		self.color = initializations.orange

	def makeVisited(self):
		self.color = initializations.light_green

	def isVisiting(self):
		return self.color == initializations.yellow

	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))         #draws the rectangle


	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

		#Add Diagonals
		if (self.col > 0 and self.row >0)  and not grid[self.row-1][self.col - 1].is_barrier(): # upper left
			self.neighbors.append(grid[self.row-1][self.col - 1])	

		if (self.row < self.total_rows-1 and self.col >0)  and not grid[self.row+1][self.col - 1].is_barrier(): # upper right
				self.neighbors.append(grid[self.row+1][self.col - 1])	

		if (self.col < self.total_rows-1 and self.row >0)  and not grid[self.row-1][self.col + 1].is_barrier(): # lower left
				self.neighbors.append(grid[self.row-1][self.col + 1])

		if (self.col < self.total_rows-1 and self.row <self.total_rows-1)  and not grid[self.row+1][self.col + 1].is_barrier(): # lower right
				self.neighbors.append(grid[self.row+1][self.col + 1])
				
	def __lt__(self, other):                                # comparing two nodes
		return False