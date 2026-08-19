import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,800))

image = pygame.image.load("images/plastic.png")
image = pygame.transform.scale(image, (100, 100))

image_names = []

class nonbio(pygame.sprite.Sprite):
    
    def __init__(self, x_pos, y_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x_pos, y_pos)


class bio(pygame.sprite.Sprite):
    
    def __innit__(self, x_pos, y_pos):
        



nonbiogroup = pygame.sprite.Group()

for i in range(10):
    plastic = nonbio(random.randint(150, 750),random.randint(150, 750))
    nonbiogroup.add(plastic)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    nonbiogroup.draw(screen)
    pygame.display.update()
