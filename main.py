import pygame
import random
from tkinter import *
pygame.init()

class Player():
    #Player attributes
    player_img = pygame.image.load("spaceship.png")
    player_pos = [900,800]
    player_change = [0,0]
    player_speed = 10
    player_health = {0:True, 1:True, 2:True}
    player_state = True
    levels = [0,1,2]
    current_level = levels[0]

    #Bullet attributes
    bullet_img = pygame.image.load("bullet.png")
    bullet_pos = [600,800]
    bullet_change = [0,0]
    bullet_speed = 20
    bullet_state = True
    bullet_fire = False

    def create_hitbox(self):
        screen.blit(Player.player_img, (Player.player_pos[0],Player.player_pos[1]))
        hitbox = Player.player_img.get_rect(topleft = (Player.player_pos[0],Player.player_pos[1]))
        return hitbox
    
    def create_movement(self,event):
        self.event = event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Player.player_change[1] = -Player.player_speed
            if event.key == pygame.K_s:
                Player.player_change[1] = Player.player_speed
            if event.key == pygame.K_a:
                Player.player_change[0] = -Player.player_speed
            if event.key == pygame.K_d:
                Player.player_change[0] = Player.player_speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                Player.player_change[1] = 0
            if event.key == pygame.K_a or event.key == pygame.K_d:
                Player.player_change[0] = 0
    
    def movement(self):
        for i in range(2):
            Player.player_pos[i] += Player.player_change[i]

        # Boundary
        if Player.player_pos[0] < 0:
            Player.player_pos[0] = 0
        if Player.player_pos[0] > 1855:
            Player.player_pos[0] = 1855
        if Player.player_pos[1]  > 900:
            Player.player_pos[1] = 900
        if Player.player_pos[1] <700:
            Player.player_pos[1] = 700 

    def create_bullet(self,x,y):
        self.x = x
        self.y = y
        screen.blit(Player.bullet_img, (x+15,y))
        Player.bullet_state = False

    def shoot_bullet(self,event):
        self.event = event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if Player.bullet_state:
                    Player.bullet_pos[0] = Player.player_pos[0]
                    Player.bullet_pos[1] = Player.player_pos[1]
                    Player.bullet_change[1] = -Player.bullet_speed
                    Player.bullet_fire = True

    def bullet_reset(self):
        if Player.bullet_pos[1] < 0:
            Player.bullet_state = True
            Player.bullet_fire = False
            Player.bullet_pos[1] = 800
            
    def bullet_movement(self):
        if Player.bullet_fire:
            player.create_bullet(Player.bullet_pos[0],Player.bullet_pos[1])
            Player.bullet_pos[1] += Player.bullet_change[1]
            player.bullet_reset()

    def health(self):
        img_health = pygame.image.load("heart .png")
        img_no_health = pygame.image.load("black_heart .png")
        health_pos = [(130,20),(90,20),(50,20)]
        for i in Player.player_health.keys():
            if Player.player_health[i] == True:
                screen.blit(img_health, health_pos[i])
            else:
                screen.blit(img_no_health, health_pos[i])        
    
        if Player.player_health == 0:
            Player.player_state = False

class Enemy():
    pass

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))

if Player.current_level == Player.levels[0]:
    bg = pygame.image.load("background.jpg").convert()
bg_y = -1080

running = True
while running:
    screen.fill((255,255,255))

    # Scrolling Background
    bg_rel_y = bg_y % bg.get_rect().height
    screen.blit(bg, (0,bg_rel_y - bg.get_rect().height))
    if bg_rel_y < 1080:
        screen.blit(bg, (0,bg_rel_y))
    bg_y += 2

    player = Player()
    if Player.player_state:
        player.create_hitbox()
        player.movement()
        player.health()
        player.bullet_movement()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.create_movement(event)
        player.shoot_bullet(event)

    clock.tick(60)
    pygame.display.update()

