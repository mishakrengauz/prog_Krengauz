import sys, pygame, random
pygame.init()

size = width, height = 820, 800
speed = [2, 2]
color = 255, 255, 255

screen = pygame.display.set_mode(size)

balls = []
ballrects = []

ball2 = pygame.image.load("soccer_ball.jpeg")
balls.append(ball2)
ball1 = pygame.image.load("intro_ball.gif")
balls.append(ball1)



for ball in balls:

    ballrect = ball.get_rect(center = (random.randint(130, 600), random.randint(150, 600))) #TODO
        #balls.append(ball1)
    ballrects.append(ballrect)



while 1:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    for ballrect in ballrects:

        ballrect = ballrect.move(speed)


        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.fill(color)
        screen.blit(ball, ballrect)
        pygame.display.flip()

