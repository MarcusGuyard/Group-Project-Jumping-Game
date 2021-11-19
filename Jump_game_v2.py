import pygame
import os

pygame.init()

# Set the size of the game window
window = pygame.display.set_mode((1100, 600))      # set_mode((Tuple))

# Load and scale the background image
bg_img = pygame.image.load('2d_background.jpg')
bg = pygame.transform.scale(bg_img, (1100, 600))

# Load image of character running
jumping = pygame.image.load(os.path.join("razz", "jump2.png"))
jumping_scale = pygame.transform.scale(jumping, (100, 100))


# Load image of character running
def char_img_scaling():
    walk1 = pygame.image.load(os.path.join("razz", "walk1.png"))
    walk1_scale = pygame.transform.scale(walk1, (100, 100))
    walk2 = pygame.image.load(os.path.join("razz", "walk2.png"))
    walk2_scale = pygame.transform.scale(walk2, (100, 100))
    walk3 = pygame.image.load(os.path.join("razz", "walk3.png"))
    walk3_scale = pygame.transform.scale(walk3, (100, 100))
    walk4 = pygame.image.load(os.path.join("razz", "walk4.png"))
    walk4_scale = pygame.transform.scale(walk4, (100, 100))
    return [walk1_scale, walk2_scale, walk3_scale, walk4_scale]


# Set the name of the game window
pygame.display.set_caption("Jump Game")

# Global Variables
x = 250
y = 395

width = 1100
black = (0, 0, 0)

# Clock
clock = pygame.time.Clock()


class Character:
    JUMP_VEL = 3.6
    X_POS = 80
    Y_POS = 450

    def __init__(self, x, y, velx, vely, jump):
        # Walk
        self.x = x
        self.y = y
        self.vel_x = velx
        self.vel_y = vely
        self.jump = jump
        self.face_right = True
        self.stepIndex = 0
        self.count = 0
        self.index = 0
        self.jump_vel = self.JUMP_VEL

        self.image = jumping_scale
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.X_POS
        self.image_rect.y = self.Y_POS

    def move_char(self, userInput):
        # Moving left, right and jumping
        """if userInput[pygame.K_LEFT] and self.x > 0:
            self.x -= self.vel_x
        elif userInput[pygame.K_RIGHT] and self.x < 1050:
            self.x += self.vel_x
        else:
            self.stepIndex = 0"""

        # When player presses space bar set jump to True
        if not self.jump and userInput[pygame.K_SPACE]:
            self.jump = True

        # When jump is True
        if self.jump:
            self.make_a_jump(self.jump)
            """"self.y -= self.vel_y*4
            self.vel_y -= 1
            if self.vel_y < -10:
                self.jump = False
                self.vel_y = 10"""

        """# Eugenio Jag addet then här code to allow the rectangle to jump and move
        # Allows the player to "fly"
        if userInput[pygame.K_UP] and self.y > 0:
            self.y -= self.vel_y
        if userInput[pygame.K_DOWN] and self.y < 455:  # Eugenio Change from 400 to 455
            self.y += self.vel_y"""

    def draw_char(self):

        if self.stepIndex >= 4:
            self.stepIndex = 0
        if self.jump:
            window.blit(jumping_scale, (self.x, self.y))
        elif self.face_right:
            window.blit(char_img_scaling()[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1

    def make_a_jump(self, jump):

        self.image_rect.y -= self.jump_vel
        self.jump_vel -= 0.01
        if self.jump_vel < -self.JUMP_VEL:
            self.jump = False
            self.jump_vel = self.JUMP_VEL

def draw_game():
    global i

    # Create a black canvas behind the background picture
    window.fill(black)

    # The first background picture
    window.blit(bg, (i, 0))

    # Repeat the first background picture in a "slideshow"
    window.blit(bg, (width + i, 0))

    # Loop the background pic infinitely
    if i == -width:
        window.blit(bg, (width + i, 0))
        i = 0
    i -= 1

    # Eugenio add these code  to call the draw_game function
    player.draw_char()
    pygame.time.delay(30)
    pygame.display.update()


i = 0
player = Character(250, 395, 10, 10, False)


# The application start here
def main():

    # Main Loop
    # While run is True the game will run
    run = True
    while run:

        # pygame.QUIT = the red x button will close the window because run will be False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Allow the player to control the character
        userInput = pygame.key.get_pressed()

        # Movement
        player.move_char(userInput)

        # Draw game in window
        draw_game()


if __name__ == '__main__':
    main()