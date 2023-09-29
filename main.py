import pygame
import random

#FIX SCORE NOT SHOWING
#ADD POSSIBLE CHANGE IN CHANGE IN Y AFTER HITTING BALL AND HAVING VELOCITY IN THE Y SIMULTANEOUSLY
#CHANGE PONG PADDLE PNG FILES
#INITIALIZE
pygame.init()

# define the RGB value for white,
#  green, blue colour .
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
playerScore = 0
aiScore = 0
font = pygame.font.Font("freesansbold.ttf", 16)
playerScoreX = 125
playerScoreY = 20
aiScoreX = 525
aiScoreY = 20
titleTextX = 310
titleTextY = 525
titleText = font.render("NONSTOP PONG", True, orange)

#AI
aiImg = pygame.image.load("pongPlayers.png")
aiImg = pygame.transform.smoothscale(aiImg, (50, 150))
aiX = 680
aiY_change = 5
aiY = 200

#PLAYER
playerImg = pygame.image.load("pongPlayers.png")
playerImg = pygame.transform.smoothscale(playerImg, (50, 150))
playerX = 35
playerY_change = 0
playerY = 150

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


def player(x, y):
    screen.blit(playerImg, (x, y))


def ai(x, y):
    screen.blit(aiImg, (x, y))


def ball_movement(x, y):
    screen.blit(ballImg, (x, y))


def show_score(playerscorex, playerscorey, playerscore, aiscore, aiscorex, aiscorey):
    playerscore = font.render("Player Score: " + str(playerscore), True, red)
    aiscore = font.render(" AI Score : " + str(aiscore), True, blue)
    screen.blit(playerscore, (playerscorex, playerscorey))
    screen.blit(aiscore, (aiscorex, aiscorey))


running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playerY_change -= 5
            if event.key == pygame.K_DOWN:
                playerY_change += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0
    #PLAYER LOC
    playerY += playerY_change
    player(playerX, playerY)
    if playerY > 415:
        playerY = 415
    if playerY < 0:
        playerY = 0
    #AI LOC AND BEHAVIOR
    if ballX_change > 0 and ballX < 650:
        if aiY is not ballY - 48:
            if aiY > ballY - 48:
                aiY -= aiY_change
            elif aiY < ballY - 48:
                aiY += aiY_change
    elif ballX_change < 0:
        if aiY is not 200:
            if aiY > 200:
                aiY -= aiY_change
            elif aiY < 200:
                aiY += aiY_change
    ai(aiX, aiY)
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
    if playerX - 16 <= ballX <= playerX + 16:
        if (125 + playerY) >= ballY >= playerY - 25:
            if playerY_change > 0:
                ballY_change += abs(ballX_change * 0.15)
            if playerY_change < 0:
                ballY_change -= abs(ballX_change * 0.15)
            ballX_change = ballX_change * -1
            ballX_change += 0.5
    if aiX - 16 <= ballX <= aiX + 16:
        if (125 + aiY) >= ballY >= aiY - 25:
            if aiY_change > 0:
                ballY_change += abs(ballX_change * 0.15)
            if aiY_change < 0:
                ballY_change -= abs(ballX_change * 0.15)
            ballX_change = ballX_change * -1
            ballX_change -= 0.5

    #SHOW SCORE
    show_score(playerScoreX, playerScoreY, playerScore, aiScore, aiScoreX, aiScoreY)

    #UPDATE SCREEN DISPLAY
    pygame.display.update()
    #DISPLAY AND UPDATE SCORE
    if ballX >= 750:
        playerScore += 1
        ballX = 351
        ballY = 255
        start = True
    if ballX <= 0:
        aiScore += 1
        ballX = 351
        ballY = 255
        start = True

    #SET GAME SPEED
    fps = 240
    clock = pygame.time.Clock()
    clock.tick(fps)
