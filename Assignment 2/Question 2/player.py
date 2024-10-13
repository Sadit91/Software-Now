import pygame
from constants import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH
from assets import load_assets

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isJump = False
        self.jumpCount = 10
        self.vel = 5
        self.left = False
        self.right = False
        self.walkCount = 0
        self.standing = True
        self.box = (self.x + 20, self.y + 10, 25, 55)
        self.health = 10
        self.visible = True
        self.walkLeft = [pygame.image.load(f'assets/animation/hero/L{i}.png') for i in range(1, 10)]
        self.walkRight = [pygame.image.load(f'assets/animation/hero/R{i}.png') for i in range(1, 10)]

    def draw(self, win):
        if self.visible:
            if self.walkCount + 1 >= 27:
                self.walkCount = 0
            if not self.standing:
                if self.left:
                    win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.left:
                    win.blit(self.walkLeft[0], (self.x, self.y))
                else:
                    win.blit(self.walkRight[0], (self.x, self.y))
            self.box = (self.x + 20, self.y + 10, 25, 55)

    def hit(self, win):
        self.x = 150
        self.y = 200
        self.isJump = False
        self.jumpCount = 10
        self.walkCount = 0
        win.fill(BLACK)
        font1 = pygame.font.SysFont('Arian', 60, True)
        lost_text = font1.render("You Lost!", 1, (255, 0, 0))
        win.blit(lost_text, (SCREEN_WIDTH // 2 - lost_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        game_over_text = font1.render("Game Over", 1, (255, 0, 0))
        win.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 + 10))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        return False
