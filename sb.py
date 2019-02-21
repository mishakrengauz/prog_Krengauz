import sys
import pygame
import random

def main():

    pygame.init()

    size = width, height = 1000, 700
    speed1 = [5, 10]
    speed2 = [-2, -2]
    color = 255, 255, 255

    screen = pygame.display.set_mode(size)

    ball1 = pygame.image.load("intro_ball.gif")
    ballrect1 = ball1.get_rect(center = (random.randint(70, 150), random.randint(70, 150)))

    ball2 = pygame.image.load("soccer_ball.jpeg")
    ballrect2 = ball2.get_rect(center = (random.randint(150, 400), random.randint(150, 400)))

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        ballrect1 = ballrect1.move(speed1)
        ballrect2 = ballrect2.move(speed2)
        if ballrect1.left < 0 or ballrect1.right > width:
            speed1[0] = -speed1[0]
        if ballrect1.top < 0 or ballrect1.bottom > height:
            speed1[1] = -speed1[1]

        if ballrect2.left < 0 or ballrect2.right > width:
            speed2[0] = -speed2[0]
        if ballrect2.top < 0 or ballrect2.bottom > height:
            speed2[1] = -speed2[1]

        screen.fill(color)
        screen.blit(ball1, ballrect1)
        screen.blit(ball2, ballrect2)
        pygame.display.flip()


if __name__ == "__main__":
    main()