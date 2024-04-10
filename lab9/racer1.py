import pygame, sys
import random, time
from pygame.locals import *
import os

pygame.init()
FramePerSec = pygame.time.Clock()
background = pygame.image.load("lab8/images/AnimatedStreet.png")        #Initializing pygame, loading up the background and declaring frames(FPS)

BLACK = pygame.Color(0, 0, 0)         # Black
WHITE = pygame.Color(255, 255, 255)   # White
BLUE = pygame.Color(0, 0, 255)   # Blue
RED = pygame.Color(255, 0, 0)       # Red
GREY = pygame.Color(128, 128, 128)    #Grey

#Variables
FPS = 60
SPEED = 4
WIDTH = 400
HEIGHT = 600 
SCORE = 0
COINS = 0
COINSPEED = 4

screen = pygame.display.set_mode((400, 600))
screen.fill(WHITE)                                                      #Setting up a white screen with the caption 
pygame.display.set_caption("Gran Turismo")            

#Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

#Objects

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(40, WIDTH-40),0) 
 
      def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)
 
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab8/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def move(self):
        pressed_keys = pygame.key.get_pressed()
         
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image_orig = pygame.image.load("lab8/images/goldcoin.png")
        self.image = pygame.transform.scale(self.image_orig, (30, 30))  # Resize the image to 30x30
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)
 
    def respawn(self):
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
    def move(self):
        self.rect.move_ip(0, COINSPEED)
        if (self.rect.top > 600):
            self.respawn()




#Initializing sprites
P1 = Player()
E1 = Enemy()   
C = Coin()

#Creating Sprite Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)
all_sprites.add(C)
objects = pygame.sprite.Group()
objects.add(C)

#New user event, not "quit"
INC_SPEED = pygame.USEREVENT + 1
enemy_speed_increment = 0.5
coins_for_speed_increase = 10
enemy_speed_increase_counter = 0
pygame.time.set_timer(INC_SPEED, 1000)



#Main loop
while True:     
    for event in pygame.event.get(): 
        if event.type == INC_SPEED:
            SPEED += 0.1

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
    screen.blit(background, (0,0))
    scores = font_small.render("SCORE: " + str(SCORE), True, BLACK)
    screen.blit(scores, (10,10))

    
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    
    coin_text = font_small.render("Coins: " + str(COINS), True, BLACK)
    # Blit coin counter text onto the screen
    screen.blit(coin_text, (10, 40))

    if pygame.sprite.spritecollideany(P1, objects):
        pygame.mixer.Sound("lab8/images/8bit-coin-sound-effect.mp3").play()
        COINS +=1
        entity.respawn()
        
    if pygame.sprite.spritecollideany(P1, enemies):

        pygame.mixer.Sound("lab8/images/crash.wav").play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()    

         
    pygame.display.update()
    FramePerSec.tick(FPS)
