import pygame
import random
import sys

pygame.init()
screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("Matching Game Layout")

font = pygame.font.SysFont("Italic", 40)


subway = pygame.image.load("L.5/ssurfer.png")
candy = pygame.image.load("L.5/ccrush.jpg")
temple = pygame.image.load("L.5/trun.png")
ludo = pygame.image.load("L.5/ludo.png")
screen.blit(ludo,(120,50))
screen.blit(temple,(120,160))
screen.blit(candy,(120,270))
screen.blit(subway,(120,380))

te = font.render("Temple Run",False,"white")
lu = font.render("Ludo",False,"white")
ca = font.render("Candy Crush",False,"white")
su = font.render("Subway Surfers",False,"white")
screen.blit(te,(600, 85))
screen.blit(lu,(600,185))
screen.blit(su,(600,285))
screen.blit(ca,(600,400))

lbox = pygame.Rect(120, 50, 100, 80)
tbox = pygame.Rect(120, 160, 100, 80)
cbox = pygame.Rect(120, 270, 100, 80)
sbox = pygame.Rect(120, 380, 100, 80)

ttbox = pygame.Rect(600,85, 150, 50)
ltbox = pygame.Rect(600, 185,150, 50)
st = pygame.Rect(600, 285,150, 50)
ct = pygame.Rect(600, 400,150, 50)
templrun = {"name":tbox,"clicked":False}
boxes = {"ludo":{"name":lbox,"clicked":False},"templerun":templrun,"candy":{"name":cbox,"clicked":False},"Subway":{"name":sbox,"clicked":False} }
tboxed = {"templerun":{"name":ttbox,"clicked":False},"ludo":{"name":ltbox,"clicked":False},"Subway":{"name":st,"clicked":False},"candy":{"name":ct,"clicked":False} }
while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos=pygame.mouse.get_pos()
            for keys in boxes:
              if boxes[keys]["name"].collidepoint(mousepos) and boxes[keys]["clicked"]==False:
               pygame.draw.circle(screen,"white",mousepos,4)
               boxes[keys]["clicked"]=True
               print(boxes)
        if event.type == pygame.MOUSEBUTTONUP:
            mousepos2 = pygame.mouse.get_pos()
            for keys in tboxed:
              if tboxed[keys]["name"].collidepoint(mousepos2) and tboxed[keys]["clicked"]==False:
               pygame.draw.circle(screen,"white",mousepos2,4)   
               pygame.draw.line(screen,"white",mousepos,mousepos2,2)   
               tboxed[keys]["clicked"]=True  

        pygame.display.update()

