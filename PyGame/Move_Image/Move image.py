import pygame
MAX_X = 600
MAX_Y = 200
game_over = False
bg_color = (10, 10, 10)

pygame.init()
screen = pygame.display.set_mode((MAX_X, MAX_Y))
pygame.display.set_caption('My first Pygame Game: ')

print(pygame.image.get_extended())

myimage = pygame.image.load('flag.jpg').convert()
myimage = pygame.transform.scale(myimage, (160,100))

x = MAX_X // 2
y = MAX_Y // 2

#------------main game loop

while game_over == False:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_over=True
            if event.key == pygame.K_LEFT:
                x -=20
            if event.key == pygame.K_RIGHT:
                x +=20
            if event.key == pygame.K_UP:
                y -=20
            if event.key == pygame.K_DOWN:
                y +=20
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos

    screen.fill (bg_color)
    screen.blit(myimage, (x,y))
    pygame.display.flip()

