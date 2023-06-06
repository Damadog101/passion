import pygame
import sys
import time

#game intentions will be to avoid the balloons coming from bottom of screen

bgColor = (115, 199, 199)
screen = pygame.display.set_mode((500, 500))

x = 100
y = 100

screenWidth = 1000
screenHeight = 600
window = pygame.display.set_mode((screenWidth, screenHeight))




class seagull(pygame.sprite.Sprite):
    def __init__(self, x, y, dx, dy, image):
        super().__init__()
        self.position = (x, y)
        self.velocity = (dx, dy) 
        self.sprite = pygame.image.load(image)
        self.isJumping = False
        self.isFalling = True
        self.startTime = time.time()


    def update(self):

        #Checks collisions on screen edges
        self.position = ((self.position[0] + self.velocity[0]), (self.position[1] + self.velocity[1]))
        if self.position[0] + 200 > screenWidth:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.position[0] < 0:
            self.velocity = (-self.velocity[0], self.velocity[1])
        if self.position[1] + 125 > screenHeight:
            self.velocity = (self.velocity[0], 0)
            self.position = (self.position[0], self.position[1] - 1)  
        if self.position[1] < 0:
            self.velocity = (self.velocity[0], 0)
            self.position = (self.position[0], self.position[1] + 10)




        #Supposed to check jumping but no work well
        if self.isJumping and not self.isFalling:
            self.velocity = (self.velocity[0], -1)
            if (time.time() - self.startTime) > 1:
                print(time.time() - self.startTime)
                print("fall:", self.isFalling, "jump:", self.isJumping, "velocity", self.velocity[1])

                self.isJumping = False
                self.isFalling = True
                self.gravity()
                print("fall:", self.isFalling, "jump:", self.isJumping, "velocity", self.velocity[1])



            


    def moveLeft(self):
        self.velocity = (-1, self.velocity[1])



    def moveRight(self):
        self.velocity = (1, self.velocity[1])

    def gravity(self):
        # print("gravity won")
        if self.isFalling is True and self.isJumping is False:
            self.velocity = (self.velocity[0], 1)


    def flap(self):
        self.isFalling = False
        self.isJumping = True



    def draw(self, surface):
        surface.blit(self.sprite, self.position)

pygame.init()
player = seagull(320, 240, 0, 0, "seagull.png")



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
                elif event.key == pygame.K_w:
                    player.isJumping = True
                    player.isFalling = False
                    # print("fall:", player.isFalling, "jump:", player.isJumping)
        jump = str(player.isJumping)
        fall = str(player.isFalling)
        pygame.display.set_caption(jump + fall)


        
        # Update the player sprite
        player.update()
        
        # Clear the windowda
        window.fill(bgColor)
        
        # Draw the player sprite
        player.draw(window)
        
        # Update the display
        pygame.display.update()











main()



