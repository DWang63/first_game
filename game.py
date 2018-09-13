import sys, pygame
pygame.init()

size = width, height = 1200, 800
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.jpg")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()


# Update only where the rectangle used to be and where the rectangle is now


# If you click or you press a key, the ball increases or decreases in speed. But nothing happens if you try to decrease past 0
# Alternative: Click reverse the direction