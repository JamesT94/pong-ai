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


# The objects that we'll spawn 2 of to create the players. They take in the x/y coords and the width/height
# when you create them later on in the main game loop. This is like the 'recipe' for a player.
class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # The method we call when we want to move the player
    def move(self, direction):
        if direction == 'UP':
            self.y -= 1
        elif direction == 'DOWN':
            self.y += 1

    # The method we call to draw the rectangle of the player on to the screen
    def draw(self):
        pygame.draw.rect(WIN, (0, 255, 0), (self.x, self.y, self.width, self.height))


# This function sits outside of the Player class. We call this once per frame to draw the whole scene
def draw_window(players):
    # First it fills the screen with black for the background and to erase the previous frame
    WIN.fill((0, 0, 0))

    # Then for each player we call upon their draw method (see above) to draw their rectangle
    for player in players:
        player.draw()

    pygame.display.update()


# Main game loop
player1 = Player(0, 10, 20, 60)
player2 = Player(580, 100, 20, 60)
player_list = [player1, player2]

clock = pygame.time.Clock()

run = True
while run:
    clock.tick(60)  # The number represents the amount of frames per second. More means the game runs faster.
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
    if keys[pygame.K_w]:
        player2.move('UP')
    if keys[pygame.K_s]:
        player2.move('DOWN')
