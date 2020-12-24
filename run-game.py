"""
info or whatever, authors? date?
all that stuff
"""

import pygame

pygame.init()

# Initial setup and global variables
WIN_WIDTH = 600
WIN_HEIGHT = 600
STAT_FONT = pygame.font.SysFont("Calibri", 50)
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pong")


class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def move(self, direction):
        if direction == 'UP':
            self.y += 1
        elif direction == 'DOWN':
            self.y -= 1

    # def get_rect(self):
    #     return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(WIN, (0, 255, 0), (self.x, self.y, self.width, self.height))


def draw_window(players):
    WIN.fill((0, 0, 0))

    for player in players:
        player.draw()

    pygame.display.update()


# Main game loop
player1 = Player(10, 10, 20, 60)
player_list = [player1]

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(10)
    draw_window(player_list)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        player1.move('UP')
    if keys[pygame.K_DOWN]:
        player1.move('DOWN')
