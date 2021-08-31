import pygame
import pygame.event

pygame.init()

#screen size
screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))

#game title
pygame.display.set_caption('Vidwat Kukur')

#adding player and its location

class Warrior(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('img/player/Idle/0.png')
        self.image = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def draw(self):
        screen.blit(self.image, self.rect)


player = Warrior(200, 200, 2)
player2 = Warrior(400, 200, 2)

run = True
while run:

    player.draw()
    player2.draw()

    for event in pygame.event.get():
        # quit game
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()