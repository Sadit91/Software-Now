import pygame
from constants import BULLET_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from assets import load_assets
from player import Player
from enemy import Enemy
from projectile import Projectile

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

assets = load_assets()
clock = pygame.time.Clock()

score = 0
health = 10
levelCount = 0  
hero = Player(150, 200, 64, 64)
villain = Enemy(200, 400, 64, 64, 800, health)
bullets = []
run = True
shootLoop = 0
font = pygame.font.SysFont('Arian', 40, True, True)  

level_names = ["Beginner", "Skillful", "Boss"]
level_colors = [(255, 255, 255), (0, 255, 0), (255, 0, 0)] 

while run:
    if levelCount == 0:
        clock.tick(15)  
    elif levelCount == 1:
        clock.tick(20)  
    elif levelCount == 2:
        clock.tick(30) 

    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 4:
        shootLoop = 0

    if villain.visible:
        if hero.box[1] + hero.box[3] > villain.box[1] and hero.box[1] < villain.box[1] + villain.box[3]:
            if hero.box[0] + hero.box[2] > villain.box[0] and hero.box[0] < villain.box[0] + villain.box[2]:
                hero.hit(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in bullets:
        if villain.visible:
            if bullet.y + bullet.radius > villain.box[1] and bullet.y - bullet.radius < villain.box[1] + villain.box[3]:
                if bullet.x + bullet.radius > villain.box[0] and bullet.x - bullet.radius < villain.box[0] + villain.box[2]:
                    bullets.pop(bullets.index(bullet))
                    villain.hit()  
                    assets['hit_sound'].play()
                    score += 1

        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_x] and shootLoop == 0:
        assets['bullet_sound'].play()
        facing = -1 if hero.left else 1
        if len(bullets) < 5:
            bullets.append(Projectile(round(hero.x + hero.width // 2), round(hero.y + hero.height // 2), 6, BULLET_COLOR, facing))
        shootLoop = 1

    if keys[pygame.K_LEFT] and hero.x > hero.vel:
        hero.x -= hero.vel
        hero.left = True
        hero.right = False
        hero.standing = False
    elif keys[pygame.K_RIGHT] and hero.x < SCREEN_WIDTH - hero.width - hero.vel:
        hero.x += hero.vel
        hero.right = True
        hero.left = False
        hero.standing = False
    else:
        hero.standing = True
        hero.walkCount = 0

    if keys[pygame.K_DOWN] and hero.y < SCREEN_HEIGHT - hero.height:
        hero.y += hero.vel

    if not hero.isJump:
        if keys[pygame.K_SPACE]:
            hero.isJump = True
            hero.right = False
            hero.left = False
            hero.walkCount = 0
    else:
        if hero.jumpCount >= -10:
            neg = 1 if hero.jumpCount >= 0 else -1
            hero.y -= (hero.jumpCount ** 2) * 0.5 * neg
            hero.jumpCount -= 1
        else:
            hero.isJump = False
            hero.jumpCount = 10

    win.blit(assets['background'], (0, 0))
    hero.draw(win)
    villain.draw(win, score)  

    for bullet in bullets:
        bullet.draw(win)

    levelText = font.render(f'Level: {level_names[levelCount]}' if levelCount < len(level_names) else 'Level: Max', 1, level_colors[levelCount])
    win.blit(levelText, (10, 10))  

    scoreText = font.render(f'Score: {score}', 1, (0, 0, 0))
    score_x_pos = SCREEN_WIDTH - scoreText.get_width() - 10 
    win.blit(scoreText, (score_x_pos, 10))

    if not villain.visible:
        win.fill(BLACK)          
        win.blit(assets['background'], (0, 0))  
        
        win_text = font.render("You Won!", 1, (255, 215, 0))  
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)) 
        pygame.draw.rect(win, (0, 0, 0), text_rect.inflate(20, 20)) 
        win.blit(win_text, text_rect)  
 
        if levelCount == 0:
            win_text = font.render("Transfer from Beginner to Skillful", 1, (255, 255, 255))
        elif levelCount == 1:
            win_text = font.render("You won, level up to Boss!", 1, (255, 255, 255))
        elif levelCount == 2:
            win_text = font.render("Last time, Congratulations, champ!", 1, (255, 255, 255))
        
        win.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))  
        
        pygame.display.update()  
        pygame.time.delay(2000)  

        if levelCount < len(level_names) - 1:
            levelCount += 1             
            score = 0
            health += 10  
            hero = Player(150, 200, 64, 64)
            villain = Enemy(200, 400, 64, 64, 800, health)            
            bullets = [] 
        else:
            run = False 

    pygame.display.update()

pygame.quit()
