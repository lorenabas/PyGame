import pygame as p 

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
        self.rect.center = (self.x, self.y)
    
    def moviment(self):
        keys = p.key.get_pressed()
        if keys[p.K_LEFT]:
            self.x -=self.vel
        
        elif keys[p.K_RIGHT]:
            self.x += self.vel

        if keys[p.K_UP]:
            self.y -= self.val

        elif keys[p.K_DOWN]:
            self.y += self.val

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
             self_vel = 5
        
        self.y = HEIGHT/2
        self.width = 100
        self.height = 150
        self.image = p.transform.scale(self.image, (self.width, self.height))
        self.retangulo = self.image.get_rect()


    def update(self):
        self.movimento()
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
    
    def movimento(self):
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
        score_text = score_font.render(str(SCORE) + ' / 5', True, (0,0,0))
        win.blit(score_text(255,10))

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

run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    
    tela_group.draw(win)

    ScoreDisplay()
    checkFlags()

    student_group.draw(win)
    carro_group.draw(win)

    student_group.update()
    carro_group.update()
    tela_group.update()
    ScoreDisplay()
    p.display.update()

    

p.quit()