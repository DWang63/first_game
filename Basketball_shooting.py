import sys, pygame
pygame.init
run = True

#creating screen variables
screen_size = width, height = 1400, 800
ball_speed = [3, 3]
black = 0, 0, 0
screen = pygame.display.set_mode(screen_size)

#loading and setting up the photos
ball = pygame.image.load("Basketball_shooting game/Pixel.ball.png")
#rescaling the photos
ball = pygame.transform.scale(ball, (50, 50))
ballrect = ball.get_rect()
oldballrect = ballrect
ballrect = ballrect.move(100, 650)


basketball_net = pygame.image.load("Basketball_shooting game/Basketball_net.png")
basketball_net = pygame.transform.scale(basketball_net, (200, 300))
basketball_netrect = basketball_net.get_rect()
basketball_netrect = basketball_netrect.move(1180, 250)


arrow = pygame.image.load("Basketball_shooting game/red_arrow.png")
arrow = pygame.transform.scale(arrow, (75, 75))
arrowrect = arrow.get_rect()
arrowrect = arrowrect.move(165, 610)

background = pygame.image.load("Basketball_shooting game/Brick.wall.png")
background = pygame.transform.scale(background, (1400, 800))
background_rect = background.get_rect()

player = pygame.image.load("Basketball_shooting game/basketball.player.png")
player = pygame.transform.scale(player, (100, 300))
player_rect = player.get_rect()
player_rect.bottomleft = screen.get_rect().bottomleft




#game loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    screen.blit(background, background_rect)
    screen.blit(player, player_rect)
    screen.blit(ball, ballrect)
    screen.blit(basketball_net, basketball_netrect)
    screen.blit(arrow, arrowrect)
    pygame.display.update()







# Part 1

# Render a person, a basketball, and a hoop
# Have an arrow off of the ball that reacts to keyboard inputs to indicate the trajectory of the ball

# Part 2
# Holding the space bar locks the arrow, and brings up a power meter that increases until you unpress the space bar

# Part 3
# Have the bar fluctuate back and forth if they don't release