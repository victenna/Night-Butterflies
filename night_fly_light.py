import pygame,random,time
from math import *
pygame.init()
screen = pygame.display.set_mode((1200, 1200))
bgr=pygame.image.load("bg.png")
light=pygame.image.load('light.png')
#background_image=pygame.transform.scale(background_image,(1400,1200))
clock = pygame.time.Clock()

class Flyy(pygame.sprite.Sprite):
    def __init__(self,image,scale,A,B):
        super().__init__()
        self.image=pygame.image.load(image)
        self.image=pygame.transform.scale(self.image,(scale,scale))
        self.start_image=self.image
        #self.image1=self.image#!!!!!!!!!!!!!!!!!!!
        self.rect=self.image.get_rect()
        x=random.randint(A,B)
        y=random.randint(A,B)
        dx=random.randint(-15,15)
        dy=random.randint(-15,15)
        self.x,self.y=x,y
        self.rect.center=(self.x,self.y)
        self.dx,self.dy=dx,dy
    def update(self):#,D,C):
        self.x+=self.dx
        self.y+=self.dy
        #if self.x>1000 or self.x<50: self.dx=-self.dx #!!!!!!!!!!!!!!!
        #if self.y>800 or self.y<50: self.dy=-self.dy #!!!!!!!!!!!!!!!!!!!!
        #self.rect.center=(self.x,self.y)
        
    def borders(self,C,D,x_mouse,y_mouse):
        self.x+=self.dx
        self.y+=self.dy
        if self.x<(x_mouse-C) or self.x>(x_mouse+D): self.dx=-self.dx #!!!!!!!!!!!!!!!
        if self.y<(y_mouse-C) or self.y>(y_mouse+D) : self.dy=-self.dy #!!!!!!!!!!!!!!!!!!!!
        self.rect.center=(self.x,self.y)
        
        
    def rotate(self):
        degree=atan2(-self.dy,self.dx)*180/3.14159-90
        self.image=pygame.transform.rotate(self.start_image,degree)
        self.rect=self.image.get_rect(center=(self.x,self.y))
        
    def move(self,dx,dy) :
        self.x +=dx
        self.y += dy
    def rotate1(self, deg) :
        self.image= pygame.transform.rotate(self.start_image, deg)
        self.rect=self.image.get_rect(center=(self.x,self.y))
    def draw(self):
        screen.blit(self.image,self.rect)
a,Q=0,20
z=0
x_mouse=0
y_mouse=0
degree=[0]*Q
deltaX,deltaY=[0]*Q,[0]*Q

flyy=[0]*Q
for i in range(Q):
    #flyy[i]=Flyy('ladybug2.png',40,100,1000) #random borders!!!!!!!!!!!!!
    flyy[i]=Flyy('bfly1.png',40,100,1000) #random borders!!!!!!!!!!!!!
while True:
    #screen.fill('green')
    screen.blit(bgr,(0,0))
    if a==0 and z==0:
        for i in range(Q):
            flyy[i].update()
            flyy[i].borders(90,1100,0,0)
            flyy[i].rotate()
            flyy[i].draw()
            
    if a==0 and z==1:
        screen.blit(light,rect)
        
        
        for i in range(Q):
            flyy[i].update()
            flyy[i].borders(150,150,x_mouse,y_mouse)
            flyy[i].rotate()
            flyy[i].draw()
 
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            exit()
    if event.type == pygame.MOUSEBUTTONDOWN :
        (x0, y0) = pygame.mouse.get_pos()#позиция мыши
        x_mouse=x0
        y_mouse=y0
        a=1
        rect=light.get_rect(center=(x0,y0))
        screen.blit(light,rect)
        
        for i in range (Q):
            deltaY[i]=-(y0-flyy[i].y)
            deltaX[i]=x0-flyy[i].x
            degree[i]=atan2(deltaY[i],deltaX[i])*180/3.14159-90
    if a==1:
        rect=light.get_rect(center=(x0,y0))
        screen.blit(light,rect)
        for i in range (Q):
            flyy[i].rotate1(degree[i])
            flyy[i].move(deltaX[i]/80,-deltaY[i]/80)
            flyy[i].draw()
            if ((flyy[i].x-x0)*(flyy[i].x-x0)+(flyy[i].y-y0)*(flyy[i].y-y0))<200:
                a,z=0,1
    if a==0 and z==0:
        clock.tick(30)
    if a==0 and z==1:
        clock.tick(10)
        
    button=pygame.key.get_pressed()
    if button[pygame.K_SPACE]:
        a,z=0,0
    pygame.display.update()
