import pygame
import random

#FIX SCORE NOT SHOWING, ADD POSSIBLE CHANGE IN Y AFTER HITTING BALL AND HAVING VELOCITY IN THE Y
#INITIALIZE
pygame.init()

# define the RGB value for white,
#  green, blue, red, and orange colour .
white = (255, 255, 255)
green = (0, 255, 0)
blue = (21, 36, 173)
red = (255, 0, 13)
orange = (255, 89, 0)

#CONDITIONAL VARIABLES (OCCUR CERTAIN NUMBER OF TIMES)
start = True
#SCREEN
screen = pygame.display.set_mode((750, 563))

#BACKGROUND
background = pygame.image.load("pongBackground.png")

#SCREEN TEXT
p1Score = 0
p2Score = 0
font = pygame.font.Font("freesansbold.ttf", 16)
p1ScoreX = 125
p1ScoreY = 20
p2ScoreX = 500
p2ScoreY = 20
titleTextX = 310
titleTextY = 525
titleText = font.render("Nonstop Pong", True, orange)

#PLAYER 2
p2Img = pygame.image.load("pongPlayers.png")
p2Img = pygame.transform.smoothscale(p2Img, (50, 150))
p2X = 680
p2Y_change = 0
p2Y = 200

#PLAYER
p1Img = pygame.image.load("pongPlayers.png")
p1Img = pygame.transform.smoothscale(p1Img, (50, 150))
p1X = 35
p1Y_change = 0
p1Y = 150

#PONG BALL
ballImg = pygame.image.load("ball.png")
ballImg = pygame.transform.smoothscale(ballImg, (50, 50))
ballX = 351
ballX_change = 0
ballY = 255
ballY_change = 0
#GAME ICON
icon = pygame.image.load("pongPlayers.png")
pygame.display.set_icon(icon)
#NAME OF GAME
pygame.display.set_caption("Pong")


def p1(x, y):
    screen.blit(p1Img, (x, y))


def p2(x, y):
    screen.blit(p2Img, (x, y))


def ball_movement(x, y):
    screen.blit(ballImg, (x, y))


def show_score(p1scorex, p1scorey, p1score, p2score, p2scorex, p2scorey):
    p1score = font.render("Player 1 Score: " + str(p1score), True, red)
    p2score = font.render("Player 2 Score: " + str(p2score), True, blue)
    screen.blit(p1score, (p1scorex, p1scorey))
    screen.blit(p2score, (p2scorex, p2scorey))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                p1Y_change -= 5
            if event.key == pygame.K_s:
                p1Y_change += 5
            if event.key == pygame.K_UP:
                p2Y_change -= 5
            if event.key == pygame.K_DOWN:
                p2Y_change += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                p1Y_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                p2Y_change = 0
    #PLAYER 1 LOC
    p1Y += p1Y_change
    p1(p1X, p1Y)
    if p1Y > 415:
        p1Y = 415
    if p1Y < 0:
        p1Y = 0
    #P2 LOC AND BEHAVIOR
    p2Y += p2Y_change
    p2(p2X, p2Y)
    if p2Y > 415:
        p2Y = 415
    if p2Y < 0:
        p2Y = 0
    #BALL LOC AND BEHAVIOR
    if start is True:
        start = False
        if random.randint(0, 1) == 1:
            ballX_change = -5
        else:
            ballX_change = 5
        ballY_change = random.randint(3, 7)
    if ballY <= 0:
        ballY_change = ballY_change * -1
    if ballY >= 516:
        ballY_change = ballY_change * -1
    ballX += ballX_change
    ballY += ballY_change
    ball_movement(ballX, ballY)

    #COLLISION BEHAVIOR
    if p1X - 20 <= ballX <= p1X + 20:
        if (125 + p1Y) >= ballY >= p1Y - 25:
            if p1Y_change > 0:
                ballY_change += abs(ballX_change * 0.15)
            if p1Y_change < 0:
                ballY_change -= abs(ballX_change * 0.15)
            ballX_change = ballX_change * -1
            ballX_change += 0.5
    if p2X - 20 <= ballX <= p2X + 20:
        if (125 + p2Y) >= ballY >= p2Y - 25:
            if p1Y_change > 0:
                ballY_change += abs(ballX_change * 0.15)
            if p1Y_change < 0:
                ballY_change -= abs(ballX_change * 0.15)
            ballX_change = ballX_change * -1
            ballX_change -= 0.5

    #SHOW TEXT
    show_score(p1ScoreX, p1ScoreY, p1Score, p2Score, p2ScoreX, p2ScoreY)

    #UPDATE SCREEN DISPLAY
    pygame.display.update()
    #UPDATE SCORE
    if ballX >= 750:
        p1Score += 1
        ballX = 351
        ballY = 255
        start = True
    if ballX <= 0:
        p2Score += 1
        ballX = 351
        ballY = 255
        start = True

    #SET GAME SPEED
    fps = 300
    clock = pygame.time.Clock()
    clock.tick(fps)
