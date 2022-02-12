# make a game with a ball attached to an elastic string
# STANDARD 'STANDARD' stands for parts of code which will be used in most of my pygame programs
# change the x_vel and y_vel to make kx and ky, this code was an attempt to make angry birds


# STANDARD standard initiation and declarations
import pygame, random, sys, math, time

pygame.init()

# STANDARD Time variables
clock = pygame.time.Clock()
FPS = 60

#STANDARD colors
GREEN=(0,200,0)
RED=(250,0,0)
LIGHT_BLUE=(100,100,250)
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (255,100,100)

#STANDARD screen window dimensions
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

GRAVITY = 0
SPRING_CONSTANT = 0.2

# STANDARD make screen window and caption
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('SPRING ELASTIC STRING')

# make a ball projectile class
class Ball():
    def __init__(self,x,y,x_vel,y_vel, radius): # initiation variables passed
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = radius

    def draw(self): # draw the circle and calculate the distance
        pygame.draw.circle(screen,LIGHT_BLUE,(self.x,self.y), self.radius)
        mouse_x,mouse_y = pygame.mouse.get_pos()
        pygame.draw.line(screen,RED,(mouse_x,mouse_y),(self.x,self.y),1)
        distance_x = self.x - mouse_x
        distance_y = self.y - mouse_y
        distance = math.hypot(distance_x,distance_y)
        

    def move(self): #move the cirlce based on velocity and modify velocity on distance
        self.x += self.x_vel
        self.y += self.y_vel
        self.y_vel += GRAVITY

        mouse_x,mouse_y = pygame.mouse.get_pos()
        distance_x = mouse_x - self.x
        distance_y = mouse_y - self.y
        self.y_vel = distance_y*SPRING_CONSTANT
        self.x_vel = distance_x*SPRING_CONSTANT
           
# initialise a ball
projectile = Ball(250,250,5,0,15)
#projectile1 = Ball(50,50,5,0,15) # later make another ball but not overlapping each other

# STANDARD quit function           
def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                sys.exit()

#STANDARD game loop
run = True
while run:
    quit()

    # STANDARD background color    
    screen.fill(WHITE)

    projectile.draw()
    projectile.move()
  
    #STANDARD speed of loop
    clock.tick(FPS)

    #STANDARD Update the screen
    pygame.display.update()
    pygame.display.flip()
