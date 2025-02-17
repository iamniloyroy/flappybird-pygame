import pygame
import pygame.freetype
pygame.init()#intiates all the modules of pygame
windowW=600
screen=pygame.display.set_mode((400,windowW))#sets the resolution of the window
clock = pygame.time.Clock()

# Title
pygame.display.set_caption("Hello World")

gameFont = pygame.freetype.Font("LoveCraft.ttf", 24)


# bg1 = pygame.image.load('background.png')
# bg1 = pygame.transform.scale(bg1, (1080, 600))
# bgm1 = bg1.get_rect()
# bg2 = pygame.image.load('background.png')
# bg2 = pygame.transform.scale(bg2, (1080, 600))
# bgm2 = bg2.get_rect()

birdImg = pygame.image.load('option1.png')
birdImg = pygame.transform.scale(birdImg, (110, 80))
birdRect = birdImg.get_rect(topleft=(100,100))
sel = pygame.image.load('notSelected.png')
sel = pygame.transform.scale(sel, (110, 80))
selRect = birdImg.get_rect(birdRect)

# Font
# font=pygame.font.Font('font-file',fontSize)
# showText=font.render(text,visibilty(boolean),(r,g,b))
# screen.blit(showText,(positionx,positiony))

# Sound
# from pygame import mixer
# mixer.music.load(filename)
# mixer.music.play(-1)
# sound=mixer.Sound(filename)
# sound.play()



# Image
# Img=pygame.image.load('nameofthefile.png')
# screen.blit(Img,(positionX,positionY))#to be put in the loop

#icon
# icon=pygame.image.load('filename.jpg')
# pygame.display.set_icon(icon)

running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
    
    screen.fill((255,255,255))
    
    screen.blit(birdImg, birdRect)
    screen.blit(sel,selRect)
    pygame.display.update()#to update the display
    clock.tick(60)
pygame.quit()