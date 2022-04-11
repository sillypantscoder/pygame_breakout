import pygame
import random

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARDSIZE = [10, 10]
BOARD = [[random.choices([0, 1], weights=[5, 1], k=1)[0] for x in range(BOARDSIZE[0])] for y in range(BOARDSIZE[1])]
CELLSIZE = 50
FONT = pygame.font.SysFont(pygame.font.get_default_font(), round(CELLSIZE / 2))
FONTHEIGHT = FONT.render("0", True, WHITE).get_height()

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
	for x in range(BOARDSIZE[0]):
		for y in range(BOARDSIZE[1]):
			cell = BOARD[x][y]
			cellrect = pygame.Rect(x * CELLSIZE, y * CELLSIZE, CELLSIZE, CELLSIZE)
			if cell > 0:
				pygame.draw.rect(rendered_board, BLACK, cellrect, 0, 5)
				number = FONT.render(str(cell), True, WHITE)
				rendered_board.blit(number, (cellrect.centerx - (number.get_width() / 2), cellrect.centery - (number.get_height() / 2)))
	screen.blit(rendered_board, (0, 0))
	# Flip
	pygame.display.flip()
	c.tick(60)
