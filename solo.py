import pygame
import sys

#game intentions will be to avoid the balloons coming from bottom of screen

bgColor = (115, 199, 199)
screen = pygame.display.set_mode((500, 500))

x = 100
y = 100

screenWidth = 1000
screenHeight = 700
window = pygame.display.set_mode((screenWidth, screenHeight))




class seagull(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, image, mass, jumpdx):
        super().__init__()
        self.position = (x, y)
        self.velocity = (dx, dy) 
        self.sprite = pygame.image.load(image)
        self.mass = mass
        self.jump = jumpdx
        self.isJumping = True
        self.isFalling = False


    def update(self):
        self.position = ((self.position[0] + self.velocity[0]), (self.position[1] + self.velocity[1]))
        if self.position[0] + 200 > screenWidth:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.position[0] < 0:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.position[1] + 125 > screenHeight:
            self.velocity = (self.velocity[0], 0)
            self.position = (self.position[0], self.position[1] - 10)  

        if self.position[1] < 0:
            self.velocity = (self.velocity[0], 0)
            self.position = (self.position[0], self.position[1] + 10)

        if self.isJumping and self.isFalling is False:
            # self.isFalling = True
            print("velocity Y: ", self.velocity[1])
            self.velocity = (self.velocity[0], -1)  # how high to jump
            # pygame.time.delay(10)


    def moveLeft(self):
        self.velocity = (-1, self.velocity[1])


    def moveRight(self):
        self.velocity = (1, self.velocity[1])

    def gravity(self):
        if self.isJumping:
            self.velocity = (self.velocity[0], 3)

    def flap(self):
        if self.isJumping is False:
            self.isFalling = False
            self.isJumping = True


    # def moveUp(self):  

    #     pass

    #     # self.isJump = isJump

    #     # if self.isJump:
    #     #     Force = (1 / 2) * self.mass * (self.jump ** 2)
    #     #     self.velocity = (self.velocity[0], self.velocity[1] - Force)
    #     #     self.jump = self.jump - 1
    #     # if self.jump < 0:
    #     #     self.mass = -self.mass

    #     # if self.jump == -1:
   
    #     #     self.isJump = False
            
    #     #     self.jump = 5
    #     #     self.mass = 1
    #     # pygame.time.delay(10)
    #     # pygame.display.update() 



    def draw(self, surface):
        surface.blit(self.sprite, self.position)

pygame.init()
player = seagull(320, 240, 0, 0, "seagull.png", 1, 1)


def main():




    while True:
        player.gravity()

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
                elif event.key == pygame.K_SPACE:
                    print(player.isFalling)
                    print(player.isJumping)
                    player.flap()

        
        # Update the player sprite
        player.update()
        
        # Clear the windowda
        window.fill(bgColor)
        
        # Draw the player sprite
        player.draw(window)
        
        # Update the display
        pygame.display.update()






main()



