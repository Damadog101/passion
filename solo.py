import pygame
import sys

#game intentions will be to avoid the balloons coming from bottom of screen

bgColor = (115, 199, 199)
screen = pygame.display.set_mode((500, 500))

x = 100
y = 100


class shork(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, image):
        super().__init__()
        self.position = (x, y)
        self.velocity = (dx, dy)
        self.sprite = pygame.image.load(image)
    def update(self):
        self.position = ((self.position[0] + self.velocity[0]), (self.position[1] + self.velocity[1]))
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 0, 0), self.position, 10)
        # surface.blit(self.sprite, self.position)
    def moveLeft(self):
        self.velocity = (-1, self.velocity[1])
    def moveRight(self):
        self.velocity = (1, self.velocity[1])
    def draw(self, surface):
        # width = self.sprite.get_rect().width
        # height = self.sprite.get_rect().height
        # self.sprite = pygame.transform.scale(self.sprite, (width/2, height/2))

        surface.blit(self.sprite, self.position)
    def moveUp(self):
        self.position = (self.position[0], self.position[1] + 20)











def main():
    pygame.init()
    screenSize = (1000, 700)
    window = pygame.display.set_mode(screenSize)
    player = shork(320, 240, 0, 0, "shork.png")
    pygame.display.set_caption('Safe Seagulls')


    while True:
    # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.moveLeft()
                elif event.key == pygame.K_d:
                    player.moveRight()
                elif event.key == pygame.MOUSEBUTTONDOWN:
                    player.moveUp()
        
        # Update the player sprite
        player.update()
        
        # Clear the window
        window.fill(bgColor)
        
        # Draw the player sprite
        player.draw(window)
        
        # Update the display
        pygame.display.update()

    # pygame.display.flip()

    # running = True




main()



