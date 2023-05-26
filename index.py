import pygame
import sys
import random


class snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((screenWidth / 2), (screenHeight / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)

    def getHeadPosition(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.getHeadPosition()
        x, y = self.direction
        new = (((cur[0] + (x*gridSize)) % screenWidth), ((cur[1] + (y*gridSize)) % screenHeight))
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def handleKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def reset(self):
        self.length = 1
        self.positions = [((screenWidth / 2), (screenHeight / 2))]
        self.direction = random.choice([up, down, left, right])



    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridSize, gridSize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93, 216, 228), r, 1)


class food(object):
    def __init__(self):
        pass
    def randomizePosition(self):
        pass
    def draw(self, surface):
        pass


def drawGrid(surface):
    for y in range(0, int(gridHeight)):
        for x in range(0, int(gridWidth)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*gridSize, y*gridSize), (gridSize, gridSize))
                pygame.draw.rect(surface, (96, 216, 228), r)
            else:
                rr = pygame.Rect((x*gridSize, y*gridSize), (gridSize, gridSize))
                pygame.draw.rect(surface, (85, 194, 205), rr)


screenWidth = 480
screenHeight = 480
gridSize = 20
gridWidth = screenWidth / gridSize
gridHeight = screenHeight / gridSize

up = (0, -1)
down = (0, 1)
left = (-1, 0)
right = (1, 0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screenWidth, screenHeight), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = snake()
    food = food()

    score = 0

    while (True):
        clock.tick(10)
        #Handle Events

        screen.blit(surface, (0,0))
        pygame.display.update()

main()