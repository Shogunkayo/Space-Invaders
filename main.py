import pygame
import random
pygame.init()

class Player:
    #Player attributes
    player_img = pygame.image.load("spaceship.png")
    player_pos = [900,800]
    player_change = [0,0]
    player_speed = 10
    player_health = {0:True, 1:True, 2:True}
    player_state = True
    current_level = 0
    score = 0
    hitcount = 0

    #Bullet attributes
    bullet_img = pygame.image.load("bullet.png")
    bullet_pos = [0,800]
    bullet_change = [0,0]
    bullet_speed = 20
    bullet_state = "ready"
    bullet_fire = False

    def create_hitbox(self):
        # Draws player on screen
        # Creates rect object around the player image
        screen.blit(Player.player_img, (Player.player_pos[0],Player.player_pos[1]))
        hitbox = Player.player_img.get_rect(topleft = (Player.player_pos[0],Player.player_pos[1]))
        return hitbox
    
    def create_player_movement(self,event):
        # Gets input
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
        # Uses input and moves the player
        for i in range(2):
            Player.player_pos[i] += Player.player_change[i]

        # Boundary for the player
        if Player.player_pos[0] < 0:
            Player.player_pos[0] = 0
        if Player.player_pos[0] > 1855:
            Player.player_pos[0] = 1855
        if Player.player_pos[1]  > 900:
            Player.player_pos[1] = 900
        if Player.player_pos[1] <750:
            Player.player_pos[1] = 750 

    def create_bullet(self,x,y):
        # Draws bullet on screen
        self.x = x
        self.y = y
        screen.blit(Player.bullet_img, (x+15,y))
        Player.bullet_state = "not ready"

    def bullet_hitbox(self):
        # Creates rect object around bullet image
        hitbox = Player.bullet_img.get_rect(topleft=(Player.bullet_pos[0],Player.bullet_pos[1]))
        return hitbox

    def shoot_bullet(self,event):
        # Takes input and makes bullet ready to move
        self.event = event
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if Player.bullet_state == "ready":
                    Player.bullet_pos[0] = Player.player_pos[0]
                    Player.bullet_pos[1] = Player.player_pos[1]
                    Player.bullet_change[1] = -Player.bullet_speed
                    Player.bullet_fire = True

    def bullet_reset(self):
        # Resets position of bullet if it goes out of screen
        if Player.bullet_pos[1] < 0:
            Player.bullet_state = "ready"
            Player.bullet_fire = False
            Player.bullet_pos[1] = 800
            
    def bullet_movement(self):
        if Player.bullet_fire:
            player.create_bullet(Player.bullet_pos[0],Player.bullet_pos[1])
            Player.bullet_pos[1] += Player.bullet_change[1]
            player.bullet_reset()

    def health(self):
        # Draw hearts
        img_health = pygame.image.load("heart .png")
        img_no_health = pygame.image.load("black_heart .png")
        health_pos = [(130,975),(90,975),(50,975)]
        for i in Player.player_health.keys():
            if Player.player_health[i] == True:
                screen.blit(img_health, health_pos[i])
            else:
                screen.blit(img_no_health, health_pos[i])        
    '''
    def reduce_health(self):
        # Detect if boss hit player
        if EnemyBoss.mechanic.bullet_fired:
            for i in range(4):
                if player_hitbox.colliderect(boss.mechanic.bullet_hitboxes[i]):
                    boss.mechanic.bullet_pos[i] = [-1000,200] 
                    player.hitcount += 1

        # Reduce player health
        
        if player.hitcount > 16:
            for i in Player.player_health.keys():
                if Player.player_health[i]:
                    Player.player_health[i] = False
                    break

            print("player hit")
            print(Player.player_health)
            player.hitcount = 0

        # End game if player dies
        if Player.player_health[2] == 0:
            Player.player_state = False
        '''
class EnemyBoss:
    # Boss Attributes
    enemy_img = pygame.image.load("alienboss.png")
    enemy_pos = [600,-1000]
    enemy_speed = 4
    enemy_change = [enemy_speed,0]
    enemy_health = {0:True,1:True,2:True,3:True,4:True,5:True,6:True,7: True,8: True,9:True}
    enemy_state = "not spawned"
    hitcount = 0
    mechanic = None
    
    def spawn(self):
        screen.blit(EnemyBoss.enemy_img, (EnemyBoss.enemy_pos[0],EnemyBoss.enemy_pos[1]))
        if EnemyBoss.enemy_pos[1] < -200:
            EnemyBoss.enemy_change[1] = 5
        else:
            EnemyBoss.enemy_change[1] = 0
            EnemyBoss.enemy_state = "moving" 
        EnemyBoss.enemy_pos[1] += EnemyBoss.enemy_change[1]
        EnemyBoss.movement()

    def create_hitbox(self):
        hitbox = EnemyBoss.enemy_img.get_rect(topleft=(EnemyBoss.enemy_pos[0], EnemyBoss.enemy_pos[1]))
        return hitbox

    def movement():
        if EnemyBoss.enemy_state == "moving":
            EnemyBoss.enemy_pos[0] += EnemyBoss.enemy_change[0]
            if EnemyBoss.enemy_pos[0] < 0:
                EnemyBoss.enemy_change[0] = EnemyBoss.enemy_speed
                EnemyBoss.enemy_pos[0] += EnemyBoss.enemy_change[0]
            elif EnemyBoss.enemy_pos[0] > 1410:
                EnemyBoss.enemy_change[0] = -EnemyBoss.enemy_speed
                EnemyBoss.enemy_pos[0] += EnemyBoss.enemy_change[0]

    def health(self):
        #Choose mechanic based on health of boss
        if EnemyBoss.enemy_health[2]:
            EnemyBoss.mechanic = ThirdMechanic()
        elif EnemyBoss.enemy_health[5]:
            EnemyBoss.mechanic = SecondMechanic()
        elif EnemyBoss.enemy_health[9]:
            EnemyBoss.mechanic = ThirdMechanic()
        else:
            EnemyBoss.enemy_state = "dead"

        # Detect if player hit boss
        bullet_hit = player.bullet_hitbox()
        boss_hit = boss.create_hitbox()
        if boss_hit.colliderect(bullet_hit):
            player.bullet_reset()
            EnemyBoss.hitcount += 1
        
        # Reduce boss health
        if EnemyBoss.hitcount == 80:
            for i in EnemyBoss.enemy_health.keys():
                if EnemyBoss.enemy_health[i] == True:
                    EnemyBoss.enemy_health[i] = False
                    break

                print("Enemy health reduced")
            print(EnemyBoss.enemy_health)

            EnemyBoss.hitcount = 0        

class FirstMechanic:
    bullet_img = pygame.image.load("laser.png") 
    bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
    bullet_hitboxes = [None,None,None,None]
    bullet_speed = 15
    bullet_change = 0
    bullet_state = "ready"
    bullet_fired = True
    bullet_fire_duration = 8000
    bullet_cooldown_vary = 0
    bullet_cooldown_const = 0
    bullet_cooldown_delay = 3000
    x = [85,185,315,415]

    def create_hitbox(self):
        if FirstMechanic.bullet_fired:
            for i in range(4):
                FirstMechanic.bullet_hitboxes[i] = FirstMechanic.bullet_img.get_rect(topleft = (FirstMechanic.bullet_pos[i][0]+FirstMechanic.x[i],FirstMechanic.bullet_pos[i][1]))
            #pygame.draw.rect(screen, (255,0,0), FirstMechanic.bullet_hitboxes[i])
        
    def draw_bullet(self):
        if FirstMechanic.bullet_fired:
            for i in range(4):
                screen.blit(FirstMechanic.bullet_img, (FirstMechanic.bullet_pos[i][0] + FirstMechanic.x[i],FirstMechanic.bullet_pos[i][1]))
                
        FirstMechanic.bullet_state = "not ready"

    def bullet_movement(self):
        pass

    def shoot_bullet(self):
        for i in range(4):
            FirstMechanic.bullet_pos[i][0] = EnemyBoss.enemy_pos[0]

    def bullet_reset():
        pass
            
    def cooldown(self):
        FirstMechanic.bullet_cooldown_vary = pygame.time.get_ticks()
        if FirstMechanic.bullet_cooldown_vary - FirstMechanic.bullet_cooldown_const > FirstMechanic.bullet_cooldown_delay:
            FirstMechanic.bullet_fired = True
            # Duration to fire bullet
            if FirstMechanic.bullet_cooldown_vary - FirstMechanic.bullet_cooldown_const > FirstMechanic.bullet_cooldown_delay + FirstMechanic.bullet_fire_duration:
                FirstMechanic.bullet_cooldown_const = pygame.time.get_ticks()

        # Reset Bullet  
        else:
            FirstMechanic.bullet_fired = False

class SecondMechanic:
    bullet_img = pygame.image.load("boss1.png") 
    bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
    bullet_hitboxes = [None,None,None,None]
    bullet_speed = 15
    bullet_change = 0
    bullet_state = "ready"
    bullet_fired = False
    bullet_fire_duration = 4800
    bullet_cooldown_vary = 0
    bullet_cooldown_const = 0
    bullet_cooldown_delay = 2000
    x = [50,150,290,390]

    def create_hitbox(self):
        for i in range(4):
            SecondMechanic.bullet_hitboxes[i] = SecondMechanic.bullet_img.get_rect(topleft = (SecondMechanic.bullet_pos[i][0]+SecondMechanic.x[i],SecondMechanic.bullet_pos[i][1]))
            #dpygame.draw.rect(screen, (255,0,0), SecondMechanic.bullet_hitboxes[i])
    
    def draw_bullet(self):
        if SecondMechanic.bullet_fired:
            for i in range(4):
                screen.blit(SecondMechanic.bullet_img, (SecondMechanic.bullet_pos[i][0] + SecondMechanic.x[i],SecondMechanic.bullet_pos[i][1]))
                
        SecondMechanic.bullet_state = "not ready"

    def bullet_movement(self):
        if SecondMechanic.bullet_fired:
            SecondMechanic.bullet_change = SecondMechanic.bullet_speed
        else:
            SecondMechanic.bullet_change = 0
        for i in range(4):
            SecondMechanic.bullet_pos[i][1] += SecondMechanic.bullet_change

        SecondMechanic.bullet_reset()

    def shoot_bullet(self):
        if SecondMechanic.bullet_state == "ready":
            SecondMechanic.bullet_fired = True
            for i in range(4):
                SecondMechanic.bullet_pos[i][0] = EnemyBoss.enemy_pos[0]

    def bullet_reset():
        for i in range(4):
            if SecondMechanic.bullet_pos[i][1] > 1100:
                SecondMechanic.bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
                SecondMechanic.bullet_state = "ready"
                SecondMechanic.bullet_fired = False
            
    def cooldown(self):
        SecondMechanic.bullet_cooldown_vary = pygame.time.get_ticks()
        if SecondMechanic.bullet_cooldown_vary - SecondMechanic.bullet_cooldown_const > SecondMechanic.bullet_cooldown_delay:
            SecondMechanic.bullet_fired = True
            # Duration to fire bullet
            if SecondMechanic.bullet_cooldown_vary - SecondMechanic.bullet_cooldown_const > SecondMechanic.bullet_cooldown_delay + SecondMechanic.bullet_fire_duration:
                SecondMechanic.bullet_cooldown_const = pygame.time.get_ticks()
        
        # Reset Bullet
        else:
            SecondMechanic.bullet_fired = False
            SecondMechanic.bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
            SecondMechanic.bullet_reset()    

class ThirdMechanic:
    # se - side enemy
    # me - main enemy

    se_img = [pygame.image.load("boss3alien-b-left.png"), pygame.image.load("boss3alien-b-right.png")]
    se_pos = [[-150,860],[2030,770]]
    se_bullet_img = pygame.image.load("laser-horizontal.png")
    se_bullet_pos = [[110,885],[-47,795]]
    se_bullet_state = ["ready","ready"]
    se_bullet_fired = [False,False]
    se_bullet_duration = 5000
    se_bullet_delay = 5000
    se_bullet_cooldown_const = pygame.time.get_ticks()
    se_selector = random.choice([0,1])
    
    me_img = pygame.image.load("boss3alien-a.png")
    me_hitbox = [None for _ in range(8)]
    me_spawn_rand = (100,50)
    me_spawn_y = [0 for i in range(6)]
    me_pos = [[700,400],[400,500],[250,300],[1200,450],[1450,280],[1650,550]]
    me_bound_x = []
    me_speed = 2
    me_change = []  
    me_bullet_img = pygame.image.load("slime.png")
    me_bullet_pos = [[],[],[],[],[],[]]
    me_bullet_state = ["ready" for _ in range(6)]
    me_bullet_fired = [False for _ in range(6)]
    me_bullet_cooldown = 10000
    me_bullet_cooldown_const = 0
    bullet_cooldown_vary = 0
    bullet_hitboxes = [None for _ in range(8)]


    for i in range(6):
        # Different spawn points for me each run
        me_pos[i][0] = random.choice([i for i in range(me_pos[i][0] - me_spawn_rand[0],me_pos[i][0] + me_spawn_rand[0])])
        me_pos[i][1] = random.choice([i for i in range(me_pos[i][1] - me_spawn_rand[1],me_pos[i][1] + me_spawn_rand[1])])
    
        # Initial spawn point for me
        me_spawn_y[i] = me_pos[i][1] - 1000
        '''
        # Boundary
        me_bound_x.append([me_pos[i][0]+50,me_pos[i][0]-50])

        # Speed
        me_change.append(random.choice([me_speed, -me_speed]))
        '''
    me_bound_x = [[me_pos[i][0]+50,me_pos[i][0]-50] for i in range(6)]
    me_change = [random.choice([me_speed, -me_speed]) for i in range(6)]
    
    def draw_enemies(self):
        for i in range(2):
            screen.blit(ThirdMechanic.se_img[i], ThirdMechanic.se_pos[i])
            if ThirdMechanic.se_pos[0][0] < 50 and ThirdMechanic.se_pos[1][0] > 1830:
                ThirdMechanic.se_pos[0][0] += 1
                ThirdMechanic.se_pos[1][0] += -1
        
        for i in range(6):
            screen.blit(ThirdMechanic.me_img, (ThirdMechanic.me_pos[i][0],ThirdMechanic.me_spawn_y[i])) 
            if ThirdMechanic.me_spawn_y[i] < ThirdMechanic.me_pos[i][1]:
                ThirdMechanic.me_spawn_y[i] += 5
            else:
                ThirdMechanic.me_pos[i][0] += ThirdMechanic.me_change[i]

        # Restrict player movement from the sides   
        if Player.player_pos[0] < 150:
            Player.player_pos[0] = 150
        if Player.player_pos[0] > 1730:
            Player.player_pos[0] = 1730

    def create_hitbox(self):
        for i in range(6):
            ThirdMechanic.me_hitbox[i] = ThirdMechanic.me_img.get_rect(topleft = ThirdMechanic.me_pos[i])
            pygame.draw.rect(screen,(255,0,0),ThirdMechanic.me_hitbox[i])

    def me_movement(self):
        for i in range(6):
            if ThirdMechanic.me_pos[i][0] < ThirdMechanic.me_bound_x[i][1]:
                ThirdMechanic.me_change[i] = ThirdMechanic.me_speed
            if ThirdMechanic.me_pos[i][0] > ThirdMechanic.me_bound_x[i][0]:
                ThirdMechanic.me_change[i] = -ThirdMechanic.me_speed
            
    def draw_bullet(self):
        for i in range(2):
            if ThirdMechanic.se_bullet_fired[i]:
                screen.blit(ThirdMechanic.se_bullet_img, ThirdMechanic.se_bullet_pos[i])
                ThirdMechanic.se_bullet_state[i] = "not ready"

        for i in range(6):
            if ThirdMechanic.me_bullet_fired[i]:
                screen.blit(ThirdMechanic.me_bullet_img, ThirdMechanic.me_bullet_pos[i])
                ThirdMechanic.me_bullet_state[i] = "not ready"

    def create_bullet_hitbox(self):
        for i in range(2):
            if ThirdMechanic.se_bullet_fired[i]: 
                ThirdMechanic.bullet_hitboxes[i] = ThirdMechanic.se_bullet_img.get_rect(topleft=ThirdMechanic.se_bullet_pos[i])
        for i in range(6):
            if ThirdMechanic.me_bullet_fired[i]:
                ThirdMechanic.bullet_hitboxes[i+2] = ThirdMechanic.me_bullet_img.get_rect(topleft=ThirdMechanic.me_bullet_pos[i])
    
    def bullet_movement(self):
        if SecondMechanic.bullet_fired:
            SecondMechanic.bullet_change = SecondMechanic.bullet_speed
        else:
            SecondMechanic.bullet_change = 0
        for i in range(4):
            SecondMechanic.bullet_pos[i][1] += SecondMechanic.bullet_change

        SecondMechanic.bullet_reset()

    def shoot_bullet(self):
        if SecondMechanic.bullet_state == "ready":
            SecondMechanic.bullet_fired = True
            for i in range(4):
                SecondMechanic.bullet_pos[i][0] = EnemyBoss.enemy_pos[0]

    def bullet_reset():
        for i in range(4):
            if SecondMechanic.bullet_pos[i][1] > 1100:
                SecondMechanic.bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
                SecondMechanic.bullet_state = "ready"
                SecondMechanic.bullet_fired = False

    def cooldown(self):
        ThirdMechanic.bullet_cooldown_vary = pygame.time.get_ticks()
        if ThirdMechanic.bullet_cooldown_vary - ThirdMechanic.se_bullet_cooldown_const> ThirdMechanic.se_bullet_delay:
            ThirdMechanic.se_bullet_fired[ThirdMechanic.se_selector] = True
            
            if ThirdMechanic.bullet_cooldown_vary - ThirdMechanic.se_bullet_cooldown_const >ThirdMechanic.se_bullet_delay + ThirdMechanic.se_bullet_duration:
                ThirdMechanic.se_bullet_cooldown_const = pygame.time.get_ticks()
                ThirdMechanic.se_selector = random.choice([0,1])
    
        else:
           ThirdMechanic.se_bullet_fired = [False,False]

        #print(ThirdMechanic.se_bullet_cooldown_const, ThirdMechanic.bullet_cooldown_vary)

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1920, 1080))

# Set background according to level
if Player.current_level == 0:
    bg = pygame.image.load("background.jpg")

bg_y = -1080


player = Player()
boss = EnemyBoss()

running = True
while running:
    screen.fill((255,255,255))

    # Scrolling Background
    bg_rel_y = bg_y % bg.get_rect().height
    screen.blit(bg, (0,bg_rel_y - bg.get_rect().height))
    if bg_rel_y < 1080:
        screen.blit(bg, (0,bg_rel_y))
    bg_y += 2

    
    if player.player_state:
        player_hitbox = player.create_hitbox()
        player.movement()
        player.health()
        player.bullet_movement()


    if boss.enemy_state != "dead":
        boss.spawn()
        boss.health()
        boss_hitbox = boss.create_hitbox()
        '''
        if boss.health[6]:
            boss.mechanic.create_hitbox()
            boss.mechanic.draw_bullet()
            boss.mechanic.bullet_movement()
            boss.mechanic.shoot_bullet()
            boss.mechanic.cooldown()
        else:
            pass
        '''
        boss.mechanic.draw_enemies()
        boss.mechanic.create_hitbox()
        boss.mechanic.create_bullet_hitbox()
        boss.mechanic.draw_bullet()
        boss.mechanic.cooldown()
        boss.mechanic.me_movement()
    #player.reduce_health()

    # Key-press Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        player.create_player_movement(event)
        player.shoot_bullet(event)

    clock.tick(60)
    pygame.display.update()
    
