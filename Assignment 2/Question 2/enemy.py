import pygame
from constants import BLACK

class Enemy(object):
    def __init__(self, x, y, width, height, end, health):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 40
        self.visible = True
        self.health = health
        self.box = (self.x, self.y, self.width, self.height)
        self.walkLeftV = [pygame.image.load(f'assets/animation/villain/L{i}E.png') for i in range(1, 12)]
        self.walkRightV = [pygame.image.load(f'assets/animation/villain/R{i}E.png') for i in range(1, 12)]

    def draw(self, win, score):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRightV[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeftV[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            pygame.draw.rect(win, (255, 0, 0), (self.x + 10, self.y - 10, 50, 5))
            pygame.draw.rect(win, (0, 0, 255), (self.x + 10, self.y - 10, 50 * (self.health / 3), 5))
            pygame.draw.rect(win, BLACK, (self.x + 10, self.y - 10, 50, 5), 1)
            self.box = (self.x, self.y, self.width, self.height)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1] + 35:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x + self.vel > 0 - self.width / 2:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            self.visible = False
        print('hit')
