import math
import pygame
from queue import PriorityQueue
import grid_drawing
import classss

def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()


def algorithm(draw, grid, start, end):
    visited = {node: False for row in grid for node in row}
    distance = {node: math.inf for row in grid for node in row}
    distance[start] = 0
    came_from = {}
    priority_queue = PriorityQueue()
    priority_queue.put((0, start))
    while not priority_queue.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        current = priority_queue.get()[1]

        if visited[current]:
            continue
        visited[current] = True
        if current == end:
            reconstruct_path(came_from, end, draw)
            return True
        if current != start:
            current.makeVisited()
        for neighbor in current.neighbors:
            weight = 1
            if distance[current] + weight < distance[neighbor]:
                came_from[neighbor] = current
                distance[neighbor] = distance[current] + weight
                priority_queue.put((distance[neighbor], neighbor))
            if neighbor != end and neighbor != start and not visited[neighbor]:
                neighbor.makeVisiting()
        draw()
    return False