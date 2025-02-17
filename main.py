# libraries
import pygame
import pygame.freetype
from random import randint
from pygame import mixer

# Variables globales
windowWidth = 400
windowHeight = 600
fps = 60
speed = 0
debutOiseau = False
birdPositionX = 50
birdPositionY = 300
pipeW = 130
pipeH = 500
score=0
bestScore=0
heightOfOptions=20
clock = pygame.time.Clock()

# fonctions

def makePipe():
    """
    Makes pipes
    """
    y = randint(-150,130)
    tH = pipeUp.get_rect(center=(windowWidth+pipeW//2,y+pipeH+120))
    listeTuyauxHaut.append(tH)
    tD = pipeDown.get_rect(center=(windowWidth+pipeW//2,y))
    listeTuyauxBas.append(tD)


# Initialisation du module
pygame.init()  # intiates all the modules of pygame
# sets the resolution of the window
screen = pygame.display.set_mode((windowWidth, windowHeight))

pygame.display.set_caption("Flappy Bird")
icon = pygame.image.load('flappybird.png')
pygame.display.set_icon(icon)

# Oiseau
birdImg1 = pygame.image.load('birdy1.png')
birdImg1 = pygame.transform.scale(birdImg1, (55, 40))
birdRect1 = birdImg1.get_rect(center=(birdPositionX,birdPositionY))
birdImg2 = pygame.image.load('birdy2.png')
birdImg2 = pygame.transform.scale(birdImg2, (55, 40))
birdRect2 = birdImg2.get_rect(center=(birdPositionX,birdPositionY))
birdImg3 = pygame.image.load('birdy3.png')
birdImg3 = pygame.transform.scale(birdImg3, (55, 40))
birdRect3 = birdImg3.get_rect(center=(birdPositionX,birdPositionY))

option1 = pygame.image.load('option1.png')
option1 = pygame.transform.scale(option1, (170, 125))
optionRect1 = option1.get_rect(topleft=(windowWidth/2-175,windowHeight/2+heightOfOptions))
notSel1 = pygame.image.load('notSelected.png')
notSel1 = pygame.transform.scale(notSel1, (170, 125))
notSelRect1 = notSel1.get_rect(topleft=(windowWidth/2-175,windowHeight/2+heightOfOptions))
sel1 = pygame.image.load('selected.png')
sel1 = pygame.transform.scale(sel1, (170,125))
selRect1 = sel1.get_rect(topleft=(windowWidth/2-175,windowHeight/2+heightOfOptions))
hover1 = pygame.image.load('hover.png')
hover1 = pygame.transform.scale(hover1,(170,125))
hoverRect1 = hover1.get_rect(topleft=(windowWidth/2-175,windowHeight/2+heightOfOptions))

option2 = pygame.image.load('option2.png')
option2 = pygame.transform.scale(option2, (170, 125))
optionRect2 = option2.get_rect(topleft=(windowWidth/2+5,windowHeight/2+heightOfOptions))
notSel2 = pygame.image.load('notSelected.png')
notSel2 = pygame.transform.scale(notSel2, (170, 125))
notSelRect2 = notSel2.get_rect(topleft=(windowWidth/2+5,windowHeight/2+heightOfOptions))
sel2 = pygame.image.load('selected.png')
sel2 = pygame.transform.scale(sel2, (170,125))
selRect2 = sel2.get_rect(topleft=(windowWidth/2+5,windowHeight/2+heightOfOptions))
hover2 = pygame.image.load('hover.png')
hover2 = pygame.transform.scale(hover2,(170,125))
hoverRect2 = hover2.get_rect(topleft=(windowWidth/2+5,windowHeight/2+heightOfOptions))

option3 = pygame.image.load('option3.png')
option3 = pygame.transform.scale(option3, (170, 125))
optionRect3 = option3.get_rect(center=(windowWidth/2,windowHeight/2+195+heightOfOptions))
notSel3 = pygame.image.load('notSelected.png')
notSel3 = pygame.transform.scale(notSel3, (170, 125))
notSelRect3 = notSel3.get_rect(center=(windowWidth/2,windowHeight/2+195+heightOfOptions))
sel3 = pygame.image.load('selected.png')
sel3 = pygame.transform.scale(sel3, (170,125))
selRect3 = sel3.get_rect(center=(windowWidth/2,windowHeight/2+195+heightOfOptions))
hover3 = pygame.image.load('hover.png')
hover3 = pygame.transform.scale(hover3,(170,125))
hoverRect3 = hover3.get_rect(center=(windowWidth/2,windowHeight/2+195+heightOfOptions))


#Sound
soundHit=mixer.Sound('sfx_hit.wav')
soundFlap=mixer.Sound('sfx_wing.wav')
soundPoint=mixer.Sound('sfx_point.wav')


# Tuyaux
pipeUp = pygame.image.load('pipeDown.png')
pipeUp = pygame.transform.scale(pipeUp, (pipeW, pipeH))
pipeDown = pygame.image.load('pipe.png')
pipeDown = pygame.transform.scale(pipeDown, (pipeW, pipeH))



#Texte
gameFont = pygame.freetype.Font("PixelGameFont.ttf", 25)
scoreFont = pygame.freetype.Font("PixelGameFont.ttf", 30)
font = pygame.freetype.Font("PixelGameFont.ttf", 19)
#Photo Text
title=pygame.image.load('flappyTitle.png')
title=pygame.transform.scale(title,(250,65))
gOver=pygame.image.load('gameOver.png')
gOver=pygame.transform.scale(gOver,(250,250))

#Background
bg1 = pygame.image.load('background.png').convert()
bg1 = pygame.transform.scale(bg1, (1080, 600))
bgm1 = bg1.get_rect()
bg2 = pygame.image.load('background.png').convert()
bg2 = pygame.transform.scale(bg2, (1080, 600))
bgm2 = bg2.get_rect()


listeTuyauxHaut = []
listeTuyauxBas = []

#Default bird
bird=birdImg1
birdBox=birdRect1
bird1=False
bird2=True
bird3=True

running = True
showMenu = False
bgMove=False
iExist=False #Initializes the counter when space is pressed
i = 512   #c'est un compteur, il incrémente 60 par seconde.

#Default colours of the options
colour1=notSel1
colourRect1=notSelRect1
colour2=notSel2
colourRect2=notSelRect2
colour3=notSel3
colourRect3=notSelRect3

#Pause/Play
pause=False

spacePressed = False
while running:
    
    # Vérifications d'actions
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and showMenu==False and pause==False:
                spacePressed = True
                debutOiseau = True
                iExist=True
                bgMove=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and showMenu:
                listeTuyauxHaut.clear()
                listeTuyauxBas.clear()
                showMenu=False
                birdBox = bird.get_rect(center=(birdPositionX,birdPositionY))
                i = 512
                score=0
            if event.key == pygame.K_p:
                if pause==False:
                    pause=True
                else:
                    pause=False
                
        #Checks if mouse is hovering over the options
        elif event.type == pygame.MOUSEMOTION:
            colour1=notSel1
            colourRect1=notSelRect1
            colour2=notSel2
            colourRect2=notSelRect2
            colour3=notSel3
            colourRect3=notSelRect3
            if optionRect1.collidepoint(event.pos) and bird1:
                colour1=hover1
                colourRect1=hoverRect1
            elif optionRect2.collidepoint(event.pos) and bird2:
                colour2=hover2
                colourRect2=hoverRect2
            elif optionRect3.collidepoint(event.pos) and bird3:
                colour3=hover3
                colourRect3=hoverRect3
            
        #Checks if Mouse button is pressed
        if event.type == pygame.MOUSEBUTTONDOWN:
            colour1=notSel1
            colourRect1=notSelRect1
            colour2=notSel2
            colourRect2=notSelRect2
            colour3=notSel3
            colourRect3=notSelRect3
            if optionRect1.collidepoint(event.pos):
                colour1=sel1
                colourRect1=selRect1
                bird=birdImg1
                birdBox=birdRect1
                bird2=True
                bird1=False
                bird3=True
            elif optionRect2.collidepoint(event.pos):
                colour2=sel2
                colourRect2=selRect2
                bird=birdImg2
                birdBox=birdRect2
                bird2=False
                bird1=True
                bird3=True
            elif optionRect3.collidepoint(event.pos):
                colour3=sel3
                colourRect3=selRect3
                bird=birdImg3
                birdBox=birdRect3
                bird2=True
                bird1=True
                bird3=False
    
    if iExist:
        # Gestion du temps
        i += 1
    
    #Changes the selected option's border colour
    if bird1==False:
        colour1=sel1
        colourRect1=selRect1
    elif bird2==False:
        colour2=sel2
        colourRect2=selRect2
    elif bird3==False:
        colour3=sel3
        colourRect3=selRect3
    
    
    #Making background image move continuously
    if showMenu==False and bgMove and pause==False:
        bgm1=bgm1.move((-1,0))
        bgm2=bgm2.move((-1,0))
        if bgm1.x==(windowWidth-1080):
            bgm2.x=windowWidth
        if bgm2.x==(windowWidth-1080):
            bgm1.x=windowWidth
    
    
        
    
    
    # Oiseau
    birdBox = birdBox.move((0,speed))
    if pause:
        speed=0
    if showMenu:
        speed=0
    else:
        if debutOiseau == True:
            speed += 0.2
        if spacePressed and pause==False:
            soundFlap.play()
            speed = -4
            spacePressed = False
    
    # Création de tuyaux supplémentaires
    if iExist and showMenu==False:
        if i % (randint(2,3)*60) == 0 or i == 513:
            makePipe()
            i=0
    
    # Images
    screen.fill((255, 255, 255))  # background colour
    #Displays the background
    screen.blit(bg1, bgm1)
    screen.blit(bg2, bgm2)
    screen.blit(bird, birdBox) # Oiseau
    
    if pause:
        i=0
        bgm1=bgm1.move((0,0))
        bgm2=bgm2.move((0,0))
    
    
    # Tuyaux
    for index in range(len(listeTuyauxBas)):
        if showMenu or pause:
            listeTuyauxBas[index] = listeTuyauxBas[index].move((0,0))
            listeTuyauxHaut[index] = listeTuyauxHaut[index].move((0,0))
        else:
            listeTuyauxBas[index] = listeTuyauxBas[index].move((-2,0))
            listeTuyauxHaut[index] = listeTuyauxHaut[index].move((-2,0))
        if listeTuyauxBas[index].x==10 and showMenu==False:
            soundPoint.play()
            score+=1
            if  bestScore<=score:
                bestScore=score
        screen.blit(pipeDown,listeTuyauxBas[index])
        screen.blit(pipeUp,listeTuyauxHaut[index])
    #Collision
    if (birdBox.collidelist(listeTuyauxBas)!=-1 or birdBox.collidelist(listeTuyauxHaut)!=-1 or birdBox.y<-20 or birdBox.y>windowHeight+20) and showMenu==False:
        
        soundHit.play()
        showMenu=True
        
    if showMenu==False:
        textSurface, rect = gameFont.render("SCORE : "+str(score), (0, 0, 0))
        screen.blit(textSurface, (10, 35))
    else: #Menu
        
            
        scoreText, rect = scoreFont.render("SCORE : "+str(score), (0, 0, 0))
        bestScoreText, rect = scoreFont.render("BEST SCORE : "+str(bestScore), (0, 0, 0))
        screen.blit(scoreText, (windowWidth/2-72, windowHeight/2-10))
        screen.blit(title, (windowWidth/2-125, 50))
        screen.blit(gOver, (windowWidth/2-125, 50))
        screen.blit(bestScoreText, (windowWidth/2-118, 230))
        bgm1=bgm1.move((0,0))
        bgm2=bgm2.move((0,0))
    if showMenu:
        screen.blit(option1, optionRect1)
        screen.blit(colour1,colourRect1)
        screen.blit(option2, optionRect2)
        screen.blit(colour2,colourRect2)
        screen.blit(option3, optionRect3)
        screen.blit(colour3,colourRect3)
    
    if debutOiseau==False:
        normalText, rect = font.render("Tap space to start playing & P to pause")
        screen.blit(normalText, (5,5))
        pygame.display.flip()
    elif showMenu==True:
        normalText, rect = font.render("Tap space to replay, you can select your")
        screen.blit(normalText, (5,5))
        selectText, rect = font.render("bird by clicking with mouse.")
        screen.blit(selectText, (5,25))
        pygame.display.flip()
    pygame.display.update()  # to update the display
    clock.tick(fps)

pygame.quit()