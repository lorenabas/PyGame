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
    
    def movimento(self):
        self.y += self.vel
        if self.y - self.height/2 < 0:
            self.y = self.height/2
            self.vel *= -1

        elif self.y + self.height/2 > HEIGHT:
            self.y = HEIGHT - self.height/2
            self.vel *= -1


WIDTH = 640
HEIGHT = 480

p.init()

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_captions('Crossy Road')
clock = p.time.Clock()

student = Student()
student_group = p.sprite.Group()
student_group.add(student)

carro_pi = Carro(1)
carro_dp = Carro(2)
carro_group = p.sprite.Group()
carro_group.add(carro_pi, carro_dp)

run = True
while run:
    clock.tick(60)
    for event in p.event.get():
        if event.type == p.QUIT:
            run = False

    screen_group.draw(win)

    ScoreDisplay()
    checkFlags()


    win.fill((0, 255, 0))

    student_group.draw(win)
    carro_group.draw(win)

    student_group.update()
    carro_group.update()
    p.display.update()

    

p.quit()