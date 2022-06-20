import pygame
import os
from sys import exit
pygame.mixer.init()

y = 500
VEL = 10

def main():
    pygame.init()
    screen = pygame.display.set_mode((1200,600))
    pygame.display.set_caption("Space Runner")
    clock = pygame.time.Clock()
    test_font = pygame.font.Font(None, 50)
    explode = pygame.mixer.Sound(os.path.join("assets/XWing explode.mp3"))
    bg_music = pygame.mixer.Sound("assets/Star Wars Theme.mp3")
    bg_music.play(loops = -1)


    background = pygame.image.load("assets/space.jpg").convert()
    text_surface = test_font.render("Star Wars", False, "Yellow")

    rock_surface = pygame.image.load("assets/space rock.png").convert_alpha()
    rock_surface = pygame.transform.scale(rock_surface, (100,100))
    rock_rect = rock_surface.get_rect(midtop = (1100,150))

    rock_surface2 = pygame.image.load("assets/space rock.png").convert_alpha()
    rock_surface2 = pygame.transform.scale(rock_surface2, (90,90))
    rock_rect2 = rock_surface2.get_rect(midright = (1100,500))

    rock_surface3 = pygame.image.load("assets/space rock.png").convert_alpha()
    rock_surface3 = pygame.transform.scale(rock_surface3, (80,80))
    rock_rect3 = rock_surface3.get_rect(midbottom = (1100,400))

    rock_surface4 = pygame.image.load("assets/space rock.png").convert_alpha()
    rock_surface4 = pygame.transform.scale(rock_surface4, (70,70))
    rock_rect4 = rock_surface4.get_rect(midleft = (1100,50))

    ship = pygame.image.load("assets/spaceship.png").convert_alpha()
    ship = pygame.transform.scale(ship, (180, 90))
    ship_rect = ship.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        userInput = pygame.key.get_pressed()
        if userInput [pygame.K_UP] and ship_rect.y - VEL > 0:
            ship_rect.y -= 10 
        if userInput [pygame.K_DOWN] and ship_rect.y + VEL < 525:
            ship_rect.y += 10


        screen.blit(background,(0,0))
        screen.blit(text_surface,(500,50))
        
        rock_rect.x -= 10
        if rock_rect.right <= 0: rock_rect.left = 1100
        screen.blit(rock_surface,rock_rect)
        
        rock_rect2.x -= 11
        if rock_rect2.right <= 0: rock_rect2.left = 1100
        screen.blit(rock_surface2,rock_rect2)
    
        rock_rect3.x -= 8
        if rock_rect3.right <= 0: rock_rect3.left = 1100
        screen.blit(rock_surface3,rock_rect3)
    
        rock_rect4.x -= 7
        if rock_rect4.right <= 0: rock_rect4.left = 1100
        screen.blit(rock_surface4,rock_rect4)
        
        screen.blit(ship, ship_rect)

        if ship_rect.colliderect(rock_rect):
            explode.play()
            pygame.time.delay(3000)
            main()
        if ship_rect.colliderect(rock_rect2):
            explode.play()
            pygame.time.delay(3000)
            main()
        if ship_rect.colliderect(rock_rect3):
            explode.play()
            pygame.time.delay(3000)
            main()
        if ship_rect.colliderect(rock_rect4):
            explode.play()
            pygame.time.delay(3000)
            main()
            

        
        pygame.display.update() 
        clock.tick(60)

main()

