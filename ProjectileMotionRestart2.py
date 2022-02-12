# make elastic string for a ball 
# STANDARD standard initiation and declarations
import pygame, random, sys, math

pygame.init()

# STANDARD Time variables
clock = pygame.time.Clock()
FPS = 70

#STANDARD colors
GREEN=(0,200,0)
RED=(250,0,0)
LIGHT_BLUE=(100,100,250)
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (250,100,100)
BLUE = (0,0,255)

# STANDARD screen window dimensions
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
RADIUS = 20
GRAVITY = 0.2
ELASTIC_CONSTANT = 1/15

# number of attempts and hits
Attempts = 0
Hits = 0 

# STANDARD make screen window and caption
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Hungry Birds')

# Upload and re-size images
background = pygame.image.load("cartoon1.jpg").convert_alpha()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
#bee = pygame.image.load("bee.png").convert_alpha()
#bee = pygame.transform.scale(bee, (70, 50))

# STANDARD quit function           
def quit():
    global Hits,Attempts
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
        if event.type == pygame.KEYDOWN: # to get power at space press
            if event.key == pygame.K_SPACE:
                shoot = True
                Attempts += 1
                return shoot
            if event.key == pygame.K_r: # restart the game and give initial values
                ball.x = 25
                ball.y = SCREEN_HEIGHT - RADIUS
                ball.x_vel = 0
                ball.y_vel = 0
                fruit.colour = LIGHT_BLUE # change the colour of the fruit from RED to LIGHT_BLUE
                Attempts = 0
                Hits = 0
                                

#create a class for ball

class Ball():
    def __init__(self, x, y, x_vel, y_vel, RADIUS):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = RADIUS

    def draw(self):
        pygame.draw.circle(screen,RED,(self.x,self.y), self.radius)
        m_x, m_y = pygame.mouse.get_pos()
        pygame.draw.line(screen, RED, (self.x,self.y), (m_x, m_y), 1)
                    
    def move(self):
        
        if shoot:
            m_x, m_y = pygame.mouse.get_pos()
            dist_x = m_x - ball.x #the distance is calculated with ball.x not with self.x
            dist_y = m_y - ball.y
            self.x_vel = dist_x*ELASTIC_CONSTANT
            self.y_vel = dist_y*ELASTIC_CONSTANT
            self.x += self.x_vel
            self.y += self.y_vel

            
        else:
            
            self.x += self.x_vel # here we use sel.x_vel not ball.x_vel
            self.y += self.y_vel
            self.y_vel += GRAVITY

        # bounce if circle touches right wall
        if(self.x >= (SCREEN_WIDTH - self.radius)):
            self.x = SCREEN_WIDTH - self.radius
            self.x_vel *= -0.75
        # bounce if circle touches left wall  
        if(self.x <= self.radius):
            self.x = self.radius
            self.x_vel *= -0.75
        # bounce if circle touches bottom wall   
        if(self.y >= (SCREEN_HEIGHT - self.radius)):
            self.y = SCREEN_HEIGHT -self.radius # this keeps the ball bouncing higher
            self.y_vel *= -0.75
        # bounce if circle touches top wall      
        if(self.y <= self.radius):
            self.y = self.radius
            self.y_vel *= -0.75


# make class for fruits

class Fruits():
    def __init__(self, colour, x, y, x_vel, y_vel, RADIUS):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.radius = RADIUS
        self.colour = colour
        
    def draw(self):
        pygame.draw.circle(screen,self.colour,(self.x,self.y), self.radius)
                           
    def move(self):
        global Hits, Attempts
        self.x += self.x_vel
        self.y += self.y_vel

        # bounce if circle touches right wall
        if(self.x >= (SCREEN_WIDTH - self.radius)):
            self.x = SCREEN_WIDTH - self.radius
            self.x_vel *= -0.95
        # bounce if circle touches left wall  
        if(self.x <= self.radius):
            self.x = self.radius
            self.x_vel *= -0.95
        # bounce if circle touches bottom wall   
        if(self.y >= (SCREEN_HEIGHT - self.radius)):
            self.y = SCREEN_HEIGHT -self.radius # this keeps the ball bouncing higher
            self.y_vel *= -0.95
        # bounce if circle touches top wall      
        if(self.y <= self.radius):
            self.y = self.radius
            self.y_vel *= -0.95

        # detect collission
        dist_x = ball.x-self.x
        dist_y = ball.y-self.y
        dist = math.hypot(dist_x,dist_y)
        if dist < (ball.radius+self.radius):
            self.colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            Hits += 1
            ball.x_vel *= -1 # bounce the ball back so that there is only one hit mostly
            ball.x -= 5 # to prevent multiple hits with one actual hit
            
    

# put text on the screen

def text():
    global Attempts, Hits
    
    #Title board
    font= pygame.font.SysFont('CalibriBold', 50, False, False)
    text = font.render("HUNGRY BIRDS", True, RED)
    screen.blit(text,[SCREEN_WIDTH//2 - 150,25])
    
    #Instruction board
    font= pygame.font.SysFont('Calibri', 20, False, False)
    text1 = font.render('Spacebar to shoot, "r" to start again, "esc" to quit', True, BLACK)
    screen.blit(text1,[SCREEN_WIDTH//2 - 200,SCREEN_HEIGHT - 25])

    #Score board
    font= pygame.font.SysFont('Calibri', 25, False, False) # font for score board
    text2 = font.render("Attempts = " + str(Attempts), True, WHITE)
    screen.blit(text2,[SCREEN_WIDTH - 200,30])
    
    text3 = font.render("Hits = " + str(Hits), True, WHITE)
    screen.blit(text3,[SCREEN_WIDTH - 200,10])


            
# create a object of class ball
ball = Ball(50,SCREEN_HEIGHT - RADIUS,0,0,RADIUS)
fruit = Fruits((random.randint(0,255),random.randint(0,255),random.randint(0,255)),SCREEN_WIDTH - RADIUS,RADIUS, 0,5,RADIUS-5)
shoot = False


#STANDARD game loop
run = True
while run:
    shoot = quit()

    #STANDARD background color    
    #screen.fill(WHITE)
    screen.blit(background, (0, 0)) # insert background image
    text() # draw text
    ball.draw() # draw ball and line
    ball.move() # move ball

    fruit.draw()
    fruit.move()
    #STANDARD speed of loop
    clock.tick(FPS)

    #STANDARD Update the screen
    pygame.display.update()
    pygame.display.flip()
