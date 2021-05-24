import pygame as p 
import time

class Student(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = HEIGHT / 2
        self.vel = 4
        self.weigh = 100
        self.height = 50 

        self.student1 = p.image.load('student1.png')
        self.student2 = p.image.load('student2.png')
        self.student1 = p.transform.scale(self.student1, (self.widht, self.hight))

        self.image = self.student1
        self.rect = self.image.get_rect()
        self.mask = p.mask.from_surface(self.image)
          
    def update(self):
        self.movement()
        self.correction()
        self.VerificaColisao()
        self.rect.center = (self.x, self.y)
        
    
    def movement(self):
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            self.x -=self.vel
        
        elif keys[p.K_RIGHT]:
            self.x += self.vel

        if keys[p.K_UP]:
            self.y -= self.val

        elif keys[p.K_DOWN]:
            self.y += self.val

    def VerificaColisao(self):
        carro_check = p.sprite.spritecollide(self, carro_group, False, p.sprite.collide_mask)
        if carro_check:
            explosao.explodir(self.x, self.y)


class Carro(p.sprite.Sprite):
    def __init__(self, number):
        super().__init()
        if number == 1:
            self.x = 190
            self.image = p.image.load('Carro_PI.png')
            self.vel = -4

        else:
             self.x = 460
             self.image = p.image.load('Carro_DP.png')
             self.vel = 5
        
        self.y = HEIGHT/2
        self.width = 100
        self.height = 150
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.retangulo = self.image.get_rect()


    def update(self):
        self.movement()
        self.rect.center = (self.x, self.y)
    
        def SwitchLevel():
            global SCORE

            if carro_pi.vel < 0:
               carro_pi.vel -= 1
        
            else:
                carro_pi.vel += 1

            if carro_dp.vel < 0:
                carro_dp.vel -= 1
        
            else:
                carro_dp.vel += 1

            SCORE += 1
    
    def movement(self):
        self.y += self.vel
        if self.y - self.height/2 < 0:
            self.y = self.height/2
            self.vel *= -1

        elif self.y + self.height/2 > HEIGHT:
            self.y = HEIGHT - self.height/2
            self.vel *= -1

class Tela(p.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img1 = p.image.load('Scene.png')
        self.img2 = p.image.load('You win.png')
        self.img3 = p.image.load('You loose.png')
        
        self.img1 = p.transform.scale(self.img1(WIDTH,HEIGHT))
        self.img2 = p.transform.scale(self.img2(WIDTH,HEIGHT))
        self.img3 = p.transform.scale(self.img3(WIDTH,HEIGHT))
        
        self.image = self.img1
        self.x = 0
        self.y = 0
        
        self.rect = self.image.get_rect()
        
    def updade(self):
        self.rect.topleft = (self.x,self.y)

class Flag(p.sprite.Sprite):
    def __init__(self,number):
        super().__init__()
        self.number = number
        
        if self.number == 1:
            self.image = p.image.load('Green flag.png') 
            self.visible = False
            self.x = 50
        else:
            self.image = p.image.load('White flag.png') 
            self.visible = True
            self.x = 580
            
        self.y = HEIGHT/2
        self.image = p.transforme.scale2x(self.image)
        self.rect = self.image.get_rect()
        
    def update(self):
        if self.visible:
            self.rect.center = (self.x,self.y)
    
    def checkFlags():
        for flag in flags:
            if not flag.visiable:
                flag.kill()

            else:
                if not flag.alive():
                    flag_group.add(flag)
    
    def ScoreDisplay():
        global gameOn
        if gameOn:
            score_text = score_font.render(str(SCORE) + ' / 5', True, (0,0,0))
            win.blit(score_text(255,10))
        

def DeleteStudent():
    global student

    student.kill()
    tela_group.draw(win)
    carro_group.draw(win)
    flag_group.draw(win)

    tela_group.update()
    carro_group.update()
    flag_group.update()

    p.display.update()

def DeleteOutrosItems():
    carro_group.empty()
    flag_group.empty()
    flags.clear()

def collision(self):
    global SCORE, student
    flag_hit = p.sprite.spritecollide(self, student_group, False, p.sprite.collide_mask)
    if flag_hit:
        self.visiable = False
    if self.number == 1:
        white_flag.visiable = True
    if SCORE < 5:
        SwitchLevel()
    else:
        cat_group.empty()
        DeleteOtherItems()
        EndScreen(1)
    else:
        green_flag.visiable = True

def EndScreen(n):
    global gameOn
    gameOn = False
    if n == 0:
        bg.image = bg.img3
    elif n == 1:
        bg.image = gb.img2



class Explosao(object):
    def __init__(self):
        self.costume = 1
        self.width = 140
        self.height = 140
        self.image = p.image.load('explosao' + str(self.costume) + '.png')
        self.image = p.transform.scale(self.image, (self.width, self.height))

    def explodir(self, x, y):
        x = x - self.width/2
        y = y - self.height/2
        DeleteStudent()

        while self.costume < 9:
            self.image = p.image.load('explosao' + str(self.costume) + '.png')
            self.image = p.transform.scale(self.image, (self.width, self.height))
            win.blit(self.image, (x, y))
            p.display.update()

            self.costume += 1
            time.sleep(0.1)
        
        DeleteOutrosItems()
        EndScreen(0)

WIDTH = 640
HEIGHT = 480

p.init()

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_captions('Crossy Road')
clock = p.time.Clock()
SCORE = 0
score_font = p.font.SysFont('comicsans',8, True)

bg = Tela()
tela_group = p.sprite.Group()
tela_group.add(bg)

student = Student()
student_group = p.sprite.Group()
student_group.add(student)

carro_pi = Carro(1)
carro_dp = Carro(2)
carro_group = p.sprite.Group()
carro_group.add(carro_pi, carro_dp)

green_flag = Flag(1)
white_flag = Flag(2)
flag_group = p.sprit.Group()
flag_group.add(green_flag, white_flag)
flags = [green_flag, white_flag]

explosao = Explosao()
gameOn = True

run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    
    tela_group.draw(win)

    ScoreDisplay()
    checkFlags()

    carro_group.draw(win)
    student_group.draw(win)
    flag_group.draw(win)

    carro_group.update()
    student_group.update()
    tela_group.update()

    p.display.update()


p.quit()