import sys
import pygame
import random

running = True
exit = False

def run():
    global running, exit 
    pygame.init()

    class Player:
        #Player attributes
        player_img = pygame.image.load("images/spaceship.png")
        player_pos = [900,800]
        player_change = [0,0]
        player_speed = 10
        player_health = {0:True, 1:True, 2:True}
        player_state = True
        current_level = 0
        score = 0
        first_hitcount = 0
        second_hitcount = 0
        se_hitcount = 0
        me_hitcount = 0
        display_time_const = pygame.time.get_ticks()
        level_proceed = False
        level_done = False
        game_done = False

        #Bullet attributes
        bullet_img = pygame.image.load("images/bullet.png")
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
                Player.bullet_state = "ready"
                Player.bullet_fire = False
                Player.bullet_pos[1] = 800
                
        def bullet_movement(self):
            if Player.bullet_fire:
                player.create_bullet(Player.bullet_pos[0],Player.bullet_pos[1])
                Player.bullet_pos[1] += Player.bullet_change[1]
            if Player.bullet_pos[1] < 0:
                player.bullet_reset()

        def health(self):
            # Draw hearts
            img_health = pygame.image.load("images/heart .png")
            img_no_health = pygame.image.load("images/black_heart .png")
            health_pos = [(130,975),(90,975),(50,975)]
            for i in Player.player_health.keys():
                if Player.player_health[i] == True:
                    screen.blit(img_health, health_pos[i])
                else:
                    screen.blit(img_no_health, health_pos[i])        
        
        def reduce_health(self):
            # Detect if boss hit player
            if player.current_level == 2:
                if boss.enemy_health[5]:
                    if boss.mechanic.bullet_fired:
                        for i in range(4):
                            if player_hitbox.colliderect(boss.mechanic.bullet_hitboxes[i]):
                                boss.mechanic.bullet_pos[i] = [-1000,200] 
                                if boss.enemy_health[2]:
                                    player.first_hitcount += 1
                                else:
                                    player.second_hitcount = 1
                else:
                    for i in range(6):
                        if boss.mechanic.me_bullet_fired[i]:
                            boss.mechanic.me_bullet_hitbox()
                            if player_hitbox.colliderect(boss.mechanic.me_bullet_hitboxes[i]):
                                boss.mechanic.bullet_reset(i)
                                player.me_hitcount = 1
                        
                    for i in range(2):
                        if boss.mechanic.se_bullet_fired[i]:
                            boss.mechanic.se_bullet_hitbox()
                            if player_hitbox.colliderect(boss.mechanic.se_bullet_hitboxes[i]):
                                player.se_hitcount += 1

            elif player.current_level == 1:
                for i in range(5):
                    if SecondLevel.bullet_hitboxes[i].colliderect(player_hitbox):
                        level2.bullet_reset(i) 
                        for i in player.player_health.keys():
                             if Player.player_health[i]:
                                Player.player_health[i] = False
                                break

            # Reduce player health
            if player.first_hitcount>16 or player.second_hitcount or player.me_hitcount or player.se_hitcount>70:
                for i in Player.player_health.keys():
                    if Player.player_health[i]:
                        Player.player_health[i] = False
                        break
                
                player.first_hitcount = 0
                player.second_hitcount = 0
                player.me_hitcount = 0
                player.se_hitcount = 0
                
            # End game if player dies
            if not Player.player_health[2]:
                    Player.player_state = False
                    player.game_over()

        def game_over(self):
            over = pygame.font.Font("AldotheApache.ttf",200)
            over1 = pygame.font.Font("AldotheApache.ttf",50)
            game  = over.render("GAME OVER ",True,(255,255,255))
            menu = over1.render("PRESS SPACE TO RETURN TO MENU", True,(255,255,255))
            screen.blit(game,(550,300))
            screen.blit(menu,(640,500))

        def level_complete(self):
            comp = pygame.font.Font("AldotheApache.ttf",150)
            comp1 = pygame.font.Font("AldotheApache.ttf",50)
            level = comp.render("LEVEL COMPLETED",True,(255,255,255)) 
            next = comp1.render("PRESS SPACE TO PROCEED", True,(255,255,255))
            screen.blit(level,(460,300))
            screen.blit(next,(710,450))
            if player.level_proceed:
                player.current_level += 1
                player.level_proceed = False
                player.level_done = False

        def game_complete(self):
            global exit, running
            player.game_done = True
            comp = pygame.font.Font("AldotheApache.ttf",150)
            comp1 = pygame.font.Font("AldotheApache.ttf",100)
            cong1 = pygame.font.Font("AldotheApache.ttf",50)
            cong = comp.render("CONGRATULATIONS",True,(255,255,255)) 
            level = comp1.render("YOU WON",True,(255,255,255)) 
            next = cong1.render("PRESS SPACE TO RETURN TO MENU", True,(255,255,255))
            screen.blit(cong,(440,250))
            screen.blit(level,(750,400))
            screen.blit(next,(630,500))
            if player.level_proceed:
                exit = True
                running = False
                
            
        def mission(self):
            goal = pygame.font.Font("AldotheApache.ttf",30)
            text = ""
            text_pos = [0,0]
            if player.current_level == 0:
                text = "Shoot All The Enemies Before They Reach You"
                text_pos = [650,975]
            elif player.current_level == 1:
                text = "Shoot Each Enemy 3 times to eleminate them"
                text_pos = [650, 975]
            elif player.current_level == 2:
                text = "Defeat The Boss"
                text_pos = [800,975]
            aim = goal.render(text,True,(255,255,255)) 
            screen.blit(aim,text_pos)

    class FirstLevel:
        num = 20
        enemyimg = [pygame.image.load("images/alien.png") for _ in range(num)]
        enemyx = [random.randint(1000,1800) for _ in range(num)]
        enemyy = [random.randint(20,350) for _ in range(num)]
        enemyx_change = [6.5 for _ in range(num)]
        enemyy_change = [60 for _ in range(num)] 
        enemy_hitbox = [pygame.rect.Rect(0,0,0,0) for _ in range(num)]
        enemy_state = [True for _ in range(num)]
        score = 0
        
        def draw_enemy(x,y,i):
            screen.blit(FirstLevel.enemyimg[i],(x,y))

        def create_htibox(self):
            for i in range(FirstLevel.num):
                if FirstLevel.enemy_state[i]:
                    FirstLevel.enemy_hitbox[i] = FirstLevel.enemyimg[i].get_rect(topleft = (FirstLevel.enemyx[i], FirstLevel.enemyy[i]))
                else:
                    FirstLevel.enemy_hitbox[i] = pygame.rect.Rect(-100,-100,0,0)
                    pygame.draw.rect(screen, (255,0,0), FirstLevel.enemy_hitbox[i])

        def collision(self):
            bullet_hit = player.bullet_hitbox()
            for i in range(FirstLevel.num):
                if bullet_hit.colliderect(FirstLevel.enemy_hitbox[i]):
                    player.bullet_reset()
                    FirstLevel.enemy_state[i] = False
                    FirstLevel.score += 1

        def movement(self):
            for i in range(FirstLevel.num):
                # Game Over
                if FirstLevel.enemyy[i] > 800:
                    for j in range(FirstLevel.num):
                        player.player_state = False
                        player.game_over()
                        FirstLevel.enemy_state = [False for _ in range(FirstLevel.num)]
                    break 

                # Level Completion
                elif FirstLevel.score == FirstLevel.num:
                    player.level_done = True
                    break

                FirstLevel.enemyx[i] += FirstLevel.enemyx_change[i]
                if FirstLevel.enemyx[i] <=0:
                    FirstLevel.enemyx_change[i] = 6.5
                    FirstLevel.enemyy[i] += FirstLevel.enemyy_change[i]
                elif FirstLevel.enemyx[i] >= 1880:
                    FirstLevel.enemyx_change[i] = -6.5
                    FirstLevel.enemyy[i] += FirstLevel.enemyy_change[i]

                if FirstLevel.enemy_state[i]:
                    FirstLevel.draw_enemy(FirstLevel.enemyx[i],FirstLevel.enemyy[i],i)

    class SecondLevel:
        enemyimgs = [pygame.image.load("images/monster.png"),pygame.image.load("images/monster2.png"),pygame.image.load("images/monster3.png"),pygame.image.load("images/monster4.png"),
                    pygame.image.load("images/monster5.png")]
        enemyx = [75,200,300,500,600]
        enemyy = [50,120,190,260,330]
        enemyx_change = [6 for _ in range(5)]
        enemyy_change = [0 for _ in range(5)]
        enemy_hitboxes = [pygame.rect.Rect(0,0,0,0) for _ in range(5)]
        enemy_state = [True for _ in range(5)]
        enemy_health = [3 for _ in range(5)]

        bulletimgs = [pygame.image.load("images/slime.png") for _ in range(5)]
        bulletx = [i for i in enemyx]
        bullety = [50,50,50,50,50]
        bullety_change = [10 for _ in range(5)]
        bullet_state = ["Ready" for _ in range(5)]  
        bullet_hitboxes = [pygame.rect.Rect(0,0,0,0) for _ in range(5)]

        def draw_enemy(self):
            for i in range(5):
                if SecondLevel.enemy_state[i]:
                    screen.blit(SecondLevel.enemyimgs[i], (SecondLevel.enemyx[i],SecondLevel.enemyy[i]))

        def fire_bullet(self):
            for i in range(5):
                if SecondLevel.enemy_state[i]:
                    SecondLevel.bullet_state[i] = "Fire"
                    screen.blit(SecondLevel.bulletimgs[i], (SecondLevel.bulletx[i]+16, SecondLevel.bullety[i]+10))
                    if SecondLevel.bullet_state[i] == "Fire":
                        SecondLevel.bullety[i] += SecondLevel.bullety_change[i]
                        
        def create_hitbox(self):
            for i in range(5):
                if SecondLevel.enemy_state[i]:
                    SecondLevel.enemy_hitboxes[i] = SecondLevel.enemyimgs[i].get_rect(topleft=(SecondLevel.enemyx[i], SecondLevel.enemyy[i]))
                    SecondLevel.bullet_hitboxes[i] = SecondLevel.bulletimgs[i].get_rect(topleft = (SecondLevel.bulletx[i], SecondLevel.bullety[i]))
        
        def enemy_movement(self):
            bullet_hit = player.bullet_hitbox()
            for i in range(5):
                if SecondLevel.enemy_state[i]:
                    SecondLevel.enemyx[i] += SecondLevel.enemyx_change[i]
                    if SecondLevel.enemyx[i] <=0:
                        SecondLevel.enemyx_change[i] = 4.5
        
                    elif SecondLevel.enemyx[i] >= 1880:
                        SecondLevel.enemyx_change[i] = -4.5
                
                    if bullet_hit.colliderect(SecondLevel.enemy_hitboxes[i]):
                        SecondLevel.enemy_health[i] -= 1
                        player.bullet_reset()

                    if not SecondLevel.enemy_health[i]: 
                        SecondLevel.enemy_state[i] = False

             # Level Completion
                elif True not in level2.enemy_state:
                    player.level_done = True
                    break

        def bullet_movement(self):
            for i in range(5):
                if SecondLevel.enemy_state[i]:
                    if SecondLevel.bullet_state[i] == "Ready":
                        level2.fire_bullet()
                    if SecondLevel.bullety[i] > 1000:
                        level2.bullet_reset(i)

        def bullet_hitbox(self):
            for i in range(5):
                if SecondLevel.enemy_state[i]:
                    SecondLevel.bullet_hitboxes[i] = SecondLevel.bulletimgs[i].get_rect(topleft=(SecondLevel.bulletx[i],SecondLevel.bullety[i]))
                else:
                    SecondLevel.bullet_hitboxes[i] = pygame.rect.Rect(0,0,0,0)
            
        def bullet_reset(self,i):
            SecondLevel.bullet_state[i] == "Ready"
            SecondLevel.bullety[i] = SecondLevel.enemyy[i] + 10
            SecondLevel.bulletx[i] = SecondLevel.enemyx[i] + 16
                        
    class EnemyBoss:
        # Boss Attributes
        enemy_img = pygame.image.load("images/alienboss.png")
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
            # Show health
            img_health = pygame.image.load("images/skull.png")
            img_no_health = pygame.image.load("images/black_skull.png")
            health_pos = [(1400,975),(1440,975),(1480,975),(1520,975),(1560,975),(1600,975),(1640,975),(1680,975),(1720,975),(1760,975)]
            for i in boss.enemy_health.keys():
                if boss.enemy_health[i]:
                    screen.blit(img_health, health_pos[i])
                else:
                    screen.blit(img_no_health, health_pos[i])
        
            # Choose mechanic based on health of boss
            if EnemyBoss.enemy_health[2]:
                EnemyBoss.mechanic = FirstMechanic()
            elif EnemyBoss.enemy_health[5]:
                EnemyBoss.mechanic = SecondMechanic()
            elif EnemyBoss.enemy_health[9]:
                EnemyBoss.mechanic = ThirdMechanic()
            else:
                EnemyBoss.enemy_state = "dead"
                player.game_complete()

            # Detect if player hit boss
            bullet_hit = player.bullet_hitbox()
            boss_hit = boss.create_hitbox()
            if boss_hit.colliderect(bullet_hit):
                EnemyBoss.hitcount += 1
            
            # Reduce boss health
            if EnemyBoss.hitcount == 80:
                for i in EnemyBoss.enemy_health.keys():
                    if EnemyBoss.enemy_health[i] == True:
                        EnemyBoss.enemy_health[i] = False
                        break

                EnemyBoss.hitcount = 0        

    class FirstMechanic:
        bullet_img = pygame.image.load("images/laser.png") 
        bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
        bullet_hitboxes = [pygame.rect.Rect(0,0,0,0) for _ in range(4)]
        bullet_speed = 15
        bullet_change = 0
        bullet_state = "ready"
        bullet_fired = False
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
        bullet_img = pygame.image.load("images/boss1.png") 
        bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
        bullet_hitboxes = [pygame.rect.Rect(0,0,0,0) for _ in range(4)]
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
                if SecondMechanic.bullet_cooldown_vary - SecondMechanic.bullet_cooldown_const > SecondMechanic.bullet_cooldown_delay + SecondMechanic.bullet_fire_duration:
                    SecondMechanic.bullet_cooldown_const = pygame.time.get_ticks()
            else:
                SecondMechanic.bullet_fired = False
                SecondMechanic.bullet_pos = [[-1000,200],[-1000,200],[-1000,200],[-1000,200]]
                SecondMechanic.bullet_reset()    

    class ThirdMechanic:
        # se - side enemy
        # me - main enemy

        se_img = [pygame.image.load("images/boss3alien-b-left.png"), pygame.image.load("images/boss3alien-b-right.png")]
        se_pos = [[-150,860],[2030,770]]
        se_bullet_img = pygame.image.load("images/laser-horizontal.png")
        se_bullet_pos = [[110,885],[-47,795]]
        se_bullet_state = ["ready","ready"]
        se_bullet_fired = [False,False]
        se_bullet_duration = 6000
        se_bullet_delay = 3000
        se_bullet_cooldown_const = pygame.time.get_ticks()
        se_selector = random.choice([0,1])
        se_bullet_hitboxes = [pygame.rect.Rect(0,0,0,0) for _ in range(2)]

        me_img = pygame.image.load("images/boss3alien-a.png")
        me_hitbox = [pygame.rect.Rect(0,0,0,0) for _ in range(6)]
        me_spawn_rand = (100,50)
        me_spawn_y = [0 for i in range(6)]
        me_pos = [[700,400],[500,500],[250,300],[1200,450],[1450,280],[1650,550]]
        me_bound_x = []
        me_speed = 2
        me_change = []
        me_state = [True for _ in range(6)]
        me_health = [[True,True] for _ in range(6)]

        me_bullet_img = pygame.image.load("images/slime.png")
        me_bullet_pos = [[0,0] for _ in range(6)]
        me_bullet_speed = 10
        me_bullet_change = [0,0,0,0,0,0]
        me_bullet_state = ["ready" for _ in range(6)]
        me_bullet_fired = [False for _ in range(6)]
        me_bullet_cooldown = 2000
        me_bullet_duration = 10000
        me_bullet_cooldown_const = 0
        me_bullet_hitboxes = [pygame.rect.Rect(0,0,0,0) for _ in range(6)]
        bullet_cooldown_vary = 0

        for i in range(6):
            # Different spawn points for me each run
            me_pos[i][0] = random.choice([i for i in range(me_pos[i][0] - me_spawn_rand[0],me_pos[i][0] + me_spawn_rand[0])])
            me_pos[i][1] = random.choice([i for i in range(me_pos[i][1] - me_spawn_rand[1],me_pos[i][1] + me_spawn_rand[1])])

            # Initial spawn point for me
            me_spawn_y[i] = me_pos[i][1] - 1000
            
            # Boundary
            me_bound_x.append([me_pos[i][0]+100,me_pos[i][0]-100])

            # Speed
            me_change.append(random.choice([me_speed, -me_speed]))

            # Bullet 
            me_bullet_pos[i] = [me_pos[i][0] + 15, me_pos[i][1] + 10]

        def draw_enemies(self):
            for i in range(2):
                screen.blit(ThirdMechanic.se_img[i], ThirdMechanic.se_pos[i])
                if ThirdMechanic.se_pos[0][0] < 50 and ThirdMechanic.se_pos[1][0] > 1830:
                    ThirdMechanic.se_pos[0][0] += 1
                    ThirdMechanic.se_pos[1][0] += -1
            
            for i in range(6):
                if ThirdMechanic.me_state[i]:
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
                if ThirdMechanic.me_state[i]:
                    ThirdMechanic.me_hitbox[i] = ThirdMechanic.me_img.get_rect(topleft = ThirdMechanic.me_pos[i])
                #pygame.draw.rect(screen,(255,0,0),ThirdMechanic.me_hitbox[i])

        def me_movement(self):
            for i in range(6):
                if ThirdMechanic.me_state[i]:
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
                if ThirdMechanic.me_state[i]:
                    if ThirdMechanic.me_bullet_fired[i]:
                        screen.blit(ThirdMechanic.me_bullet_img, ThirdMechanic.me_bullet_pos[i])
                        ThirdMechanic.me_bullet_state[i] = "not ready"

        def se_bullet_hitbox(self):
            for i in range(2):
                if ThirdMechanic.se_bullet_fired[i]: 
                    ThirdMechanic.se_bullet_hitboxes[i] = ThirdMechanic.se_bullet_img.get_rect(topleft=ThirdMechanic.se_bullet_pos[i])
        
        def me_bullet_hitbox(self):
            for i in range(6):
                if ThirdMechanic.me_state[i]:
                    if ThirdMechanic.me_bullet_fired[i]:
                        ThirdMechanic.me_bullet_hitboxes[i] = ThirdMechanic.me_bullet_img.get_rect(topleft=ThirdMechanic.me_bullet_pos[i])
                
        def bullet_movement(self):
            for i in range(6):
                if ThirdMechanic.me_bullet_fired[i]:
                    ThirdMechanic.me_bullet_change[i] = ThirdMechanic.me_bullet_speed
                else:
                    ThirdMechanic.me_bullet_change[i] = 0
                ThirdMechanic.me_bullet_pos[i][1] += ThirdMechanic.me_bullet_change[i]
                if ThirdMechanic.me_bullet_pos[i][1] > 1100:
                    boss.mechanic.bullet_reset(i)

        def shoot_bullet(self):
            if ThirdMechanic.me_bullet_state == "ready":
                ThirdMechanic.me_bullet_fired = True
                for i in range(6):
                    ThirdMechanic.me_bullet_pos[i][0] = ThirdMechanic.me_pos[i][0]+15        

        def bullet_reset(self,i):
                ThirdMechanic.me_bullet_pos[i] = [ThirdMechanic.me_pos[i][0]+15, ThirdMechanic.me_pos[i][1] + 10]
                ThirdMechanic.me_bullet_state[i] = "ready"
                ThirdMechanic.me_bullet_fired[i] = False

        def cooldown(self):
            ThirdMechanic.bullet_cooldown_vary = pygame.time.get_ticks()
            if ThirdMechanic.bullet_cooldown_vary - ThirdMechanic.se_bullet_cooldown_const> ThirdMechanic.se_bullet_delay:
                ThirdMechanic.se_bullet_fired[ThirdMechanic.se_selector] = True
                if ThirdMechanic.bullet_cooldown_vary - ThirdMechanic.se_bullet_cooldown_const >ThirdMechanic.se_bullet_delay + ThirdMechanic.se_bullet_duration:
                    ThirdMechanic.se_bullet_cooldown_const = pygame.time.get_ticks()
                    ThirdMechanic.se_selector = random.choice([0,1])
            else:
                ThirdMechanic.se_bullet_fired = [False,False]
        
            for i in range(6):
                if ThirdMechanic.me_state[i]:
                    if ThirdMechanic.bullet_cooldown_vary - ThirdMechanic.me_bullet_cooldown_const > ThirdMechanic.me_bullet_cooldown:
                        ThirdMechanic.me_bullet_fired[i] = True
                        if ThirdMechanic.bullet_cooldown_vary - ThirdMechanic.me_bullet_cooldown_const > ThirdMechanic.me_bullet_cooldown + ThirdMechanic.me_bullet_duration:
                            ThirdMechanic.me_bullet_cooldown_const = pygame.time.get_ticks()
                    else:
                        ThirdMechanic.me_bullet_fired[i] = False
        
        def health(self):
            img_health = pygame.image.load("images/boss3alien-a-health.png")
            health_pos = [(ThirdMechanic.me_pos[i][0]+13,ThirdMechanic.me_spawn_y[i] - 20) for i in range(6)]
            bullet_hit = player.bullet_hitbox()

            for i in range(6):
                if ThirdMechanic.me_health[i][0]:
                    screen.blit(img_health, health_pos[i])
                if ThirdMechanic.me_health[i][1]:
                    screen.blit(img_health, (health_pos[i][0]+20,health_pos[i][1]))
                if ThirdMechanic.me_state[i]:
                    if bullet_hit.colliderect(ThirdMechanic.me_hitbox[i]):
                        player.bullet_reset()
                        if ThirdMechanic.me_health[i][0]:
                            ThirdMechanic.me_health[i][0] = False
                        elif ThirdMechanic.me_health[i][1]:
                            ThirdMechanic.me_health[i][1] = False
                            ThirdMechanic.me_state[i] = False

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1920, 1020))
    pygame.display.set_caption("Space Invaders")
    icon = pygame.image.load("images/ufo1.png")
    pygame.display.set_icon(icon)

    bg = [pygame.image.load("images/background.jpg"),pygame.image.load("images/background1.jpg"),pygame.image.load("images/background2.jpg")]
    bg_y = -1080

    def draw_bg(level):
        nonlocal bg_y  
        bg_rel_y = bg_y % bg[level].get_rect().height
        screen.blit(bg[level], (0,bg_rel_y - bg[level].get_rect().height))
        if bg_rel_y < 1080:
            screen.blit(bg[level], (0,bg_rel_y))
        bg_y += 2

    player = Player()
    boss = EnemyBoss()
    level1 = FirstLevel()
    level2 = SecondLevel()

    while running:
        screen.fill((255,255,255))

        draw_bg(player.current_level)

        if player.player_state:
            player_hitbox = player.create_hitbox()
            player.movement()
            player.health()
            player.bullet_movement()
            player.mission()
            if player.level_done:
                player.level_complete()
            if player.game_done:
                player.game_complete()
            
        if player.current_level == 0:
            level1.create_htibox()
            level1.movement()
            level1.collision()

        elif player.current_level == 1:
            level2.create_hitbox()
            level2.draw_enemy()
            level2.enemy_movement()
            level2.bullet_movement()
            level2.bullet_hitbox()
            level2.fire_bullet()

        elif player.current_level == 2:
            if boss.enemy_state != "dead":
                boss.spawn()    
                boss.health()
                
                if boss.enemy_health[5]:
                    boss.mechanic.create_hitbox()
                    boss.mechanic.draw_bullet()
                    boss.mechanic.bullet_movement()
                    boss.mechanic.shoot_bullet()
                    boss.mechanic.cooldown()
                else:
                    boss.health()
                    boss.mechanic.draw_enemies()
                    boss.mechanic.create_hitbox()
                    boss.mechanic.draw_bullet()
                    boss.mechanic.cooldown()
                    boss.mechanic.me_movement()
                    boss.mechanic.health()
                    boss.mechanic.bullet_movement()
                    boss.mechanic.shoot_bullet()    
                    
        player.reduce_health()

        # Key-press Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if player.level_done or player.game_done:
                    if event.key == pygame.K_SPACE:
                        player.level_proceed = True

                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            
                if not player.player_state:
                    if event.key == pygame.K_SPACE:
                        running = False


            player.create_player_movement(event)
            player.shoot_bullet(event)

        clock.tick(60)
        pygame.display.update()

        if not running:
            pygame.display.quit()
            exit = True
