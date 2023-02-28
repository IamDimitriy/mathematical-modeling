import pygame
import constants as const

pygame.init()
pygame.font.init()


class Info_panel(pygame.sprite.Sprite):  # выводит табличку с характеристиками объекта

    def __init__(self, obj, screen):
        # инициализация бактерии
        # инициализатор встроенных классов Sprite
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((const.table_size_x, const.table_size_y))
        self.image.fill(const.GRAY)
        self.rect = self.image.get_rect()
        # get_rect() оценивает изображение image и высчитывает прямоугольник, способный окружить его
        self.screen_rect = screen.get_rect()
        # размещаем плашку рядом с бактерией, но таким образом, чтоб она не выходила за экран
        if obj.rect.centerx > const.BOX_WIGHT/2:
            if obj.rect.centery > const.BOX_HEIGHT/2:
                self.rect.centerx = obj.rect.centerx - const.table_size_x/2
                self.rect.centery = obj.rect.centery - const.table_size_y/2
            else:
                self.rect.centerx = obj.rect.centerx - const.table_size_x/2
                self.rect.centery = obj.rect.centery + const.table_size_y/2
        if obj.rect.centerx < const.BOX_WIGHT/2:
            if obj.rect.centery > const.BOX_HEIGHT/2:
                self.rect.centerx = obj.rect.centerx + const.table_size_x/2
                self.rect.centery = obj.rect.centery - const.table_size_y/2
            else:
                self.rect.centerx = obj.rect.centerx + const.table_size_x/2
                self.rect.centery = obj.rect.centery + const.table_size_y/2
        self.text = "Energy = %d \nSpeed = %d \nCRISPR/Cas = %d \nimmunity = %d\n resist = %d" % (
            int(obj.eng), (abs(obj.const_change_x) + abs(obj.const_change_x)
                           ), obj.st_crispr_cas, int(obj.immunity), int(obj.resist))

    def vizualize_text(self, screen):
        blit_text(screen, self.text, (self.rect.centerx - const.table_size_x /
                                      2+5, self.rect.centery - const.table_size_y/2 + 2))

    def __del__(self):  # деструктор
        pass

    def output(self, screen):
        # вывод на экран
        self.screen.blit(self.image, self.rect, self.text)
        self.vizualize_text(screen)

    def update(self, screen):
        self.vizualize_text(screen)


# для отображения многострочных текстов
def blit_text(surface, text, pos, font=const.font, color=const.WHITE):
    # 2D array where each row is a list of words.
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The BOX_WIGHT of a space.
    max_wight, max_hight = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_wight, word_hight = word_surface.get_size()
            if x + word_wight >= max_wight:
                x = pos[0]  # Reset the x.
                y += word_hight  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_wight + space
        x = pos[0]  # Reset the x.
        y += word_hight  # Start on new row.
