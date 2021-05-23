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

WIDTH = 640
HEIGHT = 480

p.init()

win = p.display.set_mode((WIDTH, HEIGHT))
p.display.set_captions('Crossy Road')
clock = p.time.Clock()

student = Student()
student_group = p.sprite.Group()
student_group.add(student)

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
    student_group.draw()
    student_group.update()
    p.display.update()

p.quit()