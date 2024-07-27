import pygame
import math
from queue import PriorityQueue
import initializations
import Algorithm_astar
import classss
import grid_drawing
import Algorithm_Dijkstra


import pygame
from pygame.locals import *
from pygame import mixer


mixer.init()
mixer.music.load('music1.wav')
mixer.music.play()

pygame.init()


def main(win, width):
	ROWS = 35
	grid = grid_drawing.make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		if pygame.mouse.get_pressed()[0]: # LEFT
			grid_drawing.draw(win, grid, ROWS, width)
			pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = grid_drawing.get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = grid_drawing.get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_1 or pygame.K_2 and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)
					# Self.Ask_user()
					if event.key == pygame.K_1:
						Algorithm_astar.algorithm(lambda: grid_drawing.draw(win, grid, ROWS, width), grid, start, end)
					elif event.key == pygame.K_2:
						Algorithm_Dijkstra.algorithm(lambda: grid_drawing.draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = grid_drawing.make_grid(ROWS, width)

	pygame.quit()

main(initializations.WIN, initializations.width)