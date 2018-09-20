import sys, pygame
pygame.init
run = True

#creating screen variables
screen_size = width, height = 1400, 800
ball_speed = [3, 3]
black = 0, 0, 0
screen = pygame.display.set_mode(screen_size)

#loading and setting up the photos
ball = pygame.image.load("Pixel.ball.png")
ball = pygame.transform.scale(ball, (50, 50))
#rescaling the photos
ballrect = ball.get_rect()
oldballrect = ballrect

background = pygame.image.load("Brick.wall.png")
background = pygame.transform.scale(background, (1400, 800))
background_rect = background.get_rect()

player = pygame.image.load("basketball.player.png")
player = pygame.transform.scale(player, (100, 300))
player_rect = player.get_rect()
player_rect.bottomleft = screen.get_rect().bottomleft




#game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(background, background_rect)
    screen.blit(player, player_rect, )
    screen.blit(ball, ballrect)
    
    pygame.display.update()







# Part 1

# Render a person, a basketball, and a hoop
# Have an arrow off of the ball that reacts to keyboard inputs to indicate the trajectory of the ball

# Part 2
# Holding the space bar locks the arrow, and brings up a power meter that increases until you unpress the space bar

# Part 3
# Have the bar fluctuate back and forth if they don't release