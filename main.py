import pygame
import random
import math

pygame.font.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

BOARDSIZE = [10, 10]
BOARD = [[random.choices([0, 1, 2, 3, 4, 5], weights=[25, 20, 15, 10, 5, 1], k=1)[0] for x in range(BOARDSIZE[0])] for y in range(BOARDSIZE[1])]
CELLSIZE = 50
FONT = pygame.font.SysFont(pygame.font.get_default_font(), round(CELLSIZE / 2))
FONTHEIGHT = FONT.render("0", True, WHITE).get_height()

class Entity:
	def __init__(self, x, y):
		self.pos = [x, y]
	def draw(self, s: pygame.Surface):
		s.set_at(self.pos, BLACK)

class Ball(Entity):
	def __init__(self, x, y):
		self.pos = [x, y]
		self.v = [((random.random() * 2) - 1), ((random.random() * 2) - 1)]
	def draw(self, s: pygame.Surface):
		pygame.draw.circle(s, BLACK, self.pos, 5)
		self.pos[0] += self.v[0]
		self.pos[1] += self.v[1]
		# Collisions with screen edges
		if self.pos[0] <= 0:
			self.v[0] = abs(self.v[0]) # bounce off left side of screen
			self.pos[0] = 0
		elif self.pos[0] >= BOARDSIZE[0] * CELLSIZE:
			self.v[0] = -abs(self.v[0]) # bounce off right side of screen
			self.pos[0] = BOARDSIZE[0] * CELLSIZE - 1
		if self.pos[1] <= 0:
			self.v[1] = abs(self.v[1]) # bounce off top side of screen
			self.pos[1] = 0
		elif self.pos[1] >= BOARDSIZE[1] * CELLSIZE:
			self.v[1] = -abs(self.v[1]) # bounce off bottom side of screen
			self.pos[1] = BOARDSIZE[1] * CELLSIZE - 1
		pos = [0, 0]
		pos[0] = math.floor(self.pos[0] / CELLSIZE)
		pos[1] = math.floor(self.pos[1] / CELLSIZE)
		if not insideBoard(*pos):
			print('kaboom', *pos)
		if BOARD[pos[0]][pos[1]] > 0:
			BOARD[pos[0]][pos[1]] -= 1
			cellrect = pygame.Rect(pos[0] * CELLSIZE, pos[1] * CELLSIZE, CELLSIZE, CELLSIZE)
			# LEFT & RIGHT
			if self.pos[0] - 5 <= cellrect.left:
				self.v[0] = -self.v[0] # bounce off left side of brick
			elif self.pos[0] + 5 >= cellrect.right:
				self.v[0] = -self.v[0] # bounce off right side of brick
			# UP & DOWN
			if self.pos[1] - 5 <= cellrect.top:
				self.v[1] = -self.v[1] # bounce off top side of brick
			elif self.pos[1] + 5 >= cellrect.bottom:
				self.v[1] = -self.v[1] # bounce off bottom side of brick

def createBall(): entities.append(Ball(random.randint(0, BOARDSIZE[0] * CELLSIZE), random.randint(0, BOARDSIZE[1] * CELLSIZE)))
def insideBoard(x, y): return x >= 0 and x < BOARDSIZE[0] and y >= 0 and y < BOARDSIZE[1]

screen = pygame.display.set_mode((500, 500))
entities = []
createBall()
createBall()
createBall()
createBall()

c = pygame.time.Clock()
running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			pos = [*pygame.mouse.get_pos()]
			pos[0] = math.floor(pos[0] / CELLSIZE)
			pos[1] = math.floor(pos[1] / CELLSIZE)
			if BOARD[pos[0]][pos[1]] > 0:
				BOARD[pos[0]][pos[1]] -= 1
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
	# Entities
	for e in entities:
		e.draw(rendered_board)
	screen.blit(rendered_board, (0, 0))
	# Flip
	pygame.display.flip()
	c.tick(60)
