import pygame
import sys
import random



class snake(object):
    def __init__(self):
        self.length = 1
        self.positions = [((screenWidth / 2), (screenHeight / 2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (115, 199, 199)


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
        # if cur > gridSize or cur > gridSize:
        #     self.reset()

    def handleKeys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)
    

    def reset(self):
        self.length = 1
        self.positions = [((screenWidth / 2), (screenHeight / 2))]
        self.direction = random.choice([up, down, left, right])


    def draw(self, surface):        
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridSize, gridSize))
            if p == self.positions[0]:
                pygame.draw.rect(surface, (105, 180, 180), r)
            else:
                pygame.draw.rect(surface, self.color, r)

            # pygame.draw.rect(surface, (93, 216, 228), r, 1)


class food(object):
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomizePosition()
        self.color = (150, 24, 47)


    def randomizePosition(self):
        self.position = (random.randint(0, gridWidth-1) * gridSize, random.randint(0, gridHeight-1) * gridSize)
    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridSize, gridSize))
        pygame.draw.rect(surface, self.color, r)
        # pygame.draw.rect(surface, (93, 216, 228), r, 1)



def drawGrid(surface):
    for y in range(0, int(gridHeight)):
        for x in range(0, int(gridWidth)):
            if (x + y) % 2 == 0:
                r = pygame.Rect((x*gridSize, y*gridSize), (gridSize, gridSize))
                pygame.draw.rect(surface, (52, 212, 37), r)
                
            else:
                rr = pygame.Rect((x*gridSize, y*gridSize), (gridSize, gridSize))
                pygame.draw.rect(surface, (60, 240, 50), rr)


screenWidth = 576
screenHeight = 576
gridSize = 24
gridWidth = screenWidth / gridSize
gridHeight = screenHeight / gridSize


baseScore = 0

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

    
    score = baseScore

    snakeReference = snake()
    foodReference = food()

    myFont = pygame.font.SysFont("monospace", 16)

    

    while (True):
        clock.tick(10)
        snakeReference.handleKeys()
        drawGrid(surface)
        snakeReference.move()
        if snakeReference.getHeadPosition() == foodReference.position:
            snakeReference.length += 1
            score += 1
            foodReference.randomizePosition()
        
        #Handle Events
        snakeReference.draw(surface)
        foodReference.draw(surface)
        screen.blit(surface, (0,0))
        text = myFont.render("Score {0}".format(score), 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        # if len(snakeReference.positions) < 1:
        #     score = 0
        pygame.display.update()
        

main()