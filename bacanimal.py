import pygame
from constants import *


class Bacteria(pygame.sprite.Sprite):
    # поведение бактерии
    # конструктор класса

    def __init__(self, resist, immunity, crispr_cas, crispr, img, x, y):

        pygame.sprite.Sprite.__init__(self)
        # загрузка избражения
        self.img = img
        self.image = pygame.image.load(self.img).convert_alpha()
        self.image_orig = self.image  # оригинальное изображение. Нужно для поворотов
        # положение  в мире (х,у)
        # self.image.set_colorkey(WHITE)  # игнорить (цвет) заливки
        self.rect = self.image.get_rect()
        self.const_change_x = random.randint(-4, 4)
        self.const_change_y = random.randint(-4, 4)
        self.eng = 100
        self.rect = self.image.get_rect()
        # get_rect() оценивает изображение image и высчитывает прямоугольник, способный окружить его
        self.screen_rect = screen.get_rect()
        self.rect.center = (random.uniform(0, 1)*BOX_WIGHT,
                            random.uniform(0, 1)*BOX_HEIGHT)
        self.rect.x = x
        self.rect.y = y
        mutation = random.uniform(-0.005, 0.005)
        self.resist = resist+mutation
        self.immunity = immunity+mutation
        self.st_crispr_cas = crispr_cas
        self.crispr = crispr
        self.lifetime = 0  # время жизни
        self.last_move = 0

    def infection(self, x, y):
        global quantity
        ingress = fac.ingress
        suppression = fac.suppression
        # crispr/cashits = pygame.sprite.groupcollide(non_crispr or crispr_bacs, red_facs, False, True)
        hits = pygame.sprite.groupcollide(norm_bacs, red_facs, False, True)
        if hits:
            """ 
            тестовая версия определения заражения нормальным распределением. 
            мб sigma = self.mutation?
            """
            penetration = random.normalvariate(
                ingress, sigma=0.3) - random.normalvariate(self.resist, sigma=0.3)
            if penetration >= 0:
                infection = random.normalvariate(
                    suppression, sigma=0.2) - random.normalvariate(self.immunity, sigma=0.2)
                if not fac.color in self.crispr:
                    if infection >= 0:
                        # кол-во, фагов новых
                        quantity = int(abs(1-infection * 10*2))
                        self.kill()  # - нужно заменить здорового спрайта на инфицированного
                        img = dir + r'\спрайты\sprites\bacs\RED_bac.png'
                        bac = Bacteria(self.resist, self.immunity, False,
                                       crispr_def, img, x, y)
                        inf_bacs.add(bac)
                        all_sprites.add(bac)
                        bacs.add(bac)
                    else:
                        if self.st_crispr_cas == True:
                            self.crispr.append(fac.color)

        hits = pygame.sprite.groupcollide(norm_bacs, yellow_facs, False, True)
        if hits:
            penetration = random.normalvariate(
                ingress, sigma=0.3) - random.normalvariate(self.resist, sigma=0.3)
            if penetration >= 0:
                infection = random.normalvariate(
                    suppression, sigma=0.2) - random.normalvariate(self.immunity, sigma=0.2)
                if not fac.color in self.crispr:
                    if infection >= 0:
                        # кол-во, фагов новых
                        quantity = int(abs(1-infection * 10*2))
                        self.kill()
                        img = dir + r'\спрайты\sprites\bacs\YELLOW_bac.png'
                        bac = Bacteria(self.resist, self.immunity, False,
                                       crispr_def, img, x, y)
                        inf_bacs.add(bac)
                        all_sprites.add(bac)
                        bacs.add(bac)
                    else:
                        if self.st_crispr_cas == True:
                            self.crispr.append(fac.color)

        hits = pygame.sprite.groupcollide(norm_bacs, violet_facs, False, True)
        if hits:
            penetration = random.normalvariate(
                ingress, sigma=0.3) - random.normalvariate(self.resist, sigma=0.3)
            if penetration >= 0:
                infection = random.normalvariate(
                    suppression, sigma=0.2) - random.normalvariate(self.immunity, sigma=0.2)
                if not fac.color in self.crispr:
                    if infection >= 0:
                        # кол-во, фагов новых
                        quantity = int(abs(1-infection * 10*2))
                        self.kill()
                        img = dir + r'\спрайты\sprites\bacs\VIOLET_bac.png'
                        bac = Bacteria(self.resist, self.immunity, False,
                                       crispr_def, img, x, y)
                        inf_bacs.add(bac)
                        all_sprites.add(bac)
                        bacs.add(bac)
                    else:
                        if self.st_crispr_cas == True:
                            self.crispr.append(fac.color)
        return (quantity)

    def eating(self, eng):
        am_eng = eng
        eat_energy = eat.energy
        hits = pygame.sprite.groupcollide(norm_bacs, eats, False, True)
        if hits:
            am_eng += eat_energy
        else:
            am_eng += 0
        return (am_eng)

    def duplication(self, resist, immunity, duplic_x, duplic_y, crispr):
        # choice_list = ['yes', 'no', 'none']
        # if choice_list == 'yes':
        self.eng = self.eng/2 + (self.eng % 2)
        # положение  в мире (х,у)
        x = duplic_x
        y = duplic_y
        new_bac = Bacteria(
            resist, immunity, self.st_crispr_cas, crispr, img_normal, x, y)
        all_sprites.add(new_bac)
        bacs.add(new_bac)
        if self.st_crispr_cas == True:
            crispr_bacs.add(new_bac)
        elif self.st_crispr_cas == False:
            non_crispr.add(new_bac)
        norm_bacs.add(new_bac)
        return self.eng

    def rotation(self, angle):  # поворот
        self.image = pygame.transform.rotate(self.image_orig, angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self):
        choice_list = ['self.change_x', 'self.change_y', 'none', 'change']
        name = random.choice(choice_list)  # выбор стороны движения
        self.old_eng = self.eng
        self.eng = self.eating(self.eng)
        move = random.randrange(1, 12)  # случайный поворот по 4 направлениям
        if (move > 5):
            move = self.last_move
        if (1 == move):  # стоп
            self.rect.x += 0
        elif (2 == move):
            self.rotation(90)
            self.rect.x += self.const_change_x
        elif (3 == move):  # вниз
            self.rotation(90)
            self.rect.y -= self.const_change_y
        elif (4 == move):  # вверх
            self.rotation(-90)
            self.rect.y += self.const_change_y
        elif (5 == move):
            self.rotation(180)
            self.rect.x -= self.const_change_x
        self.last_move = move
        # движение
        if name == "self.change_x":
            try:
                sign_x = self.const_change_x / abs(self.const_change_x)
            except ZeroDivisionError:
                sign_x = 1
            try:
                sign_y = self.const_change_y / abs(self.const_change_y)
            except ZeroDivisionError:
                sign_y = 1
            for i in range(0, 3):
                self.change_x = random.randint(-2, 2) * \
                    sign_x + self.const_change_x * 2
                self.change_y = random.randint(-2, 2) * \
                    sign_y + self.const_change_y
                self.rect.x += self.change_x
                self.rect.y += self.change_y
                # проверка побега за границу
                if self.rect.x >= BOX_WIGHT-20 or self.rect.x <= 0:
                    self.const_change_x = random.randint(-4, 4)
                    self.rect.x -= self.change_x
                elif self.rect.y >= BOX_HEIGHT-20 or self.rect.y <= 0:
                    self.const_change_y = random.randint(-4, 4)
                    self.rect.y -= self.change_y
                self.eng -= (abs(self.change_x)+abs(self.change_y))/20
                # проверка разумности передвижения, подталкивающая бактерий ползти в неизвестность
                if self.eng >= self.old_eng - satiety:
                    choice_list.append(name)
                else:
                    choice_list.remove(name)
                i += 1
        elif name == "self.change_y":
            try:
                sign_x = self.const_change_x / abs(self.const_change_x)
            except ZeroDivisionError:
                sign_x = 1
            try:
                sign_y = self.const_change_y / abs(self.const_change_y)
            except ZeroDivisionError:
                sign_y = 1
            for i in range(0, 3):
                self.change_x = random.randint(-2, 2) * \
                    sign_x + self.const_change_x
                self.change_y = random.randint(-2, 2) * \
                    sign_y + self.const_change_y * 2
                self.rect.x += self.change_x
                self.rect.y += self.change_y
                if self.rect.x >= BOX_WIGHT-20 or self.rect.x <= 0:
                    self.const_change_x = random.randint(-4, 4)
                    self.rect.x -= self.change_x
                elif self.rect.y >= BOX_HEIGHT-20 or self.rect.y <= 0:
                    self.const_change_y = random.randint(-4, 4)
                    self.rect.y -= self.change_y
                self.eng -= (abs(self.change_x)+abs(self.change_y)) / \
                    20  # проверка разумности передвижения
                if self.eng >= self.old_eng - satiety:
                    choice_list.append(name)
                else:
                    choice_list.remove(name)
                i += 1
        elif name == "none":
            self.rect.x += 0
            self.rect.y += 0
            self.eng -= 0
            # проверка разумности передвижения, подталкивающая бактерий ползти в неизвестность
            if self.eng >= self.old_eng - satiety:
                choice_list.append(name)
            else:
                choice_list.remove(name)
        else:
            self.const_change_x = random.randint(-4, 4)
            self.const_change_y = random.randint(-4, 4)
        duplic_x = self.rect.x
        duplic_y = self.rect.y
        self.quantity = self.infection(duplic_x, duplic_y)
        crspr = self.crispr
        if self.eng >= 200:
            # проверка заразности, инф. множиться не могут
            if self in norm_bacs:
                self.eng = self.duplication(self.resist, self.immunity,
                                            duplic_x, duplic_y, crspr)
        if self.eng >= 1000:
            print("ПОЧМУ я СТАРА")
            self.eng = self.duplication(self.resist, self.immunity,
                                        duplic_x, duplic_y, crspr)
        if self.eng < 0:
            if self.img == img_normal:
                self.kill()
                x = self.rect.x
                y = self.rect.y
                eat = Eat(GRAY, x, y)
                all_sprites.add(eat)
                eats.add(eat)
            elif self.img == dir + r'\спрайты\sprites\bacs\RED_bac.png':
                self.kill()
                x = self.rect.x
                y = self.rect.y
                for i in range(0, self.quantity):
                    color = RED
                    fac = Bacteriophage(
                        color, x=x+random.randrange(-20, 20), y=y+random.randrange(-20, 20))
                    all_sprites.add(fac)
                    red_facs.add(fac)
                    i += 1
            elif self.img == dir + r'\спрайты\sprites\bacs\YELLOW_bac.png':
                self.kill()
                x = self.rect.x
                y = self.rect.y
                for i in range(0, self.quantity):
                    color = YELLOW
                    fac = Bacteriophage(
                        color, x=x+random.randrange(-40, 40), y=y+random.randrange(-40, 40))
                    all_sprites.add(fac)
                    red_facs.add(fac)
                    i += 1
            elif self.img == dir + dir + r'\спрайты\sprites\bacs\VIOLET_bac.png':
                self.kill()
                x = self.rect.x
                y = self.rect.y
                for i in range(0, self.quantity):
                    color = VIOLET
                    fac = Bacteriophage(
                        color, x=x+random.randrange(-40, 40), y=y+random.randrange(-40, 40))
                    all_sprites.add(fac)
                    red_facs.add(fac)
                    i += 1
        self.lifetime += 1  # время жизни


class Bacteriophage(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        self.ingress = random.uniform(0, 1.2)
        self.suppression = random.uniform(0, 1.2)
        pygame.sprite.Sprite.__init__(self)
        self.color = color
        if self.color == RED:
            self.img = dir + r"\спрайты\sprites\facs\RED_fac.png"
        if self.color == VIOLET:
            self.img = dir + r"\спрайты\sprites\facs\VIOLET_fac.png"
        if self.color == YELLOW:
            self.img = dir + r"\спрайты\sprites\facs\YELLOW_fac.png"
        self.image = pygame.image.load(self.img).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        choice_list = ['self.change_x', 'self.change_y', 'none']
        self.name = random.choice(choice_list)  # выбор стороны движения

    def update(self):
        if self.name == "self.change_x":
            self.change_x = random.randint(-1, 1)*2
            self.change_y = random.randint(-1, 1)
            for i in range(random.randint(0, 2)):
                self.rect.x += self.change_x
                self.rect.y += self.change_y
                i += 1
                if self.rect.x > BOX_WIGHT-30 or self.rect.x < 0:
                    self.rect.x -= self.change_x
                elif self.rect.y > BOX_HEIGHT - 30 or self.rect.y < 0:
                    self.rect.y -= self.change_y
        elif self.name == "self.change_y":
            self.change_y = random.randint(-1, 1)*2
            self.change_x = random.randint(-1, 1)
            for i in range(random.randint(0, 2)):
                self.rect.x += self.change_x
                self.rect.y += self.change_y
                i += 1
                if self.rect.x > BOX_WIGHT or self.rect.x < 0:
                    self.rect.x -= self.change_x
                elif self.rect.y > BOX_HEIGHT or self.rect.y < 0:
                    self.rect.y -= self.change_y
        else:
            self.rect.x += 0
            self.rect.y += 0


class Eat(pygame.sprite.Sprite):
    def __init__(self, color_eat, x, y):
        self.energy = satiety
        pygame.sprite.Sprite.__init__(self)
        if color_eat == GREEN:
            self.img = dir + r"\спрайты\sprites\eat.png"
            self.image = pygame.image.load(self.img).convert_alpha()
        else:
            color = color_eat
            self.image = pygame.Surface((10, 15))
            self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


resista = random.uniform(0, 1)
immunitya = random.uniform(0, 1)
bac = Bacteria(resista, immunitya, True, crispr_def, img_normal, x, y)
fac = Bacteriophage(color=random.choice(all_color), x=random.randrange(
    0, BOX_WIGHT-20), y=random.randrange(0, BOX_HEIGHT-20))
eat = Eat(color_eat, x, y)
