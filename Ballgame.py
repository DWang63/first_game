import sys, pygame

# Initialization
run = True
pygame.init()

# Initialize screen variables
size = width, height = 1200, 800
speed = [2, 2] #Default ball speed
black = 0, 0, 0

# Create the screen surface
screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()
old_ball_rect = ballrect


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_UP:
                if speed[0] < -1:
                    speed[0]-=1
                elif speed [0] > 1:
                    speed[0]+=1
                elif speed[0] == 1:
                    speed[0]+=1
                elif speed[0] == -1:
                    speed[0]-=1

                if speed [1] < -1:
                    speed[1]-=1
                elif speed [1] > 1:
                    speed[1]+=1
                elif speed[1] == 1:
                    speed[1]+=1
                elif speed[1] == -1:
                    speed[1]-=1

            elif event.key == pygame.K_DOWN:
                if speed[1] < -1:
                    speed[1]+=1
                elif speed[1] < 1:
                    speed[1]-=1
                elif speed[0] < -1:
                    speed[0]+=1
                elif speed[0] > 1:
                    speed[0]-=1
    

    old_ball_rect = ballrect

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    
    ball_list = [ballrect, old_ball_rect]
    
    pygame.display.update(ball_list)