import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARD = [[random.choices([0, 1], weights=[5, 1], k=1)[0] for x in range(10)] for y in range(10)]
CELLSIZE = 10

screen = pygame.display.set_mode((500, 500))

c = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	# Drawing
	screen.fill(WHITE)
	rendered_board = pygame.Surface((500, 500))
	rendered_board.fill(WHITE)
	for x in range(len(BOARD)):
		for y in range(len(BOARD[x])):
			cell = BOARD[x][y]
			cellrect = pygame.Rect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
			if cell > 0:
				pygame.draw.rect(rendered_board, BLACK, cellrect)
	screen.blit(rendered_board, (0, 0))
	# Flip
	pygame.display.flip()
	c.tick(60)
