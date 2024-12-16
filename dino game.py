#-----------------------------------------------------------------------------
# Name:        Barbie Run
# Purpose:     A dino run with barbie and extra features
#
# Author:      Yana P
# Created:     22-April-2023
# Updated:     22-April-2023
#-----------------------------------------------------------------------------
#I think this project deserves a level 4+ because it has all needed features for a level 4 and more. Not only does it cover all
#requirements such as elements of randomeness(randomized height of blocks and heel appearance), very polished and efficent code,
#a nice UI(I worked hard to make it barbie themed and so it would look cohesive). Aside from that it has extra features
#such as different game modes, heels that offer extra score if picked up and an increased speed/difficulty after a certain point
#(a score of 1500). As well as that it has a score that is displayed during game play and at the final screen. On top of that
#you can use the ESC key to leave the homescreen which is another nice small improvement. You can also go back from the loss
#screen to the home screen as to change the gamemode if you'd prefer. This game has a replayability aspect and it 
#deserves a level 4+ because of the amount of extra work I put into it:D.
#
#Features Added:
#  3 individual gamemodes
#  Heels than can be picked up for extra score
#  The game speeds up after a certain point
#  An ESC to leave fucntion on the homescreen
#  The ability to go back and change your gamemode after you lose
#  WAD keys added instead of just a jump
#  The positon of the heel will randomize so that its not consistenly coming at you at once
#  The height of the blocks will randomize so that its not the same obstacle over and over again
#  Cute graphics('Barbie' thats actually just princess peach)
#  Can be replayed without restarting the game
#-----------------------------------------------------------------------------
import pygame
import random
import sys
import os

def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    pygame.font.init()
    surfaceSize = 580   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
    
    #-----------------------------Program Variable Initialization----------------------------#
#   Font
    font = pygame.font.Font(None, 36)
#   Images
    backgroundStart = pygame.image.load('images/pinkhills.png')
    namelogo = pygame.image.load('images/barbie.png')
    run = pygame.image.load('images/result.png')
    start1 = pygame.image.load('images/start.png')
    htp = pygame.image.load('images/htp.png')
    barbie = pygame.image.load('images/princess.png')
    block = pygame.image.load('images/block.png')
    lost = pygame.image.load('images/lost.png')
    playagain = pygame.image.load('images/playagain.png')
    gamemode = pygame.image.load('images/gamemode.png')
    homescreen = pygame.image.load('images/homescreen.png')
    instructions = pygame.image.load('images/instructions.png')
    easy = pygame.image.load('images/easy.png')
    medium = pygame.image.load('images/medium.png')
    hard = pygame.image.load('images/hard.png')
    back = pygame.image.load('images/back.png')
    heel = pygame.image.load('images/heel.png')
#     Jumping Variables
    gravity = 10
    isJump = False
    jumpCount = 10
#     Ground Variable
    rectPos = [0, 400, 580, 400]
#     Princess peach(barbie) variables
    x = 150
    y = 350
    width = 80
    height = 70
#     Block variables
    x1 = -50
    y1 = 0
    widthP = 45
    heightP = 300
#     Game Variables
    gameState = 0
    score = 0
    mouse = []
    gmode = 1
    heelx = 1000
    heely = 250
    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        pygame.time.delay(30)
        #-----------------------------Event Handling-----------------------------------------#
        ev = pygame.event.poll()    
        if ev.type == pygame.QUIT:  
            break
        if(gameState == 0):
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    break
#             Home screen Images
            mainSurface.blit(backgroundStart, (0,0))    
            mainSurface.blit(namelogo, (90,40))
            mainSurface.blit(run, (290,110))
            pygame.draw.rect(mainSurface, (198, 115, 136), ((200, 250), (170, 45)))
            pygame.draw.rect(mainSurface, (198, 115, 136), ((200, 335), (170, 90)))
            pygame.draw.rect(mainSurface, (198, 115, 136), ((200, 470), (170, 45)))
            mainSurface.blit(start1, (220, 235))
            mainSurface.blit(htp, (190,310))
            mainSurface.blit(gamemode, (200,465))
            escape = font.render('Press ESCAPE to exit', True, (255, 255, 255))
            mainSurface.blit(escape, (10, 10))
#             Pressing the home screen buttons
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                mouse = list(pygame.mouse.get_pos())
                if(mouse[0] >= 200) and (mouse[0] <= 370) and (mouse[1] >= 250) and (mouse[1] <= 295):
                    score = 0
                    x = 150
                    x1 = -50
                    heelx = 1000
                    gameState = 1 
                if(mouse[0] >= 200) and (mouse[0] <= 370) and (mouse[1] >= 335) and (mouse[1] <= 425):
                    gameState = 3
                if(mouse[0] >= 200) and (mouse[0] <= 370) and (mouse[1] >= 450) and (mouse[1] <= 515):
                    gameState = 4
                    
#                 Actual Gameplay
        if(gameState == 1):
#             Draw Blocks/Barbie
            mainSurface.fill((53, 80, 112))
            mainSurface.blit(backgroundStart, (0,0))    
            mainSurface.blit(block, (x1, y1))
            pygame.draw.rect(mainSurface, (128, 70, 83), rectPos)
            mainSurface.blit(barbie, (x,y))
            mainSurface.blit(heel, (heelx, heely))
            
#             Score
            score = score + 1
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            mainSurface.blit(score_text, (10, 10))

            
#             Jumping/Moving function
            keys = pygame.key.get_pressed()
                
            if keys[pygame.K_a] and x > gravity: 
                x -= gravity
            if keys[pygame.K_d] and x < 580 - (gravity*5): 
                x += gravity
            if not(isJump): 
                if keys[pygame.K_w]:
                    isJump = True
            else:
                if jumpCount >= -10:
                    y -= (jumpCount * abs(jumpCount)) * 0.4
                    jumpCount -= 1
                else: 
                    jumpCount = 10
                    isJump = False
#                     Heel Speed
            heelx -= (6*gmode)
#                     Speed of Block
            x1 -= (6*gmode)
#                     Randomise Block size
            if(x1 <= -30):
                x1 = 550
                y1 = random.randint(300, 360)
                
#                 Collison Detection for Block
            if (x + 30 >= x1) and (x + 30 <= x1 + 50):
                if (y >= y1 - 20) and (y <= y1 + 50):
                    gameState = 2
#                     Collison Detection for Heel + Heel Position Randomization
            if (x + 30 >= heelx) and (x + 30 <= heelx + 50):
                if (y >= heely - 20) and (y <= heely + 65):
                    score += 200
                    heelx = random.randint(1000, 2000)
            if (heelx <= -40):
                    heelx = random.randint(1000, 2000)
#                     Speeding Up After A Certain Point
            if(score >= 1500):
                heelx -= (8*gmode)
                x1 -= (8*gmode)
#                     Loss screen
        if(gameState == 2):
#             Play again button
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                mouse = list(pygame.mouse.get_pos())
                if(mouse[0] >= 200) and (mouse[0] <= 370) and (mouse[1] >= 250) and (mouse[1] <= 295):
                    x1 -= 6
                    x1 = 550
                    y1 = random.randint(300, 360)
                    score = 0
                    x = 150
                    heelx = 1000
                    gameState = 1
#                     Home screen button
                if(mouse[0] >= 200) and (mouse[0] <= 370) and (mouse[1] >= 340) and (mouse[1] <= 440):
                    gameState = 0
#                     Loss screen images
            mainSurface.fill((53, 80, 112))
            mainSurface.blit(backgroundStart, (0,0))
            pygame.draw.rect(mainSurface, (198, 115, 136), ((200, 250), (170, 45)))
            pygame.draw.rect(mainSurface, (198, 115, 136), ((200, 350), (170, 90)))
            mainSurface.blit(lost, (50,0))
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            mainSurface.blit(score_text, (230, 170))
            mainSurface.blit(playagain, (200, 240))
            mainSurface.blit(homescreen, (200, 340))
#             How to Play screen
        if(gameState == 3):
            mainSurface.fill((53, 80, 112))
            mainSurface.blit(backgroundStart, (0,0))
            mainSurface.blit(instructions, (37,37))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                mouse = list(pygame.mouse.get_pos())
                if(mouse[0] >= 235) and (mouse[0] <= 345) and (mouse[1] >= 465) and (mouse[1] <= 530):
                    gameState = 0
#             Gamemode Screen
        if(gameState == 4):
            score = 0
            x = 150
            x1 = -50
            heelx = 1000
            mainSurface.fill((53, 80, 112))
            mainSurface.blit(backgroundStart, (0,0))
            mainSurface.blit(gamemode, (200,40))
            mainSurface.blit(easy, (235, 170))
            mainSurface.blit(medium, (210, 270))
            mainSurface.blit(hard, (225, 370))
            if(ev.type == pygame.MOUSEBUTTONDOWN):
                mouse = list(pygame.mouse.get_pos())
                if(mouse[0] >= 235) and (mouse[0] <= 345) and (mouse[1] >= 170) and (mouse[1] <= 230):
                    gameState = 0
                    gmode = 1
                if(mouse[0] >= 215) and (mouse[0] <= 365) and (mouse[1] >= 270) and (mouse[1] <= 330):
                    gameState = 0
                    gmode = 2
                if(mouse[0] >= 225) and (mouse[0] <= 345) and (mouse[1] >= 370) and (mouse[1] <= 430):
                    gameState = 0
                    gmode = 4
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()







