import os
import sys
import pygame


def load_image(name, colorkey=None):
    fullname = os.path.join('', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


pygame.init()
size = width, height = 300, 300
screen = pygame.display.set_mode(size)

bomb_image = load_image("creature.png")
all_sprites = pygame.sprite.Group()
bomb = pygame.sprite.Sprite(all_sprites)
bomb.image = bomb_image
bomb.rect = bomb.image.get_rect()
bomb.rect.x = 0
bomb.rect.y = 0
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                bomb.rect.x -= 10
            elif event.key == pygame.K_RIGHT:
                bomb.rect.x += 10
            elif event.key == pygame.K_UP:
                bomb.rect.y -= 10
            elif event.key == pygame.K_DOWN:
                bomb.rect.y += 10

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()